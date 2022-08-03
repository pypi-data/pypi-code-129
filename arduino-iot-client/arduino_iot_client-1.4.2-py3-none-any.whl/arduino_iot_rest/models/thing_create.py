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


class ThingCreate(object):
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
        'device_id': 'str',
        'id': 'str',
        'name': 'str',
        'properties': 'list[ModelProperty]',
        'timezone': 'str',
        'webhook_active': 'bool',
        'webhook_uri': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'id': 'id',
        'name': 'name',
        'properties': 'properties',
        'timezone': 'timezone',
        'webhook_active': 'webhook_active',
        'webhook_uri': 'webhook_uri'
    }

    def __init__(self, device_id=None, id=None, name=None, properties=None, timezone='America/New_York', webhook_active=None, webhook_uri=None, local_vars_configuration=None):  # noqa: E501
        """ThingCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._id = None
        self._name = None
        self._properties = None
        self._timezone = None
        self._webhook_active = None
        self._webhook_uri = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if timezone is not None:
            self.timezone = timezone
        if webhook_active is not None:
            self.webhook_active = webhook_active
        if webhook_uri is not None:
            self.webhook_uri = webhook_uri

    @property
    def device_id(self):
        """Gets the device_id of this ThingCreate.  # noqa: E501

        The arn of the associated device  # noqa: E501

        :return: The device_id of this ThingCreate.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ThingCreate.

        The arn of the associated device  # noqa: E501

        :param device_id: The device_id of this ThingCreate.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def id(self):
        """Gets the id of this ThingCreate.  # noqa: E501

        The id of the thing  # noqa: E501

        :return: The id of this ThingCreate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThingCreate.

        The id of the thing  # noqa: E501

        :param id: The id of this ThingCreate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ThingCreate.  # noqa: E501

        The friendly name of the thing  # noqa: E501

        :return: The name of this ThingCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThingCreate.

        The friendly name of the thing  # noqa: E501

        :param name: The name of this ThingCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9_.@ -]+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9_.@ -]+$/`")  # noqa: E501

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this ThingCreate.  # noqa: E501

        The properties of the thing  # noqa: E501

        :return: The properties of this ThingCreate.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ThingCreate.

        The properties of the thing  # noqa: E501

        :param properties: The properties of this ThingCreate.  # noqa: E501
        :type: list[ModelProperty]
        """

        self._properties = properties

    @property
    def timezone(self):
        """Gets the timezone of this ThingCreate.  # noqa: E501

        A time zone name Check /v2/timezones for a list of valid names.  # noqa: E501

        :return: The timezone of this ThingCreate.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ThingCreate.

        A time zone name Check /v2/timezones for a list of valid names.  # noqa: E501

        :param timezone: The timezone of this ThingCreate.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def webhook_active(self):
        """Gets the webhook_active of this ThingCreate.  # noqa: E501

        Webhook uri  # noqa: E501

        :return: The webhook_active of this ThingCreate.  # noqa: E501
        :rtype: bool
        """
        return self._webhook_active

    @webhook_active.setter
    def webhook_active(self, webhook_active):
        """Sets the webhook_active of this ThingCreate.

        Webhook uri  # noqa: E501

        :param webhook_active: The webhook_active of this ThingCreate.  # noqa: E501
        :type: bool
        """

        self._webhook_active = webhook_active

    @property
    def webhook_uri(self):
        """Gets the webhook_uri of this ThingCreate.  # noqa: E501

        Webhook uri  # noqa: E501

        :return: The webhook_uri of this ThingCreate.  # noqa: E501
        :rtype: str
        """
        return self._webhook_uri

    @webhook_uri.setter
    def webhook_uri(self, webhook_uri):
        """Sets the webhook_uri of this ThingCreate.

        Webhook uri  # noqa: E501

        :param webhook_uri: The webhook_uri of this ThingCreate.  # noqa: E501
        :type: str
        """

        self._webhook_uri = webhook_uri

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
        if not isinstance(other, ThingCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThingCreate):
            return True

        return self.to_dict() != other.to_dict()
