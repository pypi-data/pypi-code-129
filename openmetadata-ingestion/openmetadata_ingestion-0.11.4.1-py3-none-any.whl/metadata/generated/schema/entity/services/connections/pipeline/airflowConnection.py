# generated by datamodel-codegen:
#   filename:  schema/entity/services/connections/pipeline/airflowConnection.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field

from .. import connectionBasicType
from ..database import (
    mssqlConnection,
    mysqlConnection,
    postgresConnection,
    sqliteConnection,
)
from . import backendConnection


class AirflowType(Enum):
    Airflow = 'Airflow'


class AirflowConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[AirflowType] = Field(
        AirflowType.Airflow, description='Service Type', title='Service Type'
    )
    hostPort: AnyUrl = Field(
        ..., description='Pipeline Service Management/UI URI.', title='Host And Port'
    )
    numberOfStatus: Optional[int] = Field(
        '10', description='Pipeline Service Number Of Status'
    )
    connection: Union[
        backendConnection.BackendConnection,
        mysqlConnection.MysqlConnection,
        postgresConnection.PostgresConnection,
        mssqlConnection.MssqlConnection,
        sqliteConnection.SQLiteConnection,
    ] = Field(
        ...,
        description='Underlying database connection. See https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html for supported backends.',
        title='Metadata Database Connection',
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
