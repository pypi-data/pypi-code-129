# generated by datamodel-codegen:
#   filename:  schema/entity/tags/tagCategory.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field, constr

from ...type import basic, entityHistory


class TagName(BaseModel):
    __root__: constr(min_length=2, max_length=64) = Field(
        ..., description='Name of the tag.'
    )


class TagCategoryType(Enum):
    Descriptive = 'Descriptive'
    Classification = 'Classification'


class Tag(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of this entity instance.'
    )
    name: TagName = Field(..., description='Name of the tag.')
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this tag category.'
    )
    fullyQualifiedName: Optional[str] = Field(
        None,
        description='Unique name of the tag of format Category.PrimaryTag.SecondaryTag.',
    )
    description: basic.Markdown = Field(
        ..., description='Unique name of the tag category.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to the tag.'
    )
    usageCount: Optional[int] = Field(
        None, description='Count of how many times this tag and children tags are used.'
    )
    deprecated: Optional[bool] = Field(False, description='If the tag is deprecated.')
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    children: Optional[List[Tag]] = Field(
        None,
        description='Tags under this tag group or empty for tags at the leaf level.',
    )


class TagCategory(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of this entity instance.'
    )
    name: TagName
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this tag category.'
    )
    description: basic.Markdown = Field(
        ..., description='Description of the tag category.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    categoryType: TagCategoryType
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to the tag category.'
    )
    usageCount: Optional[int] = Field(
        None,
        description='Count of how many times the tags from this tag category are used.',
    )
    children: Optional[List[Tag]] = Field(None, description='Tags under this category.')
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )


Tag.update_forward_refs()
