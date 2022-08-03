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


class MetricV2Value(Model):
    """MetricV2Value.

    :param metric_id:
    :type metric_id: str
    :param created_utc:
    :type created_utc: datetime
    :param step:
    :type step: long
    :param data:
    :type data: dict[str, object]
    """

    _attribute_map = {
        'metric_id': {'key': 'metricId', 'type': 'str'},
        'created_utc': {'key': 'createdUtc', 'type': 'iso-8601'},
        'step': {'key': 'step', 'type': 'long'},
        'data': {'key': 'data', 'type': '{object}'},
    }

    def __init__(self, metric_id=None, created_utc=None, step=None, data=None):
        super(MetricV2Value, self).__init__()
        self.metric_id = metric_id
        self.created_utc = created_utc
        self.step = step
        self.data = data
