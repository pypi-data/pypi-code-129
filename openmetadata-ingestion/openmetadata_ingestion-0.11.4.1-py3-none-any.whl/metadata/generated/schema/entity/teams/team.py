# generated by datamodel-codegen:
#   filename:  schema/entity/teams/team.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference, profile


class Team(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid
    name: basic.EntityName = Field(
        ...,
        description='A unique name of the team typically the team ID from an identity provider. Example - group Id from LDAP.',
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None, description="Name used for display purposes. Example 'Data Science team'."
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the team.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: basic.Href = Field(
        ..., description='Link to the resource corresponding to this entity.'
    )
    profile: Optional[profile.Profile] = Field(
        None, description='Team profile information.'
    )
    users: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Users that are part of the team.'
    )
    owns: Optional[entityReference.EntityReferenceList] = Field(
        None, description='List of entities owned by the team.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this team. '
    )
    isJoinable: Optional[bool] = Field(
        True,
        description='Can any user join this team during sign up? Value of true indicates yes, and false no.',
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    defaultRoles: Optional[entityReference.EntityReferenceList] = Field(
        None,
        description='Default roles of a team. These roles will be inherited by all the users that are part of this team.',
    )
