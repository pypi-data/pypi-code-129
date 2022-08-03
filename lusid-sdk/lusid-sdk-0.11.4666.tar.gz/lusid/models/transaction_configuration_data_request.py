# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4666
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class TransactionConfigurationDataRequest(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'aliases': 'list[TransactionConfigurationTypeAlias]',
        'movements': 'list[TransactionConfigurationMovementDataRequest]',
        'properties': 'dict(str, PerpetualProperty)'
    }

    attribute_map = {
        'aliases': 'aliases',
        'movements': 'movements',
        'properties': 'properties'
    }

    required_map = {
        'aliases': 'required',
        'movements': 'required',
        'properties': 'optional'
    }

    def __init__(self, aliases=None, movements=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """TransactionConfigurationDataRequest - a model defined in OpenAPI"
        
        :param aliases:  List of transaction codes that map to this specific transaction model (required)
        :type aliases: list[lusid.TransactionConfigurationTypeAlias]
        :param movements:  Movement data for the transaction code (required)
        :type movements: list[lusid.TransactionConfigurationMovementDataRequest]
        :param properties:  Properties attached to the underlying holding.
        :type properties: dict[str, lusid.PerpetualProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._aliases = None
        self._movements = None
        self._properties = None
        self.discriminator = None

        self.aliases = aliases
        self.movements = movements
        self.properties = properties

    @property
    def aliases(self):
        """Gets the aliases of this TransactionConfigurationDataRequest.  # noqa: E501

        List of transaction codes that map to this specific transaction model  # noqa: E501

        :return: The aliases of this TransactionConfigurationDataRequest.  # noqa: E501
        :rtype: list[lusid.TransactionConfigurationTypeAlias]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this TransactionConfigurationDataRequest.

        List of transaction codes that map to this specific transaction model  # noqa: E501

        :param aliases: The aliases of this TransactionConfigurationDataRequest.  # noqa: E501
        :type aliases: list[lusid.TransactionConfigurationTypeAlias]
        """
        if self.local_vars_configuration.client_side_validation and aliases is None:  # noqa: E501
            raise ValueError("Invalid value for `aliases`, must not be `None`")  # noqa: E501

        self._aliases = aliases

    @property
    def movements(self):
        """Gets the movements of this TransactionConfigurationDataRequest.  # noqa: E501

        Movement data for the transaction code  # noqa: E501

        :return: The movements of this TransactionConfigurationDataRequest.  # noqa: E501
        :rtype: list[lusid.TransactionConfigurationMovementDataRequest]
        """
        return self._movements

    @movements.setter
    def movements(self, movements):
        """Sets the movements of this TransactionConfigurationDataRequest.

        Movement data for the transaction code  # noqa: E501

        :param movements: The movements of this TransactionConfigurationDataRequest.  # noqa: E501
        :type movements: list[lusid.TransactionConfigurationMovementDataRequest]
        """
        if self.local_vars_configuration.client_side_validation and movements is None:  # noqa: E501
            raise ValueError("Invalid value for `movements`, must not be `None`")  # noqa: E501

        self._movements = movements

    @property
    def properties(self):
        """Gets the properties of this TransactionConfigurationDataRequest.  # noqa: E501

        Properties attached to the underlying holding.  # noqa: E501

        :return: The properties of this TransactionConfigurationDataRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TransactionConfigurationDataRequest.

        Properties attached to the underlying holding.  # noqa: E501

        :param properties: The properties of this TransactionConfigurationDataRequest.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionConfigurationDataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionConfigurationDataRequest):
            return True

        return self.to_dict() != other.to_dict()
