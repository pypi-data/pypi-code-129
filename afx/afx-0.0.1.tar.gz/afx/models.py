#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import (
  auto,
  Enum
)
from re import sub
from typing import (
  Any,
  Dict,
  List,
  Union
)

from botocore.exceptions import ClientError
from dynamojo import DynamojoBase
from pydantic import validator
from semantic_version import Version

from .globals import (
  BUCKET,
  LOGGER,
  S3
)
from .exceptions import (
  InvalidVersion,
  NotFound,
  StatusError
)

class PackageStatus(Enum):
  available = auto()
  uploading = auto()
  scanning = auto()
  processing = auto()
  invalid = auto()
  quarantine = auto()

  @classmethod
  def is_member(cls, val: Any) -> bool:
    return val in list(cls.__members__.keys())


class ArtifactBase(DynamojoBase):
  tenant: str
  dateTime: str = None
  type: str = None

  class Config:
    validate_assignment = True

  @validator("*", pre=True, always=True)
  def dec_to_int(cls, val: Any) -> Any:
    if isinstance(val, Decimal):
      if str(val).isdigit():
        return int(val)
      else:
        return float(val)
    return val

  @classmethod
  def get_type(cls) -> str:
    return cls.__name__

  def __new__(cls, *args: List[Any], **kwargs: Dict[Any]) -> ArtifactBase:
    cls.type = cls.__name__
    return super().__new__(cls, *args, **kwargs)

  def __init__(self, *args: List[Any], **kwargs: Dict[Any]):
    kwargs["type"] = self.__class__.__name__
    if kwargs.get("dateTime") is None:
      kwargs["dateTime"] = datetime.now().isoformat()
    super().__init__(*args, **kwargs)

  @classmethod
  def fetch(cls, *args: List[Any], **kwargs: Dict[str, Any]) -> ArtifactBase:
    fail = kwargs.get("fail_if_missing", False)
    if "fail_if_missing" in kwargs:
      del kwargs["fail_if_missing"]

    res = super().fetch(*args, **kwargs)

    if not res and fail:
      raise NotFound
    return res


class Package(ArtifactBase):
  status: Union[PackageStatus, str] = PackageStatus.processing
  version: str

  @validator("version")
  def validate_version(cls, version: str) -> str:
    # TF allows prefixing with a "v", which isn't actually a valid semver
    version = sub("^v(.*)", "\1", version)
    try:
      Version(version)
    except ValueError:
      raise InvalidVersion(f"Invalid semantic version string {version}")
    return version

  @validator("status", pre=True, always=True)
  def validate_status(cls, status: Union[PackageStatus, str]) -> str:
    if isinstance(status, PackageStatus):
      status = status.name
    if not PackageStatus.is_member(status):
      raise StatusError(f"Status {status} is not a valid PackageStatus member")
    return status

  def s3_object_exists(self) -> bool:
    try:
      S3.head_object(Bucket=BUCKET, Key=self.key)
    except ClientError as e:
      if e.response['ResponseMetadata']['HTTPStatusCode'] == 404:
        return False
    return True

  def save(self) -> Dict:
    if self.status is None:
      raise StatusError("Cannot save a package without setting the status")
    return super().save()
