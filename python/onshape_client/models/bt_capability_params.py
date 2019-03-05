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


class BTCapabilityParams(object):
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
        'name': 'str',
        'id': 'str',
        'type': 'str',
        'rule_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'rule_id': 'ruleId'
    }

    def __init__(self, name=None, id=None, type=None, rule_id=None):  # noqa: E501
        """BTCapabilityParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._id = None
        self._type = None
        self._rule_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if rule_id is not None:
            self.rule_id = rule_id

    @property
    def name(self):
        """Gets the name of this BTCapabilityParams.  # noqa: E501


        :return: The name of this BTCapabilityParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTCapabilityParams.


        :param name: The name of this BTCapabilityParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTCapabilityParams.  # noqa: E501


        :return: The id of this BTCapabilityParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTCapabilityParams.


        :param id: The id of this BTCapabilityParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this BTCapabilityParams.  # noqa: E501


        :return: The type of this BTCapabilityParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTCapabilityParams.


        :param type: The type of this BTCapabilityParams.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def rule_id(self):
        """Gets the rule_id of this BTCapabilityParams.  # noqa: E501


        :return: The rule_id of this BTCapabilityParams.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this BTCapabilityParams.


        :param rule_id: The rule_id of this BTCapabilityParams.  # noqa: E501
        :type: str
        """

        self._rule_id = rule_id

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
        if not isinstance(other, BTCapabilityParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
