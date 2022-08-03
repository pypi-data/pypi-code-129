# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ArduinoDevicev2propertyvalues(object):
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
        'last_evaluated_key': 'ArduinoDevicev2propertyvaluesLastEvaluatedKey',
        'name': 'str',
        'values': 'list[ArduinoDevicev2propertyvalue]'
    }

    attribute_map = {
        'id': 'id',
        'last_evaluated_key': 'last_evaluated_key',
        'name': 'name',
        'values': 'values'
    }

    def __init__(self, id=None, last_evaluated_key=None, name=None, values=None):  # noqa: E501
        """ArduinoDevicev2propertyvalues - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._last_evaluated_key = None
        self._name = None
        self._values = None
        self.discriminator = None

        self.id = id
        self.last_evaluated_key = last_evaluated_key
        self.name = name
        self.values = values

    @property
    def id(self):
        """Gets the id of this ArduinoDevicev2propertyvalues.  # noqa: E501


        :return: The id of this ArduinoDevicev2propertyvalues.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArduinoDevicev2propertyvalues.


        :param id: The id of this ArduinoDevicev2propertyvalues.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_evaluated_key(self):
        """Gets the last_evaluated_key of this ArduinoDevicev2propertyvalues.  # noqa: E501


        :return: The last_evaluated_key of this ArduinoDevicev2propertyvalues.  # noqa: E501
        :rtype: ArduinoDevicev2propertyvaluesLastEvaluatedKey
        """
        return self._last_evaluated_key

    @last_evaluated_key.setter
    def last_evaluated_key(self, last_evaluated_key):
        """Sets the last_evaluated_key of this ArduinoDevicev2propertyvalues.


        :param last_evaluated_key: The last_evaluated_key of this ArduinoDevicev2propertyvalues.  # noqa: E501
        :type: ArduinoDevicev2propertyvaluesLastEvaluatedKey
        """
        if last_evaluated_key is None:
            raise ValueError("Invalid value for `last_evaluated_key`, must not be `None`")  # noqa: E501

        self._last_evaluated_key = last_evaluated_key

    @property
    def name(self):
        """Gets the name of this ArduinoDevicev2propertyvalues.  # noqa: E501


        :return: The name of this ArduinoDevicev2propertyvalues.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArduinoDevicev2propertyvalues.


        :param name: The name of this ArduinoDevicev2propertyvalues.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def values(self):
        """Gets the values of this ArduinoDevicev2propertyvalues.  # noqa: E501

        ArduinoDevicev2propertyvalueCollection is the media type for an array of ArduinoDevicev2propertyvalue (default view)  # noqa: E501

        :return: The values of this ArduinoDevicev2propertyvalues.  # noqa: E501
        :rtype: list[ArduinoDevicev2propertyvalue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ArduinoDevicev2propertyvalues.

        ArduinoDevicev2propertyvalueCollection is the media type for an array of ArduinoDevicev2propertyvalue (default view)  # noqa: E501

        :param values: The values of this ArduinoDevicev2propertyvalues.  # noqa: E501
        :type: list[ArduinoDevicev2propertyvalue]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

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
        if not isinstance(other, ArduinoDevicev2propertyvalues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
