# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._azure_machine_learning_workspaces_enums import *


class Artifact(msrest.serialization.Model):
    """Details of an Artifact.

    All required parameters must be populated in order to send to Azure.

    :param artifact_id: The identifier of an Artifact. Format of ArtifactId -
     {Origin}/{Container}/{Path}.
    :type artifact_id: str
    :param origin: Required. The origin of the Artifact creation request. Available origins are
     'ExperimentRun', 'LocalUpload', 'WebUpload', 'Dataset' and 'Unknown'.
    :type origin: str
    :param container: Required. The name of container. Artifacts can be grouped by container.
    :type container: str
    :param path: Required. The path to the Artifact in a container.
    :type path: str
    :param etag: The Etag of the Artifact.
    :type etag: str
    :param created_time: The Date and Time at which the Artifact is created. The DateTime is in
     UTC.
    :type created_time: ~datetime.datetime
    :param data_path:
    :type data_path: ~azure.mgmt.machinelearningservices.models.ArtifactDataPath
    :param tags: A set of tags. Dictionary of :code:`<string>`.
    :type tags: dict[str, str]
    """

    _validation = {
        'origin': {'required': True},
        'container': {'required': True},
        'path': {'required': True},
    }

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'container': {'key': 'container', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'data_path': {'key': 'dataPath', 'type': 'ArtifactDataPath'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        origin: str,
        container: str,
        path: str,
        artifact_id: Optional[str] = None,
        etag: Optional[str] = None,
        created_time: Optional[datetime.datetime] = None,
        data_path: Optional["ArtifactDataPath"] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Artifact, self).__init__(**kwargs)
        self.artifact_id = artifact_id
        self.origin = origin
        self.container = container
        self.path = path
        self.etag = etag
        self.created_time = created_time
        self.data_path = data_path
        self.tags = tags


class ArtifactContainerSas(msrest.serialization.Model):
    """Details of the Artifact Container's shared access signature.

    All required parameters must be populated in order to send to Azure.

    :param container_sas: Required. The shared access signature of the Container.
    :type container_sas: str
    :param container_uri: Required. The URI of the Container.
    :type container_uri: str
    :param prefix: The Prefix to the Blobs in the Container.
    :type prefix: str
    :param artifact_prefix: The Prefix to the Artifact in the Blob.
    :type artifact_prefix: str
    """

    _validation = {
        'container_sas': {'required': True},
        'container_uri': {'required': True},
    }

    _attribute_map = {
        'container_sas': {'key': 'containerSas', 'type': 'str'},
        'container_uri': {'key': 'containerUri', 'type': 'str'},
        'prefix': {'key': 'prefix', 'type': 'str'},
        'artifact_prefix': {'key': 'artifactPrefix', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        container_sas: str,
        container_uri: str,
        prefix: Optional[str] = None,
        artifact_prefix: Optional[str] = None,
        **kwargs
    ):
        super(ArtifactContainerSas, self).__init__(**kwargs)
        self.container_sas = container_sas
        self.container_uri = container_uri
        self.prefix = prefix
        self.artifact_prefix = artifact_prefix


class ArtifactContentInformation(msrest.serialization.Model):
    """Details of an Artifact Content Information.

    :param content_uri: The URI of the content.
    :type content_uri: str
    :param origin: The origin of the Artifact creation request. Available origins are
     'ExperimentRun', 'LocalUpload', 'WebUpload', 'Dataset', 'ComputeRecord', 'Metric', and
     'Unknown'.
    :type origin: str
    :param container: The name of container. Artifacts can be grouped by container.
    :type container: str
    :param path: The path to the Artifact in a container.
    :type path: str
    :param tags: A set of tags. The tags on the artifact.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'container': {'key': 'container', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        content_uri: Optional[str] = None,
        origin: Optional[str] = None,
        container: Optional[str] = None,
        path: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(ArtifactContentInformation, self).__init__(**kwargs)
        self.content_uri = content_uri
        self.origin = origin
        self.container = container
        self.path = path
        self.tags = tags


class ArtifactDataPath(msrest.serialization.Model):
    """ArtifactDataPath.

    :param data_store_name:
    :type data_store_name: str
    :param relative_path:
    :type relative_path: str
    :param sql_data_path:
    :type sql_data_path: ~azure.mgmt.machinelearningservices.models.SqlDataPath
    """

    _attribute_map = {
        'data_store_name': {'key': 'dataStoreName', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'sql_data_path': {'key': 'sqlDataPath', 'type': 'SqlDataPath'},
    }

    def __init__(
        self,
        *,
        data_store_name: Optional[str] = None,
        relative_path: Optional[str] = None,
        sql_data_path: Optional["SqlDataPath"] = None,
        **kwargs
    ):
        super(ArtifactDataPath, self).__init__(**kwargs)
        self.data_store_name = data_store_name
        self.relative_path = relative_path
        self.sql_data_path = sql_data_path


class ArtifactIdList(msrest.serialization.Model):
    """Contains list of Artifact Ids.

    All required parameters must be populated in order to send to Azure.

    :param artifact_ids: Required. List of Artifacts Ids.
    :type artifact_ids: list[str]
    """

    _validation = {
        'artifact_ids': {'required': True},
    }

    _attribute_map = {
        'artifact_ids': {'key': 'artifactIds', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        artifact_ids: List[str],
        **kwargs
    ):
        super(ArtifactIdList, self).__init__(**kwargs)
        self.artifact_ids = artifact_ids


class ArtifactPath(msrest.serialization.Model):
    """Details of an Artifact Path.

    All required parameters must be populated in order to send to Azure.

    :param path: Required. The path to the Artifact in a container.
    :type path: str
    :param tags: A set of tags. Dictionary of :code:`<string>`.
    :type tags: dict[str, str]
    """

    _validation = {
        'path': {'required': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        path: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(ArtifactPath, self).__init__(**kwargs)
        self.path = path
        self.tags = tags


class ArtifactPathList(msrest.serialization.Model):
    """Contains list of Artifact Paths.

    All required parameters must be populated in order to send to Azure.

    :param paths: Required. List of Artifact Paths.
    :type paths: list[~azure.mgmt.machinelearningservices.models.ArtifactPath]
    """

    _validation = {
        'paths': {'required': True},
    }

    _attribute_map = {
        'paths': {'key': 'paths', 'type': '[ArtifactPath]'},
    }

    def __init__(
        self,
        *,
        paths: List["ArtifactPath"],
        **kwargs
    ):
        super(ArtifactPathList, self).__init__(**kwargs)
        self.paths = paths


class ArtifactZip(msrest.serialization.Model):
    """ArtifactZip.

    :param friendly_operation_name:
    :type friendly_operation_name: str
    :param content_disposition:
    :type content_disposition: str
    """

    _attribute_map = {
        'friendly_operation_name': {'key': 'friendlyOperationName', 'type': 'str'},
        'content_disposition': {'key': 'contentDisposition', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        friendly_operation_name: Optional[str] = None,
        content_disposition: Optional[str] = None,
        **kwargs
    ):
        super(ArtifactZip, self).__init__(**kwargs)
        self.friendly_operation_name = friendly_operation_name
        self.content_disposition = content_disposition


class ArtifactZipResponse(msrest.serialization.Model):
    """ArtifactZipResponse.

    :param zip_sas_uri:
    :type zip_sas_uri: str
    :param last_modified_time: Last modified time of the zip blob. UX needs it to determine if the
     zip blob is stale enough or not.
    :type last_modified_time: ~datetime.datetime
    """

    _attribute_map = {
        'zip_sas_uri': {'key': 'zipSasUri', 'type': 'str'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        zip_sas_uri: Optional[str] = None,
        last_modified_time: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(ArtifactZipResponse, self).__init__(**kwargs)
        self.zip_sas_uri = zip_sas_uri
        self.last_modified_time = last_modified_time


class BatchArtifactContentInformationResult(msrest.serialization.Model):
    """Results of the Batch Artifact Content Information request.

    :param artifacts: Artifact details of the Artifact Ids requested.
    :type artifacts: dict[str, ~azure.mgmt.machinelearningservices.models.Artifact]
    :param artifact_content_information: Artifact Content Information details of the Artifact Ids
     requested.
    :type artifact_content_information: dict[str,
     ~azure.mgmt.machinelearningservices.models.ArtifactContentInformation]
    :param errors: Errors occurred while fetching the requested Artifact Ids.
    :type errors: dict[str, ~azure.mgmt.machinelearningservices.models.ErrorResponse]
    """

    _attribute_map = {
        'artifacts': {'key': 'artifacts', 'type': '{Artifact}'},
        'artifact_content_information': {'key': 'artifactContentInformation', 'type': '{ArtifactContentInformation}'},
        'errors': {'key': 'errors', 'type': '{ErrorResponse}'},
    }

    def __init__(
        self,
        *,
        artifacts: Optional[Dict[str, "Artifact"]] = None,
        artifact_content_information: Optional[Dict[str, "ArtifactContentInformation"]] = None,
        errors: Optional[Dict[str, "ErrorResponse"]] = None,
        **kwargs
    ):
        super(BatchArtifactContentInformationResult, self).__init__(**kwargs)
        self.artifacts = artifacts
        self.artifact_content_information = artifact_content_information
        self.errors = errors


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    :param type: The additional info type.
    :type type: str
    :param info: The additional info.
    :type info: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        info: Optional[object] = None,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = type
        self.info = info


class ErrorResponse(msrest.serialization.Model):
    """The error response.

    :param error: The root error.
    :type error: ~azure.mgmt.machinelearningservices.models.RootError
    :param correlation: Dictionary containing correlation details for the error.
    :type correlation: dict[str, str]
    :param environment: The hosting environment.
    :type environment: str
    :param location: The Azure region.
    :type location: str
    :param time: The time in UTC.
    :type time: ~datetime.datetime
    :param component_name: Component name where error originated/encountered.
    :type component_name: str
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'RootError'},
        'correlation': {'key': 'correlation', 'type': '{str}'},
        'environment': {'key': 'environment', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'time': {'key': 'time', 'type': 'iso-8601'},
        'component_name': {'key': 'componentName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        error: Optional["RootError"] = None,
        correlation: Optional[Dict[str, str]] = None,
        environment: Optional[str] = None,
        location: Optional[str] = None,
        time: Optional[datetime.datetime] = None,
        component_name: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error
        self.correlation = correlation
        self.environment = environment
        self.location = location
        self.time = time
        self.component_name = component_name


class GetArtifactsByTagsCommand(msrest.serialization.Model):
    """GetArtifactsByTagsCommand.

    :param tags: A set of tags. Dictionary of
     <components·3ah063·schemas·getartifactsbytagscommand·properties·tags·additionalproperties>.
    :type tags: dict[str, list[str]]
    :param continuation_token:
    :type continuation_token: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{[str]}'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, List[str]]] = None,
        continuation_token: Optional[str] = None,
        **kwargs
    ):
        super(GetArtifactsByTagsCommand, self).__init__(**kwargs)
        self.tags = tags
        self.continuation_token = continuation_token


class InnerErrorResponse(msrest.serialization.Model):
    """A nested structure of errors.

    :param code: The error code.
    :type code: str
    :param inner_error: A nested structure of errors.
    :type inner_error: ~azure.mgmt.machinelearningservices.models.InnerErrorResponse
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorResponse'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        inner_error: Optional["InnerErrorResponse"] = None,
        **kwargs
    ):
        super(InnerErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.inner_error = inner_error


class PaginatedArtifactContentInformationList(msrest.serialization.Model):
    """A paginated list of ArtifactContentInformations.

    :param value: An array of objects of type ArtifactContentInformation.
    :type value: list[~azure.mgmt.machinelearningservices.models.ArtifactContentInformation]
    :param continuation_token: The token used in retrieving the next page. If null, there are no
     additional pages.
    :type continuation_token: str
    :param next_link: The link to the next page constructed using the continuationToken.  If null,
     there are no additional pages.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ArtifactContentInformation]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ArtifactContentInformation"]] = None,
        continuation_token: Optional[str] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PaginatedArtifactContentInformationList, self).__init__(**kwargs)
        self.value = value
        self.continuation_token = continuation_token
        self.next_link = next_link


class PaginatedArtifactList(msrest.serialization.Model):
    """A paginated list of Artifacts.

    :param value: An array of objects of type Artifact.
    :type value: list[~azure.mgmt.machinelearningservices.models.Artifact]
    :param continuation_token: The token used in retrieving the next page. If null, there are no
     additional pages.
    :type continuation_token: str
    :param next_link: The link to the next page constructed using the continuationToken.  If null,
     there are no additional pages.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Artifact]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Artifact"]] = None,
        continuation_token: Optional[str] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PaginatedArtifactList, self).__init__(**kwargs)
        self.value = value
        self.continuation_token = continuation_token
        self.next_link = next_link


class RootError(msrest.serialization.Model):
    """The root error.

    :param code: The service-defined error code. Supported error codes: ServiceError, UserError,
     ValidationError, AzureStorageError, TransientError, RequestThrottled.
    :type code: str
    :param severity: The Severity of error.
    :type severity: int
    :param message: A human-readable representation of the error.
    :type message: str
    :param message_format: An unformatted version of the message with no variable substitution.
    :type message_format: str
    :param message_parameters: Value substitutions corresponding to the contents of MessageFormat.
    :type message_parameters: dict[str, str]
    :param reference_code: This code can optionally be set by the system generating the error.
     It should be used to classify the problem and identify the module and code area where the
     failure occured.
    :type reference_code: str
    :param details_uri: A URI which points to more details about the context of the error.
    :type details_uri: str
    :param target: The target of the error (e.g., the name of the property in error).
    :type target: str
    :param details: The related errors that occurred during the request.
    :type details: list[~azure.mgmt.machinelearningservices.models.RootError]
    :param inner_error: A nested structure of errors.
    :type inner_error: ~azure.mgmt.machinelearningservices.models.InnerErrorResponse
    :param additional_info: The error additional info.
    :type additional_info: list[~azure.mgmt.machinelearningservices.models.ErrorAdditionalInfo]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'message_format': {'key': 'messageFormat', 'type': 'str'},
        'message_parameters': {'key': 'messageParameters', 'type': '{str}'},
        'reference_code': {'key': 'referenceCode', 'type': 'str'},
        'details_uri': {'key': 'detailsUri', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[RootError]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorResponse'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        severity: Optional[int] = None,
        message: Optional[str] = None,
        message_format: Optional[str] = None,
        message_parameters: Optional[Dict[str, str]] = None,
        reference_code: Optional[str] = None,
        details_uri: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["RootError"]] = None,
        inner_error: Optional["InnerErrorResponse"] = None,
        additional_info: Optional[List["ErrorAdditionalInfo"]] = None,
        **kwargs
    ):
        super(RootError, self).__init__(**kwargs)
        self.code = code
        self.severity = severity
        self.message = message
        self.message_format = message_format
        self.message_parameters = message_parameters
        self.reference_code = reference_code
        self.details_uri = details_uri
        self.target = target
        self.details = details
        self.inner_error = inner_error
        self.additional_info = additional_info


class SqlDataPath(msrest.serialization.Model):
    """SqlDataPath.

    :param sql_table_name:
    :type sql_table_name: str
    :param sql_query:
    :type sql_query: str
    :param sql_stored_procedure_name:
    :type sql_stored_procedure_name: str
    :param sql_stored_procedure_params:
    :type sql_stored_procedure_params:
     list[~azure.mgmt.machinelearningservices.models.StoredProcedureParameter]
    """

    _attribute_map = {
        'sql_table_name': {'key': 'sqlTableName', 'type': 'str'},
        'sql_query': {'key': 'sqlQuery', 'type': 'str'},
        'sql_stored_procedure_name': {'key': 'sqlStoredProcedureName', 'type': 'str'},
        'sql_stored_procedure_params': {'key': 'sqlStoredProcedureParams', 'type': '[StoredProcedureParameter]'},
    }

    def __init__(
        self,
        *,
        sql_table_name: Optional[str] = None,
        sql_query: Optional[str] = None,
        sql_stored_procedure_name: Optional[str] = None,
        sql_stored_procedure_params: Optional[List["StoredProcedureParameter"]] = None,
        **kwargs
    ):
        super(SqlDataPath, self).__init__(**kwargs)
        self.sql_table_name = sql_table_name
        self.sql_query = sql_query
        self.sql_stored_procedure_name = sql_stored_procedure_name
        self.sql_stored_procedure_params = sql_stored_procedure_params


class StoredProcedureParameter(msrest.serialization.Model):
    """StoredProcedureParameter.

    :param name:
    :type name: str
    :param value:
    :type value: str
    :param type:  Possible values include: "String", "Int", "Decimal", "Guid", "Boolean", "Date".
    :type type: str or ~azure.mgmt.machinelearningservices.models.StoredProcedureParameterType
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        value: Optional[str] = None,
        type: Optional[Union[str, "StoredProcedureParameterType"]] = None,
        **kwargs
    ):
        super(StoredProcedureParameter, self).__init__(**kwargs)
        self.name = name
        self.value = value
        self.type = type
