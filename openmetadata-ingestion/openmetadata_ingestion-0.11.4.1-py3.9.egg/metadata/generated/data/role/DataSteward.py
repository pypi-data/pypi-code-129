# generated by datamodel-codegen:
#   filename:  data/role/DataSteward.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class Model(BaseModel):
    __root__: Any = Field(
        ...,
        description='Users with Data Steward role are responsible for ensuring correctness of metadata for data assets, thereby facilitating data governance principles within the organization.<br/>Data Stewards can update metadata for any entity.',
    )
