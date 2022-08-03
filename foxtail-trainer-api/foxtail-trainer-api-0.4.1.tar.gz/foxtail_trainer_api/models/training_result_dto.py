# coding: utf-8

"""
    Foxtail Trainer

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from foxtail_trainer_api.configuration import Configuration


class TrainingResultDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'training_time_seconds': 'float',
        'training_metrics': 'list[MetricDto]',
        'validation_metrics': 'list[MetricDto]',
        'test_metrics': 'list[MetricDto]',
        'training_history': 'TrainingHistoryDto'
    }

    attribute_map = {
        'id': 'id',
        'training_time_seconds': 'trainingTimeSeconds',
        'training_metrics': 'trainingMetrics',
        'validation_metrics': 'validationMetrics',
        'test_metrics': 'testMetrics',
        'training_history': 'trainingHistory'
    }

    def __init__(self, id=None, training_time_seconds=None, training_metrics=None, validation_metrics=None, test_metrics=None, training_history=None, local_vars_configuration=None):  # noqa: E501
        """TrainingResultDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._training_time_seconds = None
        self._training_metrics = None
        self._validation_metrics = None
        self._test_metrics = None
        self._training_history = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if training_time_seconds is not None:
            self.training_time_seconds = training_time_seconds
        self.training_metrics = training_metrics
        self.validation_metrics = validation_metrics
        self.test_metrics = test_metrics
        if training_history is not None:
            self.training_history = training_history

    @property
    def id(self):
        """Gets the id of this TrainingResultDto.  # noqa: E501


        :return: The id of this TrainingResultDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrainingResultDto.


        :param id: The id of this TrainingResultDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def training_time_seconds(self):
        """Gets the training_time_seconds of this TrainingResultDto.  # noqa: E501


        :return: The training_time_seconds of this TrainingResultDto.  # noqa: E501
        :rtype: float
        """
        return self._training_time_seconds

    @training_time_seconds.setter
    def training_time_seconds(self, training_time_seconds):
        """Sets the training_time_seconds of this TrainingResultDto.


        :param training_time_seconds: The training_time_seconds of this TrainingResultDto.  # noqa: E501
        :type: float
        """

        self._training_time_seconds = training_time_seconds

    @property
    def training_metrics(self):
        """Gets the training_metrics of this TrainingResultDto.  # noqa: E501


        :return: The training_metrics of this TrainingResultDto.  # noqa: E501
        :rtype: list[MetricDto]
        """
        return self._training_metrics

    @training_metrics.setter
    def training_metrics(self, training_metrics):
        """Sets the training_metrics of this TrainingResultDto.


        :param training_metrics: The training_metrics of this TrainingResultDto.  # noqa: E501
        :type: list[MetricDto]
        """

        self._training_metrics = training_metrics

    @property
    def validation_metrics(self):
        """Gets the validation_metrics of this TrainingResultDto.  # noqa: E501


        :return: The validation_metrics of this TrainingResultDto.  # noqa: E501
        :rtype: list[MetricDto]
        """
        return self._validation_metrics

    @validation_metrics.setter
    def validation_metrics(self, validation_metrics):
        """Sets the validation_metrics of this TrainingResultDto.


        :param validation_metrics: The validation_metrics of this TrainingResultDto.  # noqa: E501
        :type: list[MetricDto]
        """

        self._validation_metrics = validation_metrics

    @property
    def test_metrics(self):
        """Gets the test_metrics of this TrainingResultDto.  # noqa: E501


        :return: The test_metrics of this TrainingResultDto.  # noqa: E501
        :rtype: list[MetricDto]
        """
        return self._test_metrics

    @test_metrics.setter
    def test_metrics(self, test_metrics):
        """Sets the test_metrics of this TrainingResultDto.


        :param test_metrics: The test_metrics of this TrainingResultDto.  # noqa: E501
        :type: list[MetricDto]
        """

        self._test_metrics = test_metrics

    @property
    def training_history(self):
        """Gets the training_history of this TrainingResultDto.  # noqa: E501


        :return: The training_history of this TrainingResultDto.  # noqa: E501
        :rtype: TrainingHistoryDto
        """
        return self._training_history

    @training_history.setter
    def training_history(self, training_history):
        """Sets the training_history of this TrainingResultDto.


        :param training_history: The training_history of this TrainingResultDto.  # noqa: E501
        :type: TrainingHistoryDto
        """

        self._training_history = training_history

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrainingResultDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrainingResultDto):
            return True

        return self.to_dict() != other.to_dict()
