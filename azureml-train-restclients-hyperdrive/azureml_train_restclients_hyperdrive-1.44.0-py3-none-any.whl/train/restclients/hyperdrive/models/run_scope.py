# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RunScope(Model):
    """RunScope.

    :param host:
    :type host: str
    :param subscription_id:
    :type subscription_id: str
    :param resource_group:
    :type resource_group: str
    :param workspace_name:
    :type workspace_name: str
    :param experiment_name:
    :type experiment_name: str
    """

    _validation = {
        'host': {'required': True},
        'subscription_id': {'required': True},
        'resource_group': {'required': True},
        'workspace_name': {'required': True},
        'experiment_name': {'required': True},
    }

    _attribute_map = {
        'host': {'key': 'host', 'type': 'str'},
        'subscription_id': {'key': 'subscription_id', 'type': 'str'},
        'resource_group': {'key': 'resource_group', 'type': 'str'},
        'workspace_name': {'key': 'workspace_name', 'type': 'str'},
        'experiment_name': {'key': 'experiment_name', 'type': 'str'},
    }

    def __init__(self, host, subscription_id, resource_group, workspace_name, experiment_name):
        super(RunScope, self).__init__()
        self.host = host
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.workspace_name = workspace_name
        self.experiment_name = experiment_name
