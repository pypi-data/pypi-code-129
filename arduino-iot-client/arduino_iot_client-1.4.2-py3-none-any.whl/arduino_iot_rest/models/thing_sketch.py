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


class ThingSketch(object):
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
        'sketch_version': 'str'
    }

    attribute_map = {
        'sketch_version': 'sketch_version'
    }

    def __init__(self, sketch_version=None, local_vars_configuration=None):  # noqa: E501
        """ThingSketch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sketch_version = None
        self.discriminator = None

        if sketch_version is not None:
            self.sketch_version = sketch_version

    @property
    def sketch_version(self):
        """Gets the sketch_version of this ThingSketch.  # noqa: E501

        The autogenerated sketch version  # noqa: E501

        :return: The sketch_version of this ThingSketch.  # noqa: E501
        :rtype: str
        """
        return self._sketch_version

    @sketch_version.setter
    def sketch_version(self, sketch_version):
        """Sets the sketch_version of this ThingSketch.

        The autogenerated sketch version  # noqa: E501

        :param sketch_version: The sketch_version of this ThingSketch.  # noqa: E501
        :type: str
        """
        allowed_values = ["v1", "v2"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sketch_version not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sketch_version` ({0}), must be one of {1}"  # noqa: E501
                .format(sketch_version, allowed_values)
            )

        self._sketch_version = sketch_version

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
        if not isinstance(other, ThingSketch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThingSketch):
            return True

        return self.to_dict() != other.to_dict()
