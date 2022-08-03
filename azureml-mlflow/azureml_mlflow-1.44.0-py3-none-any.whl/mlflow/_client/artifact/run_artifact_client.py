# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Access run artifacts client"""
import os
import posixpath
import logging

from azure.core.exceptions import HttpResponseError
from azureml.mlflow._client.artifact.base_artifact_client import BaseArtifactsClient
from azureml.mlflow._restclient.run_artifact._azure_machine_learning_workspaces import \
    AzureMachineLearningWorkspaces as RestRunArtifactsClient
from azureml.mlflow._client.artifact._utils.blob_artifact_util import download_file, upload_blob_from_stream
from azureml.mlflow._restclient.run_artifact.models import ArtifactPathList, ArtifactPath

module_logger = logging.getLogger(__name__)


class RunArtifactsClient(BaseArtifactsClient):
    """
    Run History Artifact Facade APIs

    :param host: The base path for the server to call.
    :type host: str
    :param auth: Authentication for the client
    :type auth: azureml.core.authentication.AbstractAuthentication
    :param subscription_id:
    :type subscription_id: str
    :param resource_group_name:
    :type resource_group_name: str
    :param workspace_name:
    :type workspace_name: str
    :param experiment_name:
    :type experiment_name: str
    """

    def __init__(self,
                 service_context,
                 experiment_name,
                 run_id,
                 path,
                 **kwargs):

        self._client = RestRunArtifactsClient(
            credential=service_context.auth,
            base_url=service_context.host_url,
            credential_scopes=[service_context.cloud._get_default_scope()]
        )
        self._experiment_name = experiment_name
        self._service_context = service_context
        self._run_id = run_id
        self.path = path
        self._kwargs = kwargs

    def upload_artifact(self, local_file, remote_path):
        module_logger.debug("Uploading file {0} to {1}".format(local_file, remote_path))

        with open(local_file, "rb") as file:
            return self._upload_artifact_from_stream(file, remote_path, self._run_id)

    def upload_dir(self, local_dir, artifact_path):
        remote_paths = []
        local_paths = []

        local_dir = os.path.abspath(local_dir)

        for (root, _, filenames) in os.walk(local_dir):
            upload_path = artifact_path
            if root != local_dir:
                rel_path = os.path.relpath(root, local_dir)
                upload_path = posixpath.join(artifact_path, rel_path)
            for f in filenames:
                remote_file_path = posixpath.join(upload_path, f)
                remote_paths.append(remote_file_path)
                local_file_path = os.path.join(root, f)
                local_paths.append(local_file_path)

        result = self._upload_files(local_paths=local_paths, remote_paths=remote_paths)
        return result

    def download_artifact(self, remote_path, local_path):
        """download artifact"""
        try:
            content_info = self._client.run_artifacts.get_content_information(
                subscription_id=self._service_context.subscription_id,
                resource_group_name=self._service_context.resource_group_name,
                workspace_name=self._service_context.workspace_name,
                experiment_name=self._experiment_name,
                run_id=self._run_id,
                path=remote_path
            )

            if not content_info:
                raise Exception("Cannot find the artifact '{0}' in container '{1}'".format(remote_path, self._run_id))
            uri = content_info.content_uri
        except HttpResponseError as operation_error:
            if operation_error.response.status_code == 404:
                existing_files = self.get_file_paths(self._run_id)
                raise Exception("File with path {0} was not found,\n"
                                "available files include: "
                                "{1}.".format(remote_path, ",".join(existing_files)))
            else:
                raise

        download_file(uri, local_path, cloud=self._service_context.cloud)

    def get_file_paths(self):
        """list artifact info"""
        artifacts = self._client.run_artifacts.list_in_container(
            subscription_id=self._service_context.subscription_id,
            resource_group_name=self._service_context.resource_group_name,
            workspace_name=self._service_context.workspace_name,
            experiment_name=self._experiment_name,
            run_id=self._run_id
        )

        return map(lambda artifact_dto: artifact_dto.path, artifacts)

    def _upload_artifact_from_stream(self, stream, name, run_id):
        empty_artifact_res = self._create_empty_artifacts(paths=name, run_id=run_id)
        content_information = empty_artifact_res.artifact_content_information[name]
        upload_blob_from_stream(stream=stream, artifact_uri=content_information.content_uri)
        return empty_artifact_res

    def _create_empty_artifacts(self, paths, run_id):
        if isinstance(paths, str):
            paths = [paths]

        artifacts = [ArtifactPath(path=path) for path in paths]

        response = self._client.run_artifacts.batch_create_empty_artifacts(
            subscription_id=self._service_context.subscription_id,
            resource_group_name=self._service_context.resource_group_name,
            workspace_name=self._service_context.workspace_name,
            experiment_name=self._experiment_name,
            run_id=run_id,
            body=ArtifactPathList(paths=artifacts)
        )

        if response.errors:
            error_messages = []
            for artifact_name in response.errors:
                error = response.errors[artifact_name].error
                error_messages.append("{}: {}".format(error.code,
                                                      error.message))
            raise Exception("\n".join(error_messages))

        return response
