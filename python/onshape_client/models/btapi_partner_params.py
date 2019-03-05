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


class BTAPIPartnerParams(object):
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
        'website': 'str',
        'description': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'website': 'website',
        'description': 'description',
        'user_id': 'userId'
    }

    def __init__(self, name=None, website=None, description=None, user_id=None):  # noqa: E501
        """BTAPIPartnerParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._website = None
        self._description = None
        self._user_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if website is not None:
            self.website = website
        if description is not None:
            self.description = description
        if user_id is not None:
            self.user_id = user_id

    @property
    def name(self):
        """Gets the name of this BTAPIPartnerParams.  # noqa: E501


        :return: The name of this BTAPIPartnerParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTAPIPartnerParams.


        :param name: The name of this BTAPIPartnerParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def website(self):
        """Gets the website of this BTAPIPartnerParams.  # noqa: E501


        :return: The website of this BTAPIPartnerParams.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this BTAPIPartnerParams.


        :param website: The website of this BTAPIPartnerParams.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def description(self):
        """Gets the description of this BTAPIPartnerParams.  # noqa: E501


        :return: The description of this BTAPIPartnerParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTAPIPartnerParams.


        :param description: The description of this BTAPIPartnerParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def user_id(self):
        """Gets the user_id of this BTAPIPartnerParams.  # noqa: E501


        :return: The user_id of this BTAPIPartnerParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BTAPIPartnerParams.


        :param user_id: The user_id of this BTAPIPartnerParams.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if not isinstance(other, BTAPIPartnerParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
