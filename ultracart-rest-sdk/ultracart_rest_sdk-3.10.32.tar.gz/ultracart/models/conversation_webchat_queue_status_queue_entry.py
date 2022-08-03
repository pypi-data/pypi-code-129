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


class ConversationWebchatQueueStatusQueueEntry(object):
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
        'conversation_participant_arn': 'str',
        'conversation_participant_name': 'str',
        'conversation_webchat_queue_uuid': 'str',
        'email': 'str',
        'join_dts': 'str',
        'question': 'str'
    }

    attribute_map = {
        'conversation_participant_arn': 'conversation_participant_arn',
        'conversation_participant_name': 'conversation_participant_name',
        'conversation_webchat_queue_uuid': 'conversation_webchat_queue_uuid',
        'email': 'email',
        'join_dts': 'join_dts',
        'question': 'question'
    }

    def __init__(self, conversation_participant_arn=None, conversation_participant_name=None, conversation_webchat_queue_uuid=None, email=None, join_dts=None, question=None):  # noqa: E501
        """ConversationWebchatQueueStatusQueueEntry - a model defined in Swagger"""  # noqa: E501

        self._conversation_participant_arn = None
        self._conversation_participant_name = None
        self._conversation_webchat_queue_uuid = None
        self._email = None
        self._join_dts = None
        self._question = None
        self.discriminator = None

        if conversation_participant_arn is not None:
            self.conversation_participant_arn = conversation_participant_arn
        if conversation_participant_name is not None:
            self.conversation_participant_name = conversation_participant_name
        if conversation_webchat_queue_uuid is not None:
            self.conversation_webchat_queue_uuid = conversation_webchat_queue_uuid
        if email is not None:
            self.email = email
        if join_dts is not None:
            self.join_dts = join_dts
        if question is not None:
            self.question = question

    @property
    def conversation_participant_arn(self):
        """Gets the conversation_participant_arn of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501


        :return: The conversation_participant_arn of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :rtype: str
        """
        return self._conversation_participant_arn

    @conversation_participant_arn.setter
    def conversation_participant_arn(self, conversation_participant_arn):
        """Sets the conversation_participant_arn of this ConversationWebchatQueueStatusQueueEntry.


        :param conversation_participant_arn: The conversation_participant_arn of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :type: str
        """

        self._conversation_participant_arn = conversation_participant_arn

    @property
    def conversation_participant_name(self):
        """Gets the conversation_participant_name of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501


        :return: The conversation_participant_name of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :rtype: str
        """
        return self._conversation_participant_name

    @conversation_participant_name.setter
    def conversation_participant_name(self, conversation_participant_name):
        """Sets the conversation_participant_name of this ConversationWebchatQueueStatusQueueEntry.


        :param conversation_participant_name: The conversation_participant_name of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :type: str
        """

        self._conversation_participant_name = conversation_participant_name

    @property
    def conversation_webchat_queue_uuid(self):
        """Gets the conversation_webchat_queue_uuid of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501


        :return: The conversation_webchat_queue_uuid of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :rtype: str
        """
        return self._conversation_webchat_queue_uuid

    @conversation_webchat_queue_uuid.setter
    def conversation_webchat_queue_uuid(self, conversation_webchat_queue_uuid):
        """Sets the conversation_webchat_queue_uuid of this ConversationWebchatQueueStatusQueueEntry.


        :param conversation_webchat_queue_uuid: The conversation_webchat_queue_uuid of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :type: str
        """

        self._conversation_webchat_queue_uuid = conversation_webchat_queue_uuid

    @property
    def email(self):
        """Gets the email of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501


        :return: The email of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ConversationWebchatQueueStatusQueueEntry.


        :param email: The email of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def join_dts(self):
        """Gets the join_dts of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501

        Date/time the customer joined the queue  # noqa: E501

        :return: The join_dts of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :rtype: str
        """
        return self._join_dts

    @join_dts.setter
    def join_dts(self, join_dts):
        """Sets the join_dts of this ConversationWebchatQueueStatusQueueEntry.

        Date/time the customer joined the queue  # noqa: E501

        :param join_dts: The join_dts of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :type: str
        """

        self._join_dts = join_dts

    @property
    def question(self):
        """Gets the question of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501


        :return: The question of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this ConversationWebchatQueueStatusQueueEntry.


        :param question: The question of this ConversationWebchatQueueStatusQueueEntry.  # noqa: E501
        :type: str
        """

        self._question = question

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
        if issubclass(ConversationWebchatQueueStatusQueueEntry, dict):
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
        if not isinstance(other, ConversationWebchatQueueStatusQueueEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
