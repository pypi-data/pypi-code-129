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


class Conversation(object):
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
        'closed': 'bool',
        'conversation_arn': 'str',
        'conversation_uuid': 'str',
        'merchant_id': 'str',
        'messages': 'list[ConversationMessage]',
        'participants': 'list[ConversationParticipant]'
    }

    attribute_map = {
        'closed': 'closed',
        'conversation_arn': 'conversation_arn',
        'conversation_uuid': 'conversation_uuid',
        'merchant_id': 'merchant_id',
        'messages': 'messages',
        'participants': 'participants'
    }

    def __init__(self, closed=None, conversation_arn=None, conversation_uuid=None, merchant_id=None, messages=None, participants=None):  # noqa: E501
        """Conversation - a model defined in Swagger"""  # noqa: E501

        self._closed = None
        self._conversation_arn = None
        self._conversation_uuid = None
        self._merchant_id = None
        self._messages = None
        self._participants = None
        self.discriminator = None

        if closed is not None:
            self.closed = closed
        if conversation_arn is not None:
            self.conversation_arn = conversation_arn
        if conversation_uuid is not None:
            self.conversation_uuid = conversation_uuid
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if messages is not None:
            self.messages = messages
        if participants is not None:
            self.participants = participants

    @property
    def closed(self):
        """Gets the closed of this Conversation.  # noqa: E501


        :return: The closed of this Conversation.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this Conversation.


        :param closed: The closed of this Conversation.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def conversation_arn(self):
        """Gets the conversation_arn of this Conversation.  # noqa: E501


        :return: The conversation_arn of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._conversation_arn

    @conversation_arn.setter
    def conversation_arn(self, conversation_arn):
        """Sets the conversation_arn of this Conversation.


        :param conversation_arn: The conversation_arn of this Conversation.  # noqa: E501
        :type: str
        """

        self._conversation_arn = conversation_arn

    @property
    def conversation_uuid(self):
        """Gets the conversation_uuid of this Conversation.  # noqa: E501


        :return: The conversation_uuid of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._conversation_uuid

    @conversation_uuid.setter
    def conversation_uuid(self, conversation_uuid):
        """Sets the conversation_uuid of this Conversation.


        :param conversation_uuid: The conversation_uuid of this Conversation.  # noqa: E501
        :type: str
        """

        self._conversation_uuid = conversation_uuid

    @property
    def merchant_id(self):
        """Gets the merchant_id of this Conversation.  # noqa: E501


        :return: The merchant_id of this Conversation.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this Conversation.


        :param merchant_id: The merchant_id of this Conversation.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def messages(self):
        """Gets the messages of this Conversation.  # noqa: E501


        :return: The messages of this Conversation.  # noqa: E501
        :rtype: list[ConversationMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Conversation.


        :param messages: The messages of this Conversation.  # noqa: E501
        :type: list[ConversationMessage]
        """

        self._messages = messages

    @property
    def participants(self):
        """Gets the participants of this Conversation.  # noqa: E501


        :return: The participants of this Conversation.  # noqa: E501
        :rtype: list[ConversationParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this Conversation.


        :param participants: The participants of this Conversation.  # noqa: E501
        :type: list[ConversationParticipant]
        """

        self._participants = participants

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
        if issubclass(Conversation, dict):
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
        if not isinstance(other, Conversation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
