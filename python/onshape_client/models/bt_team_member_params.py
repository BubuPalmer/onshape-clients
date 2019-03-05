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


class BTTeamMemberParams(object):
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
        'email': 'str',
        'admin': 'bool',
        'team_id': 'str'
    }

    attribute_map = {
        'email': 'email',
        'admin': 'admin',
        'team_id': 'teamId'
    }

    def __init__(self, email=None, admin=None, team_id=None):  # noqa: E501
        """BTTeamMemberParams - a model defined in OpenAPI"""  # noqa: E501

        self._email = None
        self._admin = None
        self._team_id = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if admin is not None:
            self.admin = admin
        if team_id is not None:
            self.team_id = team_id

    @property
    def email(self):
        """Gets the email of this BTTeamMemberParams.  # noqa: E501


        :return: The email of this BTTeamMemberParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTTeamMemberParams.


        :param email: The email of this BTTeamMemberParams.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def admin(self):
        """Gets the admin of this BTTeamMemberParams.  # noqa: E501


        :return: The admin of this BTTeamMemberParams.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this BTTeamMemberParams.


        :param admin: The admin of this BTTeamMemberParams.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def team_id(self):
        """Gets the team_id of this BTTeamMemberParams.  # noqa: E501


        :return: The team_id of this BTTeamMemberParams.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this BTTeamMemberParams.


        :param team_id: The team_id of this BTTeamMemberParams.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

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
        if not isinstance(other, BTTeamMemberParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
