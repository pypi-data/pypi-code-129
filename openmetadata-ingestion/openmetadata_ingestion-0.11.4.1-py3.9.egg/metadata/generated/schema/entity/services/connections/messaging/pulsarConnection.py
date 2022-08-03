# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/messaging/pulsarConnection.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from .. import connectionBasicType


class PulsarType(Enum):
    Pulsar = 'Pulsar'


class PulsarConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[PulsarType] = Field(
        PulsarType.Pulsar, description='Service Type', title='Service Type'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
