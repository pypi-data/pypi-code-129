# generated by datamodel-codegen:
#   filename:  schema/type/entityHistory.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Extra, Field, confloat


class EntityVersionHistory(BaseModel):
    class Config:
        extra = Extra.forbid

    entityType: str = Field(
        ...,
        description='Entity type, such as `database`, `table`, `dashboard`, for which this version history is produced.',
    )
    versions: List


class EntityVersion(BaseModel):
    __root__: confloat(ge=0.1, multiple_of=0.1) = Field(
        ...,
        description='Metadata version of the entity in the form `Major.Minor`. First version always starts from `0.1` when the entity is created. When the backward compatible changes are made to the entity, only the `Minor` version is incremented - example `1.0` is changed to `1.1`. When backward incompatible changes are made the `Major` version is incremented - example `1.1` to `2.0`.',
    )


class FieldName(BaseModel):
    __root__: str = Field(..., description='Name of the field of an entity.')


class FieldChange(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[FieldName] = Field(
        None, description='Name of the entity field that changed.'
    )
    oldValue: Optional[Any] = Field(
        None,
        description='Previous value of the field. Note that this is a JSON string and use the corresponding field type to deserialize it.',
    )
    newValue: Optional[Any] = Field(
        None,
        description='New value of the field. Note that this is a JSON string and use the corresponding field type to deserialize it.',
    )


class ChangeDescription(BaseModel):
    class Config:
        extra = Extra.forbid

    fieldsAdded: Optional[List[FieldChange]] = Field(
        None, description='Names of fields added during the version changes.'
    )
    fieldsUpdated: Optional[List[FieldChange]] = Field(
        None,
        description='Fields modified during the version changes with old and new values.',
    )
    fieldsDeleted: Optional[List[FieldChange]] = Field(
        None,
        description='Fields deleted during the version changes with old value before deleted.',
    )
    previousVersion: Optional[EntityVersion] = Field(
        None,
        description='When a change did not result in change, this could be same as the current version.',
    )
