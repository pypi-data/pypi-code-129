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


class OutputData(Model):
    """The configuration of how an output should be created.

    :param output_location: The output location of where the data should be
     written to.
    :type output_location: ~_restclient.models.DataLocation
    :param mechanism: The mechanism by which the output should be uploaded to
     the output location. Possible values include: 'Upload', 'Mount', 'Hdfs',
     'Link'
    :type mechanism: str or ~_restclient.models.OutputMechanism
    :param additional_options: Additional options that controls how the output
     should be uploaded.
    :type additional_options: ~_restclient.models.OutputOptions
    """

    _attribute_map = {
        'output_location': {'key': 'outputLocation', 'type': 'DataLocation'},
        'mechanism': {'key': 'mechanism', 'type': 'OutputMechanism'},
        'additional_options': {'key': 'additionalOptions', 'type': 'OutputOptions'},
    }

    def __init__(self, output_location=None, mechanism=None, additional_options=None):
        super(OutputData, self).__init__()
        self.output_location = output_location
        self.mechanism = mechanism
        self.additional_options = additional_options
