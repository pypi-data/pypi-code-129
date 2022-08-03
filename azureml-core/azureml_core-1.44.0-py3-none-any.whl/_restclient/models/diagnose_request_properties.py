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


class DiagnoseRequestProperties(Model):
    """DiagnoseRequestProperties.

    :param udr: Setting for diagnosing user defined routing
    :type udr: object
    :param nsg: Setting for diagnosing network security group
    :type nsg: object
    :param resource_lock: Setting for diagnosing resource lock
    :type resource_lock: object
    :param dns_resolution: Setting for diagnosing dns resolution
    :type dns_resolution: object
    :param storage_account: Setting for diagnosing dependent storage account
    :type storage_account: object
    :param key_vault: Setting for diagnosing dependent key vault
    :type key_vault: object
    :param container_registry: Setting for diagnosing dependent container
     registry
    :type container_registry: object
    :param others: Setting for diagnosing unclassified category of problems
    :type others: object
    """

    _attribute_map = {
        'udr': {'key': 'udr', 'type': 'object'},
        'nsg': {'key': 'nsg', 'type': 'object'},
        'resource_lock': {'key': 'resourceLock', 'type': 'object'},
        'dns_resolution': {'key': 'dnsResolution', 'type': 'object'},
        'storage_account': {'key': 'storageAccount', 'type': 'object'},
        'key_vault': {'key': 'keyVault', 'type': 'object'},
        'container_registry': {'key': 'containerRegistry', 'type': 'object'},
        'others': {'key': 'others', 'type': 'object'},
    }

    def __init__(self, udr=None, nsg=None, resource_lock=None, dns_resolution=None, storage_account=None, key_vault=None, container_registry=None, others=None):
        super(DiagnoseRequestProperties, self).__init__()
        self.udr = udr
        self.nsg = nsg
        self.resource_lock = resource_lock
        self.dns_resolution = dns_resolution
        self.storage_account = storage_account
        self.key_vault = key_vault
        self.container_registry = container_registry
        self.others = others
