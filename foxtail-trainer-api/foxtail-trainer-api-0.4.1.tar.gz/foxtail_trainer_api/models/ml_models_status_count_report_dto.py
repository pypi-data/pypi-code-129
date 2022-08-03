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


class MLModelsStatusCountReportDto(object):
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
        'model_status': 'ModelStatus',
        'count': 'int'
    }

    attribute_map = {
        'model_status': 'modelStatus',
        'count': 'count'
    }

    def __init__(self, model_status=None, count=None, local_vars_configuration=None):  # noqa: E501
        """MLModelsStatusCountReportDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_status = None
        self._count = None
        self.discriminator = None

        if model_status is not None:
            self.model_status = model_status
        if count is not None:
            self.count = count

    @property
    def model_status(self):
        """Gets the model_status of this MLModelsStatusCountReportDto.  # noqa: E501


        :return: The model_status of this MLModelsStatusCountReportDto.  # noqa: E501
        :rtype: ModelStatus
        """
        return self._model_status

    @model_status.setter
    def model_status(self, model_status):
        """Sets the model_status of this MLModelsStatusCountReportDto.


        :param model_status: The model_status of this MLModelsStatusCountReportDto.  # noqa: E501
        :type: ModelStatus
        """

        self._model_status = model_status

    @property
    def count(self):
        """Gets the count of this MLModelsStatusCountReportDto.  # noqa: E501


        :return: The count of this MLModelsStatusCountReportDto.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MLModelsStatusCountReportDto.


        :param count: The count of this MLModelsStatusCountReportDto.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if not isinstance(other, MLModelsStatusCountReportDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MLModelsStatusCountReportDto):
            return True

        return self.to_dict() != other.to_dict()
