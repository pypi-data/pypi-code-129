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


class PagedResourceListOfBlock(object):
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
        'next_page': 'str',
        'previous_page': 'str',
        'values': 'list[Block]',
        'href': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'next_page': 'nextPage',
        'previous_page': 'previousPage',
        'values': 'values',
        'href': 'href',
        'links': 'links'
    }

    required_map = {
        'next_page': 'optional',
        'previous_page': 'optional',
        'values': 'required',
        'href': 'optional',
        'links': 'optional'
    }

    def __init__(self, next_page=None, previous_page=None, values=None, href=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PagedResourceListOfBlock - a model defined in OpenAPI"
        
        :param next_page:  The next page of results.
        :type next_page: str
        :param previous_page:  The previous page of results.
        :type previous_page: str
        :param values:  The resources to list. (required)
        :type values: list[lusid.Block]
        :param href:  The URI of the resource list.
        :type href: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._next_page = None
        self._previous_page = None
        self._values = None
        self._href = None
        self._links = None
        self.discriminator = None

        self.next_page = next_page
        self.previous_page = previous_page
        self.values = values
        self.href = href
        self.links = links

    @property
    def next_page(self):
        """Gets the next_page of this PagedResourceListOfBlock.  # noqa: E501

        The next page of results.  # noqa: E501

        :return: The next_page of this PagedResourceListOfBlock.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this PagedResourceListOfBlock.

        The next page of results.  # noqa: E501

        :param next_page: The next_page of this PagedResourceListOfBlock.  # noqa: E501
        :type next_page: str
        """

        self._next_page = next_page

    @property
    def previous_page(self):
        """Gets the previous_page of this PagedResourceListOfBlock.  # noqa: E501

        The previous page of results.  # noqa: E501

        :return: The previous_page of this PagedResourceListOfBlock.  # noqa: E501
        :rtype: str
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page):
        """Sets the previous_page of this PagedResourceListOfBlock.

        The previous page of results.  # noqa: E501

        :param previous_page: The previous_page of this PagedResourceListOfBlock.  # noqa: E501
        :type previous_page: str
        """

        self._previous_page = previous_page

    @property
    def values(self):
        """Gets the values of this PagedResourceListOfBlock.  # noqa: E501

        The resources to list.  # noqa: E501

        :return: The values of this PagedResourceListOfBlock.  # noqa: E501
        :rtype: list[lusid.Block]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this PagedResourceListOfBlock.

        The resources to list.  # noqa: E501

        :param values: The values of this PagedResourceListOfBlock.  # noqa: E501
        :type values: list[lusid.Block]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def href(self):
        """Gets the href of this PagedResourceListOfBlock.  # noqa: E501

        The URI of the resource list.  # noqa: E501

        :return: The href of this PagedResourceListOfBlock.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PagedResourceListOfBlock.

        The URI of the resource list.  # noqa: E501

        :param href: The href of this PagedResourceListOfBlock.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def links(self):
        """Gets the links of this PagedResourceListOfBlock.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PagedResourceListOfBlock.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PagedResourceListOfBlock.

        Collection of links.  # noqa: E501

        :param links: The links of this PagedResourceListOfBlock.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, PagedResourceListOfBlock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PagedResourceListOfBlock):
            return True

        return self.to_dict() != other.to_dict()
