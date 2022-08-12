# Parts of the code are taken from SpellML library
# I will drop a more details during release
# License Unkown

import re
from git import Repo
from nbox import logger

def get_git_details(folder):
  repo = Repo(folder)

  # check for any unstaged files
  uncommited_files = {}
  diff = repo.index.diff(None)
  for f in diff:
    path = f.a_path or f.b_path # when new file is added, a_path is None
    uncommited_files[path] = f.change_type
  if uncommited_files:
    logger.warning(f"Uncommited files: {uncommited_files}")

  # get the remote url
  try:
    remote_url = repo.remote().url

    # clean the remote_url because it can sometimes contain the repo token as well.
    # this can become security hazard. so if you have an example, that is not suppported:
    #   go ahead, make a PR!
    if "github.com" in remote_url:
      remote_url = re.sub(r"ghp_\w+@", "", remote_url)
  except ValueError:
    remote_url = None

  # get the size of the repository
  size = None
  for line in repo.git.count_objects("-v").splitlines():
    if line.startswith("size:"):
      size = int(line[len("size:") :].strip())
  if size > (1 << 30):
    logger.warning(f"Repository size over 1GB, you might want to work on it")

  return {
    "remote_url": remote_url,
    "branch": repo.active_branch.name,
    "commit": repo.head.commit.hexsha,
    "uncommited_files": uncommited_files,
    "untracked_files": repo.untracked_files,
    "size": size,
  }

