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


class ComputeDatacacheStoreLink(Model):
    """ComputeDatacacheStoreLink.

    :param workspace_id:
    :type workspace_id: str
    :param datacache_store_names:
    :type datacache_store_names: list[str]
    :param compute_target:
    :type compute_target: str
    :param default_datacache_store_name:
    :type default_datacache_store_name: str
    """

    _validation = {
        'datacache_store_names': {'unique': True},
    }

    _attribute_map = {
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'datacache_store_names': {'key': 'datacacheStoreNames', 'type': '[str]'},
        'compute_target': {'key': 'computeTarget', 'type': 'str'},
        'default_datacache_store_name': {'key': 'defaultDatacacheStoreName', 'type': 'str'},
    }

    def __init__(self, workspace_id=None, datacache_store_names=None, compute_target=None, default_datacache_store_name=None):
        super(ComputeDatacacheStoreLink, self).__init__()
        self.workspace_id = workspace_id
        self.datacache_store_names = datacache_store_names
        self.compute_target = compute_target
        self.default_datacache_store_name = default_datacache_store_name
