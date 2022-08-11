from logging import getLogger, StreamHandler
from sys import stdin, stdout
from os import environ

from botocore.config import Config
from boto3 import client


LOGGER = getLogger(__name__)
LOGGER.setLevel("DEBUG")
if stdin.isatty() or environ.get("LOCAL_DEV"):
  LOGGER.info("Logging to stdout")
  LOGGER.addHandler(StreamHandler(stdout))

TENANT = environ["TENANT"]
HOSTNAME = environ["HOSTNAME"]
BASE_URI = environ["BASE_URI"]
BUCKET = environ["BUCKET"]
TABLE = environ["TABLE"]
S3_BOTO_CONFIG = Config(
  signature_version = "s3v4"
)
S3_SIG4 = client("s3", config=S3_BOTO_CONFIG)
S3 = client("s3")
