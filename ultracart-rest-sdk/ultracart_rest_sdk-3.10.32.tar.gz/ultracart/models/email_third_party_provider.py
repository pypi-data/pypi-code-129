# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EmailThirdPartyProvider(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'connect_url': 'str',
        'list_count': 'int',
        'lists': 'list[EmailThirdPartyList]',
        'logo_url': 'str',
        'name': 'str',
        'supports_add_tags': 'bool',
        'supports_list_subscribe': 'bool',
        'supports_list_unsubscribe': 'bool',
        'supports_remove_tags': 'bool',
        'tag_count': 'int',
        'tags': 'list[EmailThirdPartyTag]'
    }

    attribute_map = {
        'connect_url': 'connect_url',
        'list_count': 'list_count',
        'lists': 'lists',
        'logo_url': 'logo_url',
        'name': 'name',
        'supports_add_tags': 'supports_add_tags',
        'supports_list_subscribe': 'supports_list_subscribe',
        'supports_list_unsubscribe': 'supports_list_unsubscribe',
        'supports_remove_tags': 'supports_remove_tags',
        'tag_count': 'tag_count',
        'tags': 'tags'
    }

    def __init__(self, connect_url=None, list_count=None, lists=None, logo_url=None, name=None, supports_add_tags=None, supports_list_subscribe=None, supports_list_unsubscribe=None, supports_remove_tags=None, tag_count=None, tags=None):  # noqa: E501
        """EmailThirdPartyProvider - a model defined in Swagger"""  # noqa: E501

        self._connect_url = None
        self._list_count = None
        self._lists = None
        self._logo_url = None
        self._name = None
        self._supports_add_tags = None
        self._supports_list_subscribe = None
        self._supports_list_unsubscribe = None
        self._supports_remove_tags = None
        self._tag_count = None
        self._tags = None
        self.discriminator = None

        if connect_url is not None:
            self.connect_url = connect_url
        if list_count is not None:
            self.list_count = list_count
        if lists is not None:
            self.lists = lists
        if logo_url is not None:
            self.logo_url = logo_url
        if name is not None:
            self.name = name
        if supports_add_tags is not None:
            self.supports_add_tags = supports_add_tags
        if supports_list_subscribe is not None:
            self.supports_list_subscribe = supports_list_subscribe
        if supports_list_unsubscribe is not None:
            self.supports_list_unsubscribe = supports_list_unsubscribe
        if supports_remove_tags is not None:
            self.supports_remove_tags = supports_remove_tags
        if tag_count is not None:
            self.tag_count = tag_count
        if tags is not None:
            self.tags = tags

    @property
    def connect_url(self):
        """Gets the connect_url of this EmailThirdPartyProvider.  # noqa: E501

        URL to the settings screen to connect.  Null if the provider is already connected.  # noqa: E501

        :return: The connect_url of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: str
        """
        return self._connect_url

    @connect_url.setter
    def connect_url(self, connect_url):
        """Sets the connect_url of this EmailThirdPartyProvider.

        URL to the settings screen to connect.  Null if the provider is already connected.  # noqa: E501

        :param connect_url: The connect_url of this EmailThirdPartyProvider.  # noqa: E501
        :type: str
        """

        self._connect_url = connect_url

    @property
    def list_count(self):
        """Gets the list_count of this EmailThirdPartyProvider.  # noqa: E501

        list_count  # noqa: E501

        :return: The list_count of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: int
        """
        return self._list_count

    @list_count.setter
    def list_count(self, list_count):
        """Sets the list_count of this EmailThirdPartyProvider.

        list_count  # noqa: E501

        :param list_count: The list_count of this EmailThirdPartyProvider.  # noqa: E501
        :type: int
        """

        self._list_count = list_count

    @property
    def lists(self):
        """Gets the lists of this EmailThirdPartyProvider.  # noqa: E501

        lists  # noqa: E501

        :return: The lists of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: list[EmailThirdPartyList]
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """Sets the lists of this EmailThirdPartyProvider.

        lists  # noqa: E501

        :param lists: The lists of this EmailThirdPartyProvider.  # noqa: E501
        :type: list[EmailThirdPartyList]
        """

        self._lists = lists

    @property
    def logo_url(self):
        """Gets the logo_url of this EmailThirdPartyProvider.  # noqa: E501

        logo_url  # noqa: E501

        :return: The logo_url of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this EmailThirdPartyProvider.

        logo_url  # noqa: E501

        :param logo_url: The logo_url of this EmailThirdPartyProvider.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def name(self):
        """Gets the name of this EmailThirdPartyProvider.  # noqa: E501

        name  # noqa: E501

        :return: The name of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailThirdPartyProvider.

        name  # noqa: E501

        :param name: The name of this EmailThirdPartyProvider.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def supports_add_tags(self):
        """Gets the supports_add_tags of this EmailThirdPartyProvider.  # noqa: E501

        True if this provider can support adding tags  # noqa: E501

        :return: The supports_add_tags of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_add_tags

    @supports_add_tags.setter
    def supports_add_tags(self, supports_add_tags):
        """Sets the supports_add_tags of this EmailThirdPartyProvider.

        True if this provider can support adding tags  # noqa: E501

        :param supports_add_tags: The supports_add_tags of this EmailThirdPartyProvider.  # noqa: E501
        :type: bool
        """

        self._supports_add_tags = supports_add_tags

    @property
    def supports_list_subscribe(self):
        """Gets the supports_list_subscribe of this EmailThirdPartyProvider.  # noqa: E501

        True if this provider can support list subscribe  # noqa: E501

        :return: The supports_list_subscribe of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_list_subscribe

    @supports_list_subscribe.setter
    def supports_list_subscribe(self, supports_list_subscribe):
        """Sets the supports_list_subscribe of this EmailThirdPartyProvider.

        True if this provider can support list subscribe  # noqa: E501

        :param supports_list_subscribe: The supports_list_subscribe of this EmailThirdPartyProvider.  # noqa: E501
        :type: bool
        """

        self._supports_list_subscribe = supports_list_subscribe

    @property
    def supports_list_unsubscribe(self):
        """Gets the supports_list_unsubscribe of this EmailThirdPartyProvider.  # noqa: E501

        True if this provider can support list unsubscribe  # noqa: E501

        :return: The supports_list_unsubscribe of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_list_unsubscribe

    @supports_list_unsubscribe.setter
    def supports_list_unsubscribe(self, supports_list_unsubscribe):
        """Sets the supports_list_unsubscribe of this EmailThirdPartyProvider.

        True if this provider can support list unsubscribe  # noqa: E501

        :param supports_list_unsubscribe: The supports_list_unsubscribe of this EmailThirdPartyProvider.  # noqa: E501
        :type: bool
        """

        self._supports_list_unsubscribe = supports_list_unsubscribe

    @property
    def supports_remove_tags(self):
        """Gets the supports_remove_tags of this EmailThirdPartyProvider.  # noqa: E501

        True if this provider can support remove tags  # noqa: E501

        :return: The supports_remove_tags of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: bool
        """
        return self._supports_remove_tags

    @supports_remove_tags.setter
    def supports_remove_tags(self, supports_remove_tags):
        """Sets the supports_remove_tags of this EmailThirdPartyProvider.

        True if this provider can support remove tags  # noqa: E501

        :param supports_remove_tags: The supports_remove_tags of this EmailThirdPartyProvider.  # noqa: E501
        :type: bool
        """

        self._supports_remove_tags = supports_remove_tags

    @property
    def tag_count(self):
        """Gets the tag_count of this EmailThirdPartyProvider.  # noqa: E501

        tag_count  # noqa: E501

        :return: The tag_count of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: int
        """
        return self._tag_count

    @tag_count.setter
    def tag_count(self, tag_count):
        """Sets the tag_count of this EmailThirdPartyProvider.

        tag_count  # noqa: E501

        :param tag_count: The tag_count of this EmailThirdPartyProvider.  # noqa: E501
        :type: int
        """

        self._tag_count = tag_count

    @property
    def tags(self):
        """Gets the tags of this EmailThirdPartyProvider.  # noqa: E501

        tags  # noqa: E501

        :return: The tags of this EmailThirdPartyProvider.  # noqa: E501
        :rtype: list[EmailThirdPartyTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EmailThirdPartyProvider.

        tags  # noqa: E501

        :param tags: The tags of this EmailThirdPartyProvider.  # noqa: E501
        :type: list[EmailThirdPartyTag]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EmailThirdPartyProvider, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmailThirdPartyProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
