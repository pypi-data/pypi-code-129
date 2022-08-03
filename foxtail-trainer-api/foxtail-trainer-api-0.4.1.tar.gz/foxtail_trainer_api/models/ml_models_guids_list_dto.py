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


class MLModelsGuidsListDto(object):
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
        'count': 'int',
        'guids': 'list[str]'
    }

    attribute_map = {
        'count': 'count',
        'guids': 'guids'
    }

    def __init__(self, count=None, guids=None, local_vars_configuration=None):  # noqa: E501
        """MLModelsGuidsListDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._guids = None
        self.discriminator = None

        if count is not None:
            self.count = count
        self.guids = guids

    @property
    def count(self):
        """Gets the count of this MLModelsGuidsListDto.  # noqa: E501


        :return: The count of this MLModelsGuidsListDto.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MLModelsGuidsListDto.


        :param count: The count of this MLModelsGuidsListDto.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def guids(self):
        """Gets the guids of this MLModelsGuidsListDto.  # noqa: E501


        :return: The guids of this MLModelsGuidsListDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._guids

    @guids.setter
    def guids(self, guids):
        """Sets the guids of this MLModelsGuidsListDto.


        :param guids: The guids of this MLModelsGuidsListDto.  # noqa: E501
        :type: list[str]
        """

        self._guids = guids

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
        if not isinstance(other, MLModelsGuidsListDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MLModelsGuidsListDto):
            return True

        return self.to_dict() != other.to_dict()
