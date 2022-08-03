# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataProfileDto(Model):
    """DataProfileDto.

    :param profiles:
    :type profiles: list[~_restclient.models.FeatureProfiles]
    """

    _attribute_map = {
        'profiles': {'key': 'profiles', 'type': '[FeatureProfiles]'},
    }

    def __init__(self, *, profiles=None, **kwargs) -> None:
        super(DataProfileDto, self).__init__(**kwargs)
        self.profiles = profiles
