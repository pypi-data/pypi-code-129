# generated by datamodel-codegen:
#   filename:  schema/entity/services/mlmodelService.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference
from .connections.mlmodel import mlflowConnection, sklearnConnection


class MlModelServiceType(Enum):
    Mlflow = 'Mlflow'
    Sklearn = 'Sklearn'


class MlModelConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    config: Optional[
        Union[mlflowConnection.MlflowConnection, sklearnConnection.SklearnConnection]
    ] = None


class MlModelService(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of this pipeline service instance.'
    )
    name: basic.EntityName = Field(
        ..., description='Name that identifies this pipeline service.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    serviceType: MlModelServiceType = Field(
        ..., description='Type of pipeline service such as Airflow or Prefect...'
    )
    description: Optional[str] = Field(
        None, description='Description of a pipeline service instance.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this pipeline service. It could be title or label from the source services.',
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    pipelines: Optional[entityReference.EntityReferenceList] = Field(
        None,
        description='References to pipelines deployed for this pipeline service to extract metadata',
    )
    connection: MlModelConnection
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this pipeline service.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this pipeline service.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
