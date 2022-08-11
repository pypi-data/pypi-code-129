import os
from tzlocal import get_localzone_name
from dotenv import load_dotenv


APP_DIRECTORY = os.getenv('CRYTON_CLI_APP_DIRECTORY', os.path.expanduser("~/.cryton-cli/"))

load_dotenv(os.path.join(APP_DIRECTORY, ".env"))
print(os.path.join(APP_DIRECTORY, ".env"))

TIME_ZONE = os.getenv('CRYTON_CLI_TIME_ZONE')
if TIME_ZONE is None or TIME_ZONE.lower() == 'auto':
    TIME_ZONE = get_localzone_name()

API_HOST = os.getenv('CRYTON_CLI_API_HOST')
API_PORT = os.getenv('CRYTON_CLI_API_PORT')
API_SSL = True if os.getenv('CRYTON_CLI_API_SSL').lower() == 'true' else False
API_ROOT = os.getenv('CRYTON_CLI_API_ROOT')
