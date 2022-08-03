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


class BatchEventCommandResultKvp(Model):
    """BatchEventCommandResultKvp.

    :param key:
    :type key: ~_restclient.models.BaseEventDto
    :param value:
    :type value: ~_restclient.models.ErrorResponse
    """

    _attribute_map = {
        'key': {'key': 'key', 'type': 'BaseEventDto'},
        'value': {'key': 'value', 'type': 'ErrorResponse'},
    }

    def __init__(self, key=None, value=None):
        super(BatchEventCommandResultKvp, self).__init__()
        self.key = key
        self.value = value
