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


class ModelProperty(object):
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
        'max_value': 'float',
        'min_value': 'float',
        'name': 'str',
        'permission': 'str',
        'persist': 'bool',
        'type': 'str',
        'update_parameter': 'float',
        'update_strategy': 'str',
        'variable_name': 'str'
    }

    attribute_map = {
        'max_value': 'max_value',
        'min_value': 'min_value',
        'name': 'name',
        'permission': 'permission',
        'persist': 'persist',
        'type': 'type',
        'update_parameter': 'update_parameter',
        'update_strategy': 'update_strategy',
        'variable_name': 'variable_name'
    }

    def __init__(self, max_value=None, min_value=None, name=None, permission=None, persist=False, type=None, update_parameter=None, update_strategy=None, variable_name=None):  # noqa: E501
        """ModelProperty - a model defined in OpenAPI"""  # noqa: E501

        self._max_value = None
        self._min_value = None
        self._name = None
        self._permission = None
        self._persist = None
        self._type = None
        self._update_parameter = None
        self._update_strategy = None
        self._variable_name = None
        self.discriminator = None

        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        self.name = name
        self.permission = permission
        if persist is not None:
            self.persist = persist
        self.type = type
        if update_parameter is not None:
            self.update_parameter = update_parameter
        self.update_strategy = update_strategy
        if variable_name is not None:
            self.variable_name = variable_name

    @property
    def max_value(self):
        """Gets the max_value of this ModelProperty.  # noqa: E501

        Maximum value of this property  # noqa: E501

        :return: The max_value of this ModelProperty.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this ModelProperty.

        Maximum value of this property  # noqa: E501

        :param max_value: The max_value of this ModelProperty.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def min_value(self):
        """Gets the min_value of this ModelProperty.  # noqa: E501

        Minimum value of this property  # noqa: E501

        :return: The min_value of this ModelProperty.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this ModelProperty.

        Minimum value of this property  # noqa: E501

        :param min_value: The min_value of this ModelProperty.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def name(self):
        """Gets the name of this ModelProperty.  # noqa: E501

        The friendly name of the property  # noqa: E501

        :return: The name of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelProperty.

        The friendly name of the property  # noqa: E501

        :param name: The name of this ModelProperty.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def permission(self):
        """Gets the permission of this ModelProperty.  # noqa: E501

        The permission of the property  # noqa: E501

        :return: The permission of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ModelProperty.

        The permission of the property  # noqa: E501

        :param permission: The permission of this ModelProperty.  # noqa: E501
        :type: str
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501
        allowed_values = ["READ_ONLY", "READ_WRITE"]  # noqa: E501
        if permission not in allowed_values:
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

    @property
    def persist(self):
        """Gets the persist of this ModelProperty.  # noqa: E501

        If true, data will persist into a timeseries database  # noqa: E501

        :return: The persist of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._persist

    @persist.setter
    def persist(self, persist):
        """Sets the persist of this ModelProperty.

        If true, data will persist into a timeseries database  # noqa: E501

        :param persist: The persist of this ModelProperty.  # noqa: E501
        :type: bool
        """

        self._persist = persist

    @property
    def type(self):
        """Gets the type of this ModelProperty.  # noqa: E501

        The type of the property  # noqa: E501

        :return: The type of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelProperty.

        The type of the property  # noqa: E501

        :param type: The type of this ModelProperty.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ANALOG", "CHARSTRING", "FLOAT", "INT", "LENGHT_C", "LENGHT_I", "LENGHT_M", "PERCENTAGE", "STATUS", "TEMPERATURE_C", "TEMPERATURE_F", "METER", "KILOGRAM", "GRAM", "SECOND", "AMPERE", "KELVIN", "CANDELA", "MOLE", "HERTZ", "RADIAN", "STERADIAN", "NEWTON", "PASCAL", "JOULE", "WATT", "COULOMB", "VOLT", "FARAD", "OHM", "SIEMENS", "WEBER", "TESLA", "HENRY", "DEGREES_CELSIUS", "LUMEN", "LUX", "BECQUEREL", "GRAY", "SIEVERT", "KATAL", "SQUARE_METER", "CUBIC_METER", "LITER", "METER_PER_SECOND", "METER_PER_SQUARE_SECOND", "CUBIC_METER_PER_SECOND", "LITER_PER_SECOND", "WATT_PER_SQUARE_METER", "CANDELA_PER_SQUARE_METER", "BIT", "BIT_PER_SECOND", "DEGREES_LATITUDE", "DEGREES_LONGITUDE", "PH_VALUE", "DECIBEL", "DECIBEL_1W", "BEL", "COUNT", "RATIO_DIV", "RATIO_MOD", "PERCENTAGE_RELATIVE_HUMIDITY", "PERCENTAGE_BATTERY_LEVEL", "SECONDS_BATTERY_LEVEL", "EVENT_RATE_SECOND", "EVENT_RATE_MINUTE", "HEART_RATE", "HEART_BEATS", "SIEMENS_PER_METER", "LOCATION", "COLOR_HSB", "COLOR_RGB", "GENERIC_COMPLEX_PROPERTY", "HOME_COLORED_LIGHT", "HOME_DIMMERED_LIGHT", "HOME_LIGHT", "HOME_CONTACT_SENSOR", "HOME_MOTION_SENSOR", "HOME_SMART_PLUG", "HOME_TEMPERATURE", "HOME_SWITCH"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def update_parameter(self):
        """Gets the update_parameter of this ModelProperty.  # noqa: E501

        The update frequency in seconds, or the amount of the property has to change in order to trigger an update  # noqa: E501

        :return: The update_parameter of this ModelProperty.  # noqa: E501
        :rtype: float
        """
        return self._update_parameter

    @update_parameter.setter
    def update_parameter(self, update_parameter):
        """Sets the update_parameter of this ModelProperty.

        The update frequency in seconds, or the amount of the property has to change in order to trigger an update  # noqa: E501

        :param update_parameter: The update_parameter of this ModelProperty.  # noqa: E501
        :type: float
        """

        self._update_parameter = update_parameter

    @property
    def update_strategy(self):
        """Gets the update_strategy of this ModelProperty.  # noqa: E501

        The update strategy for the property value  # noqa: E501

        :return: The update_strategy of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        """Sets the update_strategy of this ModelProperty.

        The update strategy for the property value  # noqa: E501

        :param update_strategy: The update_strategy of this ModelProperty.  # noqa: E501
        :type: str
        """
        if update_strategy is None:
            raise ValueError("Invalid value for `update_strategy`, must not be `None`")  # noqa: E501
        allowed_values = ["ON_CHANGE", "TIMED"]  # noqa: E501
        if update_strategy not in allowed_values:
            raise ValueError(
                "Invalid value for `update_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(update_strategy, allowed_values)
            )

        self._update_strategy = update_strategy

    @property
    def variable_name(self):
        """Gets the variable_name of this ModelProperty.  # noqa: E501

        The  sketch variable name of the property  # noqa: E501

        :return: The variable_name of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this ModelProperty.

        The  sketch variable name of the property  # noqa: E501

        :param variable_name: The variable_name of this ModelProperty.  # noqa: E501
        :type: str
        """
        if variable_name is not None and len(variable_name) > 64:
            raise ValueError("Invalid value for `variable_name`, length must be less than or equal to `64`")  # noqa: E501
        if variable_name is not None and not re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable_name):  # noqa: E501
            raise ValueError(r"Invalid value for `variable_name`, must be a follow pattern or equal to `/^[a-zA-Z_][a-zA-Z0-9_]*$/`")  # noqa: E501

        self._variable_name = variable_name

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
        if not isinstance(other, ModelProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
