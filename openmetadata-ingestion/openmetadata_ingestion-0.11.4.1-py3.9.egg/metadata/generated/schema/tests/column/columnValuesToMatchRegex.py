# generated by datamodel-codegen:
#   filename:  schema/tests/column/columnValuesToMatchRegex.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class ColumnValuesToMatchRegex(BaseModel):
    class Config:
        extra = Extra.forbid

    regex: str = Field(
        ..., description='The regular expression the column entries should match.'
    )
