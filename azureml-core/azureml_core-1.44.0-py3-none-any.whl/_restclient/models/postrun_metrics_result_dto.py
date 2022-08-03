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


class PostrunMetricsResultDto(Model):
    """PostrunMetricsResultDto.

    :param errors:
    :type errors: list[~_restclient.models.PostRunMetricsError]
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[PostRunMetricsError]'},
    }

    def __init__(self, errors=None):
        super(PostrunMetricsResultDto, self).__init__()
        self.errors = errors
