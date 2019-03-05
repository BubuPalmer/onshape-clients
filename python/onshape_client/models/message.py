# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.94
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Message(object):
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
        'default_title': 'str',
        'default_template': 'str',
        'message_level': 'str'
    }

    attribute_map = {
        'id': 'id',
        'default_title': 'defaultTitle',
        'default_template': 'defaultTemplate',
        'message_level': 'messageLevel'
    }

    def __init__(self, id=None, default_title=None, default_template=None, message_level=None):  # noqa: E501
        """Message - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._default_title = None
        self._default_template = None
        self._message_level = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if default_title is not None:
            self.default_title = default_title
        if default_template is not None:
            self.default_template = default_template
        if message_level is not None:
            self.message_level = message_level

    @property
    def id(self):
        """Gets the id of this Message.  # noqa: E501


        :return: The id of this Message.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Message.


        :param id: The id of this Message.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def default_title(self):
        """Gets the default_title of this Message.  # noqa: E501


        :return: The default_title of this Message.  # noqa: E501
        :rtype: str
        """
        return self._default_title

    @default_title.setter
    def default_title(self, default_title):
        """Sets the default_title of this Message.


        :param default_title: The default_title of this Message.  # noqa: E501
        :type: str
        """

        self._default_title = default_title

    @property
    def default_template(self):
        """Gets the default_template of this Message.  # noqa: E501


        :return: The default_template of this Message.  # noqa: E501
        :rtype: str
        """
        return self._default_template

    @default_template.setter
    def default_template(self, default_template):
        """Sets the default_template of this Message.


        :param default_template: The default_template of this Message.  # noqa: E501
        :type: str
        """

        self._default_template = default_template

    @property
    def message_level(self):
        """Gets the message_level of this Message.  # noqa: E501


        :return: The message_level of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message_level

    @message_level.setter
    def message_level(self, message_level):
        """Sets the message_level of this Message.


        :param message_level: The message_level of this Message.  # noqa: E501
        :type: str
        """
        allowed_values = ["INFO", "WARNING", "ERROR", "MARKETING", "PRODUCT", "IMPORTANT", "ACTION"]  # noqa: E501
        if message_level not in allowed_values:
            raise ValueError(
                "Invalid value for `message_level` ({0}), must be one of {1}"  # noqa: E501
                .format(message_level, allowed_values)
            )

        self._message_level = message_level

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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
