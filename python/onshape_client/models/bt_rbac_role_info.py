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


class BTRbacRoleInfo(object):
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
        'active': 'bool',
        'predefined_role': 'int',
        'description': 'str',
        'name': 'str',
        'id': 'str',
        'view_ref': 'str',
        'href': 'str'
    }

    attribute_map = {
        'active': 'active',
        'predefined_role': 'predefinedRole',
        'description': 'description',
        'name': 'name',
        'id': 'id',
        'view_ref': 'viewRef',
        'href': 'href'
    }

    def __init__(self, active=None, predefined_role=None, description=None, name=None, id=None, view_ref=None, href=None):  # noqa: E501
        """BTRbacRoleInfo - a model defined in OpenAPI"""  # noqa: E501

        self._active = None
        self._predefined_role = None
        self._description = None
        self._name = None
        self._id = None
        self._view_ref = None
        self._href = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if predefined_role is not None:
            self.predefined_role = predefined_role
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if view_ref is not None:
            self.view_ref = view_ref
        if href is not None:
            self.href = href

    @property
    def active(self):
        """Gets the active of this BTRbacRoleInfo.  # noqa: E501


        :return: The active of this BTRbacRoleInfo.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BTRbacRoleInfo.


        :param active: The active of this BTRbacRoleInfo.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def predefined_role(self):
        """Gets the predefined_role of this BTRbacRoleInfo.  # noqa: E501


        :return: The predefined_role of this BTRbacRoleInfo.  # noqa: E501
        :rtype: int
        """
        return self._predefined_role

    @predefined_role.setter
    def predefined_role(self, predefined_role):
        """Sets the predefined_role of this BTRbacRoleInfo.


        :param predefined_role: The predefined_role of this BTRbacRoleInfo.  # noqa: E501
        :type: int
        """

        self._predefined_role = predefined_role

    @property
    def description(self):
        """Gets the description of this BTRbacRoleInfo.  # noqa: E501


        :return: The description of this BTRbacRoleInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTRbacRoleInfo.


        :param description: The description of this BTRbacRoleInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this BTRbacRoleInfo.  # noqa: E501


        :return: The name of this BTRbacRoleInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTRbacRoleInfo.


        :param name: The name of this BTRbacRoleInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTRbacRoleInfo.  # noqa: E501


        :return: The id of this BTRbacRoleInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTRbacRoleInfo.


        :param id: The id of this BTRbacRoleInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def view_ref(self):
        """Gets the view_ref of this BTRbacRoleInfo.  # noqa: E501


        :return: The view_ref of this BTRbacRoleInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTRbacRoleInfo.


        :param view_ref: The view_ref of this BTRbacRoleInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def href(self):
        """Gets the href of this BTRbacRoleInfo.  # noqa: E501


        :return: The href of this BTRbacRoleInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTRbacRoleInfo.


        :param href: The href of this BTRbacRoleInfo.  # noqa: E501
        :type: str
        """

        self._href = href

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
        if not isinstance(other, BTRbacRoleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
