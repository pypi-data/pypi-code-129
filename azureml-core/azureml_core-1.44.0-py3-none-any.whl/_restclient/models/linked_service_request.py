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


class LinkedServiceRequest(Model):
    """object used for creating linked service.

    :param name: Friendly name of the linked service
    :type name: str
    :param location: location of the linked service.
    :type location: str
    :param identity:
    :type identity: ~_restclient.models.Identity
    :param properties:
    :type properties: ~_restclient.models.LinkedServiceProps
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'properties': {'key': 'properties', 'type': 'LinkedServiceProps'},
    }

    def __init__(self, name=None, location=None, identity=None, properties=None):
        super(LinkedServiceRequest, self).__init__()
        self.name = name
        self.location = location
        self.identity = identity
        self.properties = properties
