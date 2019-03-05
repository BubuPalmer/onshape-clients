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


class BTRbacPermissionSchemeParams(object):
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
        'description': 'str',
        'permission_map': 'dict(str, BTPermissionSet)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'permission_map': 'permissionMap'
    }

    def __init__(self, name=None, description=None, permission_map=None):  # noqa: E501
        """BTRbacPermissionSchemeParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._description = None
        self._permission_map = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if permission_map is not None:
            self.permission_map = permission_map

    @property
    def name(self):
        """Gets the name of this BTRbacPermissionSchemeParams.  # noqa: E501


        :return: The name of this BTRbacPermissionSchemeParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTRbacPermissionSchemeParams.


        :param name: The name of this BTRbacPermissionSchemeParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this BTRbacPermissionSchemeParams.  # noqa: E501


        :return: The description of this BTRbacPermissionSchemeParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTRbacPermissionSchemeParams.


        :param description: The description of this BTRbacPermissionSchemeParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def permission_map(self):
        """Gets the permission_map of this BTRbacPermissionSchemeParams.  # noqa: E501


        :return: The permission_map of this BTRbacPermissionSchemeParams.  # noqa: E501
        :rtype: dict(str, BTPermissionSet)
        """
        return self._permission_map

    @permission_map.setter
    def permission_map(self, permission_map):
        """Sets the permission_map of this BTRbacPermissionSchemeParams.


        :param permission_map: The permission_map of this BTRbacPermissionSchemeParams.  # noqa: E501
        :type: dict(str, BTPermissionSet)
        """

        self._permission_map = permission_map

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
        if not isinstance(other, BTRbacPermissionSchemeParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
