# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/database/glueConnection.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from .....security.credentials import awsCredentials
from .. import connectionBasicType


class GlueType(Enum):
    Glue = 'Glue'


class GlueConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[GlueType] = Field(
        GlueType.Glue, description='Service Type', title='Service Type'
    )
    awsConfig: awsCredentials.AWSCredentials = Field(
        ..., title='AWS Credentials Configuration'
    )
    storageServiceName: str = Field(
        ..., description='AWS storageServiceName Name.', title='Storage Service Name'
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
