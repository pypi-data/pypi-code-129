# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from arduino_iot_rest.configuration import Configuration


class BatchQueryRawLastValueRequestMediaV1(object):
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
        'property_id': 'str',
        'thing_id': 'str'
    }

    attribute_map = {
        'property_id': 'property_id',
        'thing_id': 'thing_id'
    }

    def __init__(self, property_id=None, thing_id=None, local_vars_configuration=None):  # noqa: E501
        """BatchQueryRawLastValueRequestMediaV1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._property_id = None
        self._thing_id = None
        self.discriminator = None

        self.property_id = property_id
        self.thing_id = thing_id

    @property
    def property_id(self):
        """Gets the property_id of this BatchQueryRawLastValueRequestMediaV1.  # noqa: E501

        Property id  # noqa: E501

        :return: The property_id of this BatchQueryRawLastValueRequestMediaV1.  # noqa: E501
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this BatchQueryRawLastValueRequestMediaV1.

        Property id  # noqa: E501

        :param property_id: The property_id of this BatchQueryRawLastValueRequestMediaV1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and property_id is None:  # noqa: E501
            raise ValueError("Invalid value for `property_id`, must not be `None`")  # noqa: E501

        self._property_id = property_id

    @property
    def thing_id(self):
        """Gets the thing_id of this BatchQueryRawLastValueRequestMediaV1.  # noqa: E501

        Thing id  # noqa: E501

        :return: The thing_id of this BatchQueryRawLastValueRequestMediaV1.  # noqa: E501
        :rtype: str
        """
        return self._thing_id

    @thing_id.setter
    def thing_id(self, thing_id):
        """Sets the thing_id of this BatchQueryRawLastValueRequestMediaV1.

        Thing id  # noqa: E501

        :param thing_id: The thing_id of this BatchQueryRawLastValueRequestMediaV1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and thing_id is None:  # noqa: E501
            raise ValueError("Invalid value for `thing_id`, must not be `None`")  # noqa: E501

        self._thing_id = thing_id

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
        if not isinstance(other, BatchQueryRawLastValueRequestMediaV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchQueryRawLastValueRequestMediaV1):
            return True

        return self.to_dict() != other.to_dict()
