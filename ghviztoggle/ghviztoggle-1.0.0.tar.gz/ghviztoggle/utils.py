from ghviztoggle import __app_name__
import typer
from pathlib import Path
import requests
from configparser import ConfigParser

APP_DIR = Path(typer.get_app_dir(__app_name__))
CONFIG_DIR = APP_DIR / 'config.ini'

def get_repo(repo: str, token: str, owner: str,) -> bool or None:
  url = f'https://api.github.com/repos/{owner}/{repo}'
  headers = {'Authorization': f'token {token}'}
  r = requests.get(url, headers=headers)
  r = r.json()
  if 'message' in r:
    print(f"ERROR: {r['message']}")
    return None
  else:
    return r["private"]

def toggle_vis(repo:str, token:str, owner:str) -> None:
  repo = repo.strip()
  repo_private = get_repo(repo, token, owner)
  if repo_private is None:
    return
  url = f'https://api.github.com/repos/{owner}/{repo}'
  headers = {'Authorization': f'token {token}'}
  data = {'private': not repo_private}
  response = requests.patch(url, headers=headers, json=data)
  response = response.json()
  if 'message' in response:
    print(f"ERROR: {response['message']}")
    return
  new_repo_vis = response["visibility"]
  print(f"Repo \"{repo}\" is now {new_repo_vis}")
  return 

def set_config() -> list:
  APP_DIR.mkdir(exist_ok=True)

  parser = ConfigParser()
  parser.add_section('general')

  token = input("Github token: ").strip()
  owner = input("Github owner: ").strip()

  parser.set('general', 'token', token)
  parser.set('general', 'owner', owner)

  with open(str(CONFIG_DIR), 'w') as configfile:
    parser.write(configfile)

  return (token, owner)

def run() -> None:
  print(str(CONFIG_DIR))
  parser = ConfigParser()
  try:
    parser.read(str(CONFIG_DIR))
  except:
    # create config.ini if it doesn't exist
    with open(str(CONFIG_DIR), 'w') as configfile:
      parser.write(configfile)
  if parser.has_section('general'):
    token = parser.get('general', 'token')
    owner = parser.get('general', 'owner')
  else:
    token, owner = set_config()
    
  while True:
    repo = input('Enter repo name: ')
    toggle_vis(repo, token, owner)
