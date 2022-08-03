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


class Moments(Model):
    """Moments.

    :param mean:
    :type mean: float
    :param standard_deviation:
    :type standard_deviation: float
    :param variance:
    :type variance: float
    :param skewness:
    :type skewness: float
    :param kurtosis:
    :type kurtosis: float
    """

    _attribute_map = {
        'mean': {'key': 'mean', 'type': 'float'},
        'standard_deviation': {'key': 'standardDeviation', 'type': 'float'},
        'variance': {'key': 'variance', 'type': 'float'},
        'skewness': {'key': 'skewness', 'type': 'float'},
        'kurtosis': {'key': 'kurtosis', 'type': 'float'},
    }

    def __init__(self, mean=None, standard_deviation=None, variance=None, skewness=None, kurtosis=None):
        super(Moments, self).__init__()
        self.mean = mean
        self.standard_deviation = standard_deviation
        self.variance = variance
        self.skewness = skewness
        self.kurtosis = kurtosis
