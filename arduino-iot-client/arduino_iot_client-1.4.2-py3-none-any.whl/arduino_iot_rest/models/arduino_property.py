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


class ArduinoProperty(object):
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
        'created_at': 'datetime',
        'deleted_at': 'datetime',
        'href': 'str',
        'id': 'str',
        'last_value': 'object',
        'max_value': 'float',
        'min_value': 'float',
        'name': 'str',
        'permission': 'str',
        'persist': 'bool',
        'sync_id': 'str',
        'tag': 'float',
        'thing_id': 'str',
        'thing_name': 'str',
        'type': 'str',
        'update_parameter': 'float',
        'update_strategy': 'str',
        'updated_at': 'datetime',
        'value_updated_at': 'datetime',
        'variable_name': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'href': 'href',
        'id': 'id',
        'last_value': 'last_value',
        'max_value': 'max_value',
        'min_value': 'min_value',
        'name': 'name',
        'permission': 'permission',
        'persist': 'persist',
        'sync_id': 'sync_id',
        'tag': 'tag',
        'thing_id': 'thing_id',
        'thing_name': 'thing_name',
        'type': 'type',
        'update_parameter': 'update_parameter',
        'update_strategy': 'update_strategy',
        'updated_at': 'updated_at',
        'value_updated_at': 'value_updated_at',
        'variable_name': 'variable_name'
    }

    def __init__(self, created_at=None, deleted_at=None, href=None, id=None, last_value=None, max_value=None, min_value=None, name=None, permission=None, persist=None, sync_id=None, tag=None, thing_id=None, thing_name=None, type=None, update_parameter=None, update_strategy=None, updated_at=None, value_updated_at=None, variable_name=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoProperty - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._deleted_at = None
        self._href = None
        self._id = None
        self._last_value = None
        self._max_value = None
        self._min_value = None
        self._name = None
        self._permission = None
        self._persist = None
        self._sync_id = None
        self._tag = None
        self._thing_id = None
        self._thing_name = None
        self._type = None
        self._update_parameter = None
        self._update_strategy = None
        self._updated_at = None
        self._value_updated_at = None
        self._variable_name = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        self.href = href
        self.id = id
        if last_value is not None:
            self.last_value = last_value
        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        self.name = name
        self.permission = permission
        if persist is not None:
            self.persist = persist
        if sync_id is not None:
            self.sync_id = sync_id
        if tag is not None:
            self.tag = tag
        self.thing_id = thing_id
        if thing_name is not None:
            self.thing_name = thing_name
        self.type = type
        if update_parameter is not None:
            self.update_parameter = update_parameter
        self.update_strategy = update_strategy
        if updated_at is not None:
            self.updated_at = updated_at
        if value_updated_at is not None:
            self.value_updated_at = value_updated_at
        if variable_name is not None:
            self.variable_name = variable_name

    @property
    def created_at(self):
        """Gets the created_at of this ArduinoProperty.  # noqa: E501

        Creation date of the property  # noqa: E501

        :return: The created_at of this ArduinoProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ArduinoProperty.

        Creation date of the property  # noqa: E501

        :param created_at: The created_at of this ArduinoProperty.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ArduinoProperty.  # noqa: E501

        Delete date of the property  # noqa: E501

        :return: The deleted_at of this ArduinoProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ArduinoProperty.

        Delete date of the property  # noqa: E501

        :param deleted_at: The deleted_at of this ArduinoProperty.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def href(self):
        """Gets the href of this ArduinoProperty.  # noqa: E501

        The api reference of this property  # noqa: E501

        :return: The href of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ArduinoProperty.

        The api reference of this property  # noqa: E501

        :param href: The href of this ArduinoProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and href is None:  # noqa: E501
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def id(self):
        """Gets the id of this ArduinoProperty.  # noqa: E501

        The id of the property  # noqa: E501

        :return: The id of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArduinoProperty.

        The id of the property  # noqa: E501

        :param id: The id of this ArduinoProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_value(self):
        """Gets the last_value of this ArduinoProperty.  # noqa: E501

        Last value of this property  # noqa: E501

        :return: The last_value of this ArduinoProperty.  # noqa: E501
        :rtype: object
        """
        return self._last_value

    @last_value.setter
    def last_value(self, last_value):
        """Sets the last_value of this ArduinoProperty.

        Last value of this property  # noqa: E501

        :param last_value: The last_value of this ArduinoProperty.  # noqa: E501
        :type: object
        """

        self._last_value = last_value

    @property
    def max_value(self):
        """Gets the max_value of this ArduinoProperty.  # noqa: E501

        Maximum value of this property  # noqa: E501

        :return: The max_value of this ArduinoProperty.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this ArduinoProperty.

        Maximum value of this property  # noqa: E501

        :param max_value: The max_value of this ArduinoProperty.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def min_value(self):
        """Gets the min_value of this ArduinoProperty.  # noqa: E501

        Minimum value of this property  # noqa: E501

        :return: The min_value of this ArduinoProperty.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this ArduinoProperty.

        Minimum value of this property  # noqa: E501

        :param min_value: The min_value of this ArduinoProperty.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def name(self):
        """Gets the name of this ArduinoProperty.  # noqa: E501

        The friendly name of the property  # noqa: E501

        :return: The name of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArduinoProperty.

        The friendly name of the property  # noqa: E501

        :param name: The name of this ArduinoProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def permission(self):
        """Gets the permission of this ArduinoProperty.  # noqa: E501

        The permission of the property  # noqa: E501

        :return: The permission of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ArduinoProperty.

        The permission of the property  # noqa: E501

        :param permission: The permission of this ArduinoProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and permission is None:  # noqa: E501
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

    @property
    def persist(self):
        """Gets the persist of this ArduinoProperty.  # noqa: E501

        If true, data will persist into a timeseries database  # noqa: E501

        :return: The persist of this ArduinoProperty.  # noqa: E501
        :rtype: bool
        """
        return self._persist

    @persist.setter
    def persist(self, persist):
        """Sets the persist of this ArduinoProperty.

        If true, data will persist into a timeseries database  # noqa: E501

        :param persist: The persist of this ArduinoProperty.  # noqa: E501
        :type: bool
        """

        self._persist = persist

    @property
    def sync_id(self):
        """Gets the sync_id of this ArduinoProperty.  # noqa: E501

        The id of the sync pool  # noqa: E501

        :return: The sync_id of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._sync_id

    @sync_id.setter
    def sync_id(self, sync_id):
        """Sets the sync_id of this ArduinoProperty.

        The id of the sync pool  # noqa: E501

        :param sync_id: The sync_id of this ArduinoProperty.  # noqa: E501
        :type: str
        """

        self._sync_id = sync_id

    @property
    def tag(self):
        """Gets the tag of this ArduinoProperty.  # noqa: E501

        The integer id of the property  # noqa: E501

        :return: The tag of this ArduinoProperty.  # noqa: E501
        :rtype: float
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ArduinoProperty.

        The integer id of the property  # noqa: E501

        :param tag: The tag of this ArduinoProperty.  # noqa: E501
        :type: float
        """

        self._tag = tag

    @property
    def thing_id(self):
        """Gets the thing_id of this ArduinoProperty.  # noqa: E501

        The id of the thing  # noqa: E501

        :return: The thing_id of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._thing_id

    @thing_id.setter
    def thing_id(self, thing_id):
        """Sets the thing_id of this ArduinoProperty.

        The id of the thing  # noqa: E501

        :param thing_id: The thing_id of this ArduinoProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and thing_id is None:  # noqa: E501
            raise ValueError("Invalid value for `thing_id`, must not be `None`")  # noqa: E501

        self._thing_id = thing_id

    @property
    def thing_name(self):
        """Gets the thing_name of this ArduinoProperty.  # noqa: E501

        The name of the associated thing  # noqa: E501

        :return: The thing_name of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._thing_name

    @thing_name.setter
    def thing_name(self, thing_name):
        """Sets the thing_name of this ArduinoProperty.

        The name of the associated thing  # noqa: E501

        :param thing_name: The thing_name of this ArduinoProperty.  # noqa: E501
        :type: str
        """

        self._thing_name = thing_name

    @property
    def type(self):
        """Gets the type of this ArduinoProperty.  # noqa: E501

        The type of the property  # noqa: E501

        :return: The type of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ArduinoProperty.

        The type of the property  # noqa: E501

        :param type: The type of this ArduinoProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def update_parameter(self):
        """Gets the update_parameter of this ArduinoProperty.  # noqa: E501

        The update frequency in seconds, or the amount of the property has to change in order to trigger an update  # noqa: E501

        :return: The update_parameter of this ArduinoProperty.  # noqa: E501
        :rtype: float
        """
        return self._update_parameter

    @update_parameter.setter
    def update_parameter(self, update_parameter):
        """Sets the update_parameter of this ArduinoProperty.

        The update frequency in seconds, or the amount of the property has to change in order to trigger an update  # noqa: E501

        :param update_parameter: The update_parameter of this ArduinoProperty.  # noqa: E501
        :type: float
        """

        self._update_parameter = update_parameter

    @property
    def update_strategy(self):
        """Gets the update_strategy of this ArduinoProperty.  # noqa: E501

        The update strategy for the property value  # noqa: E501

        :return: The update_strategy of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        """Sets the update_strategy of this ArduinoProperty.

        The update strategy for the property value  # noqa: E501

        :param update_strategy: The update_strategy of this ArduinoProperty.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and update_strategy is None:  # noqa: E501
            raise ValueError("Invalid value for `update_strategy`, must not be `None`")  # noqa: E501

        self._update_strategy = update_strategy

    @property
    def updated_at(self):
        """Gets the updated_at of this ArduinoProperty.  # noqa: E501

        Update date of the property  # noqa: E501

        :return: The updated_at of this ArduinoProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ArduinoProperty.

        Update date of the property  # noqa: E501

        :param updated_at: The updated_at of this ArduinoProperty.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def value_updated_at(self):
        """Gets the value_updated_at of this ArduinoProperty.  # noqa: E501

        Last update timestamp of this property  # noqa: E501

        :return: The value_updated_at of this ArduinoProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._value_updated_at

    @value_updated_at.setter
    def value_updated_at(self, value_updated_at):
        """Sets the value_updated_at of this ArduinoProperty.

        Last update timestamp of this property  # noqa: E501

        :param value_updated_at: The value_updated_at of this ArduinoProperty.  # noqa: E501
        :type: datetime
        """

        self._value_updated_at = value_updated_at

    @property
    def variable_name(self):
        """Gets the variable_name of this ArduinoProperty.  # noqa: E501

        The sketch variable name of the property  # noqa: E501

        :return: The variable_name of this ArduinoProperty.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this ArduinoProperty.

        The sketch variable name of the property  # noqa: E501

        :param variable_name: The variable_name of this ArduinoProperty.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, ArduinoProperty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoProperty):
            return True

        return self.to_dict() != other.to_dict()
