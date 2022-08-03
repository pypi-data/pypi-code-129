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


class ArduinoDevicev2Pass(object):
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
        'set': 'bool',
        'suggested_password': 'str'
    }

    attribute_map = {
        'set': 'set',
        'suggested_password': 'suggested_password'
    }

    def __init__(self, set=None, suggested_password=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoDevicev2Pass - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._set = None
        self._suggested_password = None
        self.discriminator = None

        self.set = set
        if suggested_password is not None:
            self.suggested_password = suggested_password

    @property
    def set(self):
        """Gets the set of this ArduinoDevicev2Pass.  # noqa: E501

        Whether the password is set or not  # noqa: E501

        :return: The set of this ArduinoDevicev2Pass.  # noqa: E501
        :rtype: bool
        """
        return self._set

    @set.setter
    def set(self, set):
        """Sets the set of this ArduinoDevicev2Pass.

        Whether the password is set or not  # noqa: E501

        :param set: The set of this ArduinoDevicev2Pass.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and set is None:  # noqa: E501
            raise ValueError("Invalid value for `set`, must not be `None`")  # noqa: E501

        self._set = set

    @property
    def suggested_password(self):
        """Gets the suggested_password of this ArduinoDevicev2Pass.  # noqa: E501

        A random suggested password  # noqa: E501

        :return: The suggested_password of this ArduinoDevicev2Pass.  # noqa: E501
        :rtype: str
        """
        return self._suggested_password

    @suggested_password.setter
    def suggested_password(self, suggested_password):
        """Sets the suggested_password of this ArduinoDevicev2Pass.

        A random suggested password  # noqa: E501

        :param suggested_password: The suggested_password of this ArduinoDevicev2Pass.  # noqa: E501
        :type: str
        """

        self._suggested_password = suggested_password

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
        if not isinstance(other, ArduinoDevicev2Pass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoDevicev2Pass):
            return True

        return self.to_dict() != other.to_dict()
