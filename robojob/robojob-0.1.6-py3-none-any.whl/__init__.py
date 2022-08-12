import socket
import os

from .backend import SqlServerBackend
from .job_execution import JobExecution, JobException

def go(job_name, config_path=None, environment_name=None, backend=None) -> JobExecution:
    if not config_path and os.path.exists("robojob.yml"):
        config_path = "robojob.yml"

    if config_path:
        import yaml
        with open(config_path, 'rb') as doc:
            config = yaml.safe_load(doc)
    else:
        config = dict()

    return JobExecution(job_name,
                        backend=backend or get_backend_from_config(config),
                        environment_name=environment_name or config.get("environment") or socket.gethostname(),
                        parameters=config.get("parameters", {})
                        )

def get_backend_from_config(config):
    if "backend" in config:
        if "connection string" in config["backend"]:
            import pyodbc
            connection = pyodbc.connect(config["backend"]["connection string"], autocommit=True)
            return SqlServerBackend(connection)
        else:
            raise JobException("Bad backend config")
    else:
        return None
