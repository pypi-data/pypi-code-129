# generated by datamodel-codegen:
#   filename:  schema/security/client/openMetadataJWTClientConfig.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class OpenMetadataJWTClientConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    jwtToken: str = Field(..., description='OpenMetadata generated JWT token.')
