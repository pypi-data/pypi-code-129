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


class OrderCheckout(object):
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
        'browser': 'Browser',
        'comments': 'str',
        'custom_field1': 'str',
        'custom_field2': 'str',
        'custom_field3': 'str',
        'custom_field4': 'str',
        'custom_field5': 'str',
        'custom_field6': 'str',
        'custom_field7': 'str',
        'customer_ip_address': 'str',
        'screen_branding_theme_code': 'str',
        'screen_size': 'str',
        'storefront_host_name': 'str',
        'upsell_path_code': 'str'
    }

    attribute_map = {
        'browser': 'browser',
        'comments': 'comments',
        'custom_field1': 'custom_field1',
        'custom_field2': 'custom_field2',
        'custom_field3': 'custom_field3',
        'custom_field4': 'custom_field4',
        'custom_field5': 'custom_field5',
        'custom_field6': 'custom_field6',
        'custom_field7': 'custom_field7',
        'customer_ip_address': 'customer_ip_address',
        'screen_branding_theme_code': 'screen_branding_theme_code',
        'screen_size': 'screen_size',
        'storefront_host_name': 'storefront_host_name',
        'upsell_path_code': 'upsell_path_code'
    }

    def __init__(self, browser=None, comments=None, custom_field1=None, custom_field2=None, custom_field3=None, custom_field4=None, custom_field5=None, custom_field6=None, custom_field7=None, customer_ip_address=None, screen_branding_theme_code=None, screen_size=None, storefront_host_name=None, upsell_path_code=None):  # noqa: E501
        """OrderCheckout - a model defined in Swagger"""  # noqa: E501

        self._browser = None
        self._comments = None
        self._custom_field1 = None
        self._custom_field2 = None
        self._custom_field3 = None
        self._custom_field4 = None
        self._custom_field5 = None
        self._custom_field6 = None
        self._custom_field7 = None
        self._customer_ip_address = None
        self._screen_branding_theme_code = None
        self._screen_size = None
        self._storefront_host_name = None
        self._upsell_path_code = None
        self.discriminator = None

        if browser is not None:
            self.browser = browser
        if comments is not None:
            self.comments = comments
        if custom_field1 is not None:
            self.custom_field1 = custom_field1
        if custom_field2 is not None:
            self.custom_field2 = custom_field2
        if custom_field3 is not None:
            self.custom_field3 = custom_field3
        if custom_field4 is not None:
            self.custom_field4 = custom_field4
        if custom_field5 is not None:
            self.custom_field5 = custom_field5
        if custom_field6 is not None:
            self.custom_field6 = custom_field6
        if custom_field7 is not None:
            self.custom_field7 = custom_field7
        if customer_ip_address is not None:
            self.customer_ip_address = customer_ip_address
        if screen_branding_theme_code is not None:
            self.screen_branding_theme_code = screen_branding_theme_code
        if screen_size is not None:
            self.screen_size = screen_size
        if storefront_host_name is not None:
            self.storefront_host_name = storefront_host_name
        if upsell_path_code is not None:
            self.upsell_path_code = upsell_path_code

    @property
    def browser(self):
        """Gets the browser of this OrderCheckout.  # noqa: E501


        :return: The browser of this OrderCheckout.  # noqa: E501
        :rtype: Browser
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this OrderCheckout.


        :param browser: The browser of this OrderCheckout.  # noqa: E501
        :type: Browser
        """

        self._browser = browser

    @property
    def comments(self):
        """Gets the comments of this OrderCheckout.  # noqa: E501

        Comments from the customer.  Rarely used on the single page checkout.  # noqa: E501

        :return: The comments of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this OrderCheckout.

        Comments from the customer.  Rarely used on the single page checkout.  # noqa: E501

        :param comments: The comments of this OrderCheckout.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def custom_field1(self):
        """Gets the custom_field1 of this OrderCheckout.  # noqa: E501

        Custom field 1  # noqa: E501

        :return: The custom_field1 of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._custom_field1

    @custom_field1.setter
    def custom_field1(self, custom_field1):
        """Sets the custom_field1 of this OrderCheckout.

        Custom field 1  # noqa: E501

        :param custom_field1: The custom_field1 of this OrderCheckout.  # noqa: E501
        :type: str
        """
        if custom_field1 is not None and len(custom_field1) > 50:
            raise ValueError("Invalid value for `custom_field1`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_field1 = custom_field1

    @property
    def custom_field2(self):
        """Gets the custom_field2 of this OrderCheckout.  # noqa: E501

        Custom field 2  # noqa: E501

        :return: The custom_field2 of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._custom_field2

    @custom_field2.setter
    def custom_field2(self, custom_field2):
        """Sets the custom_field2 of this OrderCheckout.

        Custom field 2  # noqa: E501

        :param custom_field2: The custom_field2 of this OrderCheckout.  # noqa: E501
        :type: str
        """
        if custom_field2 is not None and len(custom_field2) > 50:
            raise ValueError("Invalid value for `custom_field2`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_field2 = custom_field2

    @property
    def custom_field3(self):
        """Gets the custom_field3 of this OrderCheckout.  # noqa: E501

        Custom field 3  # noqa: E501

        :return: The custom_field3 of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._custom_field3

    @custom_field3.setter
    def custom_field3(self, custom_field3):
        """Sets the custom_field3 of this OrderCheckout.

        Custom field 3  # noqa: E501

        :param custom_field3: The custom_field3 of this OrderCheckout.  # noqa: E501
        :type: str
        """
        if custom_field3 is not None and len(custom_field3) > 50:
            raise ValueError("Invalid value for `custom_field3`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_field3 = custom_field3

    @property
    def custom_field4(self):
        """Gets the custom_field4 of this OrderCheckout.  # noqa: E501

        Custom field 4  # noqa: E501

        :return: The custom_field4 of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._custom_field4

    @custom_field4.setter
    def custom_field4(self, custom_field4):
        """Sets the custom_field4 of this OrderCheckout.

        Custom field 4  # noqa: E501

        :param custom_field4: The custom_field4 of this OrderCheckout.  # noqa: E501
        :type: str
        """
        if custom_field4 is not None and len(custom_field4) > 50:
            raise ValueError("Invalid value for `custom_field4`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_field4 = custom_field4

    @property
    def custom_field5(self):
        """Gets the custom_field5 of this OrderCheckout.  # noqa: E501

        Custom field 5  # noqa: E501

        :return: The custom_field5 of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._custom_field5

    @custom_field5.setter
    def custom_field5(self, custom_field5):
        """Sets the custom_field5 of this OrderCheckout.

        Custom field 5  # noqa: E501

        :param custom_field5: The custom_field5 of this OrderCheckout.  # noqa: E501
        :type: str
        """
        if custom_field5 is not None and len(custom_field5) > 75:
            raise ValueError("Invalid value for `custom_field5`, length must be less than or equal to `75`")  # noqa: E501

        self._custom_field5 = custom_field5

    @property
    def custom_field6(self):
        """Gets the custom_field6 of this OrderCheckout.  # noqa: E501

        Custom field 6  # noqa: E501

        :return: The custom_field6 of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._custom_field6

    @custom_field6.setter
    def custom_field6(self, custom_field6):
        """Sets the custom_field6 of this OrderCheckout.

        Custom field 6  # noqa: E501

        :param custom_field6: The custom_field6 of this OrderCheckout.  # noqa: E501
        :type: str
        """
        if custom_field6 is not None and len(custom_field6) > 50:
            raise ValueError("Invalid value for `custom_field6`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_field6 = custom_field6

    @property
    def custom_field7(self):
        """Gets the custom_field7 of this OrderCheckout.  # noqa: E501

        Custom field 7  # noqa: E501

        :return: The custom_field7 of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._custom_field7

    @custom_field7.setter
    def custom_field7(self, custom_field7):
        """Sets the custom_field7 of this OrderCheckout.

        Custom field 7  # noqa: E501

        :param custom_field7: The custom_field7 of this OrderCheckout.  # noqa: E501
        :type: str
        """
        if custom_field7 is not None and len(custom_field7) > 50:
            raise ValueError("Invalid value for `custom_field7`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_field7 = custom_field7

    @property
    def customer_ip_address(self):
        """Gets the customer_ip_address of this OrderCheckout.  # noqa: E501

        IP address of the customer when placing the order  # noqa: E501

        :return: The customer_ip_address of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._customer_ip_address

    @customer_ip_address.setter
    def customer_ip_address(self, customer_ip_address):
        """Sets the customer_ip_address of this OrderCheckout.

        IP address of the customer when placing the order  # noqa: E501

        :param customer_ip_address: The customer_ip_address of this OrderCheckout.  # noqa: E501
        :type: str
        """

        self._customer_ip_address = customer_ip_address

    @property
    def screen_branding_theme_code(self):
        """Gets the screen_branding_theme_code of this OrderCheckout.  # noqa: E501

        Screen branding theme code associated with the order (legacy checkout)  # noqa: E501

        :return: The screen_branding_theme_code of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._screen_branding_theme_code

    @screen_branding_theme_code.setter
    def screen_branding_theme_code(self, screen_branding_theme_code):
        """Sets the screen_branding_theme_code of this OrderCheckout.

        Screen branding theme code associated with the order (legacy checkout)  # noqa: E501

        :param screen_branding_theme_code: The screen_branding_theme_code of this OrderCheckout.  # noqa: E501
        :type: str
        """
        if screen_branding_theme_code is not None and len(screen_branding_theme_code) > 10:
            raise ValueError("Invalid value for `screen_branding_theme_code`, length must be less than or equal to `10`")  # noqa: E501

        self._screen_branding_theme_code = screen_branding_theme_code

    @property
    def screen_size(self):
        """Gets the screen_size of this OrderCheckout.  # noqa: E501

        Screen size small, medium or large  # noqa: E501

        :return: The screen_size of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._screen_size

    @screen_size.setter
    def screen_size(self, screen_size):
        """Sets the screen_size of this OrderCheckout.

        Screen size small, medium or large  # noqa: E501

        :param screen_size: The screen_size of this OrderCheckout.  # noqa: E501
        :type: str
        """

        self._screen_size = screen_size

    @property
    def storefront_host_name(self):
        """Gets the storefront_host_name of this OrderCheckout.  # noqa: E501

        StoreFront host name associated with the order  # noqa: E501

        :return: The storefront_host_name of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._storefront_host_name

    @storefront_host_name.setter
    def storefront_host_name(self, storefront_host_name):
        """Sets the storefront_host_name of this OrderCheckout.

        StoreFront host name associated with the order  # noqa: E501

        :param storefront_host_name: The storefront_host_name of this OrderCheckout.  # noqa: E501
        :type: str
        """

        self._storefront_host_name = storefront_host_name

    @property
    def upsell_path_code(self):
        """Gets the upsell_path_code of this OrderCheckout.  # noqa: E501

        Upsell path code assigned during the checkout that the customer went through  # noqa: E501

        :return: The upsell_path_code of this OrderCheckout.  # noqa: E501
        :rtype: str
        """
        return self._upsell_path_code

    @upsell_path_code.setter
    def upsell_path_code(self, upsell_path_code):
        """Sets the upsell_path_code of this OrderCheckout.

        Upsell path code assigned during the checkout that the customer went through  # noqa: E501

        :param upsell_path_code: The upsell_path_code of this OrderCheckout.  # noqa: E501
        :type: str
        """

        self._upsell_path_code = upsell_path_code

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
        if issubclass(OrderCheckout, dict):
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
        if not isinstance(other, OrderCheckout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
