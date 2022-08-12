import os
import re

from json import dumps
from typing import Dict, Any, List, Optional, Union
from nbox.utils import logger, env
from nbox import Instance
from nbox.auth import secret
from nbox.nbxlib.tracer import Tracer
from requests import Session

import dainik.utils as U
from dainik.utils import env
from dainik.lmao_client import *
from dainik.proto.lmao_pb2 import AgentDetails
from dainik.git_utils import get_git_details
from dainik.metrics.system import SystemMetricsLogger

DEBUG_LOG_EVERY = 5
INFO_LOG_EVERY = 100

class Dainik():
  def __init__(self, workspace_id: str, *, local: bool = False) -> None:
    if not local:
      self._create_connection(workspace_id)
    else:
      self.lmao = LMAO_Stub(url = "http://127.0.0.1:8080", session = Session())
    self._initialized = False
    self.nbx_job_folder = env.NBOX_JOB_FOLDER("")
    self._total_logged_elements = 0 # this variable keeps track for logging
    self.completed = False
    self.tracer = None

  def _create_connection(self, workspace_id: str):
    # prepare the URL
    # id_or_name, workspace_id = U.split_iw(instance_id)
    id_or_name = f"monitoring-{workspace_id}"
    logger.info(f"id_or_name: {id_or_name}")
    logger.info(f"workspace_id: {workspace_id}")
    instance = Instance(id_or_name, workspace_id)
    try:
      open_data = instance.open_data
    except AttributeError:
      raise Exception(f"Is instance '{instance.project_id}' running?")
    build = "build"
    if "app.c." in secret.get("nbx_url"):
      build = "build.c"
    url = f"https://server-{open_data['url']}.{build}.nimblebox.ai/"
    logger.info(f"URL: {url}")

    # create a tracer object that will load all the information
    self.tracer = Tracer(start_heartbeat=False)

    # create a session with the auth header
    _session = Session()
    _session.headers.update({
      "NBX-TOKEN": open_data["token"],
      "X-NBX-USERNAME": self.tracer.job_proto.auth_info.username,
    })

    # define the stub
    self.lmao = LMAO_Stub(url = url, session = _session)


  def init(self, project_name: Optional[str] = "", config: Dict[str, Any] = {}, project_id: Optional[str] = ""):
    if project_id:
      project_name = ""
      if project_name:
        logger.info("ignoring `project_name` as `project_id` was given")
    else:
      project_id = ""
      if not project_name:
        raise Exception("Provide one from `project_id` or `project_name`")

    # this is the config value that is used to store data on the plaform, user cannot be allowed to have
    # like a full access to config values
    log_config: Dict[str, Any] = {
      "user_config": config
    }

    # check if the current folder from where this code is being executed has a .git folder
    # NOTE: in case of NBX-Jobs the current folder ("./") is expected to contain git by default
    log_config["git"] = None
    if os.path.exists(".git"):
      log_config["git"] = get_git_details("./")

    # continue as before
    self.project_name = project_name
    self.project_id = project_id
    self.config = config
    self._agent_details = AgentDetails(
      nbx_job_id = self.tracer.job_id if self.tracer else "jj_guvernr",
      nbx_run_id = self.tracer.token if self.tracer else U.get_random_id(),
    )
    run_details = self.lmao.init_run(
      _InitRunRequest = InitRunRequest(
        agent_details=self._agent_details,
        created_at = U.get_timestamp(),
        project_name = self.project_name,
        project_id = self.project_id,
        config = dumps(log_config),
      )
    )

    if not run_details:
      # TODO: Make a custom exception of this
      raise Exception("Server Side exception has occurred, Check the log for details")

    # TODO: change f-string here when refactoring `run_id` to `exp_id`
    logger.info(f"Assigned run_id: {run_details.run_id}")
    self.run = run_details
    self._initialized = True

    # system metrics monitoring, by default is enabled optionally turn it off
    if not env.DK_DISABLE_SYSTEM_METRICS(False):
      SystemMetricsLogger(self)

  def log(self, y: Dict[str, Union[int, float, str]], step = None, *, log_type: str = RunLog.LogType.USER):
    if not self._initialized:
      raise Exception("Run not initialized, call init() first")
    if self.completed:
      raise Exception("Run already completed, cannot log more data!")

    if self._total_logged_elements % DEBUG_LOG_EVERY == 0:
      logger.debug(f"Logging: {y.keys()} | {self._total_logged_elements}")

    if self._total_logged_elements % INFO_LOG_EVERY == 0:
      logger.info(f"Logging: {y.keys()} | {self._total_logged_elements}")

    step = step if step is not None else U.get_timestamp()
    if step < 0:
      raise Exception("Step must be <= 0")
    run_log = RunLog(run_id = self.run.run_id, log_type=log_type)
    for k,v in y.items():
      record = U.get_record(k, v)
      record.step = step
      run_log.data.append(record)

    ack = self.lmao.on_log(_RunLog = run_log)
    if not ack.success:
      logger.error("  >> Server Error")
      for l in ack.message.splitlines():
        logger.error("  " + l)
      raise Exception("Server Error")

    self._total_logged_elements += 1

  def save_file(self, files: List[str]):
    logger.info(f"Saving files: {files}")
    if not self._initialized:
      raise Exception("Run not initialized, call init() first")

    file_list = FileList(run_id=self.run.run_id)
    for f in files:
      # remove path till env.NBOX_JOB_FOLDER, input can contain full path or part of it
      f = os.path.abspath(f)
      assert os.path.exists(f)
      f = re.sub(self.nbx_job_folder, "", f)
      file_list.files.append(File(
        name = f,
        created_at = int(os.path.getctime(f)),
        is_input=False
      ))
    ack = self.lmao.on_save(_FileList = file_list)
    if not ack.success:
      logger.error("  >> Server Error")
      for l in ack.message.splitlines():
        logger.error("  " + l)
      raise Exception("Server Error")

  def end(self):
    logger.info("Ending run")
    ack = self.lmao.on_train_end(_Run = Run(run_id=self.run.run_id,))
    if not ack.success:
      logger.error("  >> Server Error")
      for l in ack.message.splitlines():
        logger.error("  " + l)
      raise Exception("Server Error")
    self.completed = True
