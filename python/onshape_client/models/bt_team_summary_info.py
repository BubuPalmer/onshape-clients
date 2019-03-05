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


class BTTeamSummaryInfo(object):
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
        'predefined_team': 'int',
        'owner': 'BTOwnerInfo',
        'has_pending_owner': 'bool',
        'tree_href': 'str',
        'resource_type': 'str',
        'is_mutable': 'bool',
        'is_container': 'bool',
        'can_move': 'bool',
        'description': 'str',
        'project_id': 'str',
        'created_at': 'datetime',
        'created_by': 'BTUserBasicSummaryInfo',
        'modified_by': 'BTUserBasicSummaryInfo',
        'modified_at': 'datetime',
        'is_enterprise_owned': 'bool',
        'name': 'str',
        'id': 'str',
        'view_ref': 'str',
        'href': 'str'
    }

    attribute_map = {
        'active': 'active',
        'predefined_team': 'predefinedTeam',
        'owner': 'owner',
        'has_pending_owner': 'hasPendingOwner',
        'tree_href': 'treeHref',
        'resource_type': 'resourceType',
        'is_mutable': 'isMutable',
        'is_container': 'isContainer',
        'can_move': 'canMove',
        'description': 'description',
        'project_id': 'projectId',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'modified_at': 'modifiedAt',
        'is_enterprise_owned': 'isEnterpriseOwned',
        'name': 'name',
        'id': 'id',
        'view_ref': 'viewRef',
        'href': 'href'
    }

    def __init__(self, active=None, predefined_team=None, owner=None, has_pending_owner=None, tree_href=None, resource_type=None, is_mutable=None, is_container=None, can_move=None, description=None, project_id=None, created_at=None, created_by=None, modified_by=None, modified_at=None, is_enterprise_owned=None, name=None, id=None, view_ref=None, href=None):  # noqa: E501
        """BTTeamSummaryInfo - a model defined in OpenAPI"""  # noqa: E501

        self._active = None
        self._predefined_team = None
        self._owner = None
        self._has_pending_owner = None
        self._tree_href = None
        self._resource_type = None
        self._is_mutable = None
        self._is_container = None
        self._can_move = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._created_by = None
        self._modified_by = None
        self._modified_at = None
        self._is_enterprise_owned = None
        self._name = None
        self._id = None
        self._view_ref = None
        self._href = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if predefined_team is not None:
            self.predefined_team = predefined_team
        if owner is not None:
            self.owner = owner
        if has_pending_owner is not None:
            self.has_pending_owner = has_pending_owner
        if tree_href is not None:
            self.tree_href = tree_href
        if resource_type is not None:
            self.resource_type = resource_type
        if is_mutable is not None:
            self.is_mutable = is_mutable
        if is_container is not None:
            self.is_container = is_container
        if can_move is not None:
            self.can_move = can_move
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_at is not None:
            self.modified_at = modified_at
        if is_enterprise_owned is not None:
            self.is_enterprise_owned = is_enterprise_owned
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
        """Gets the active of this BTTeamSummaryInfo.  # noqa: E501


        :return: The active of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BTTeamSummaryInfo.


        :param active: The active of this BTTeamSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def predefined_team(self):
        """Gets the predefined_team of this BTTeamSummaryInfo.  # noqa: E501


        :return: The predefined_team of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._predefined_team

    @predefined_team.setter
    def predefined_team(self, predefined_team):
        """Sets the predefined_team of this BTTeamSummaryInfo.


        :param predefined_team: The predefined_team of this BTTeamSummaryInfo.  # noqa: E501
        :type: int
        """

        self._predefined_team = predefined_team

    @property
    def owner(self):
        """Gets the owner of this BTTeamSummaryInfo.  # noqa: E501


        :return: The owner of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: BTOwnerInfo
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BTTeamSummaryInfo.


        :param owner: The owner of this BTTeamSummaryInfo.  # noqa: E501
        :type: BTOwnerInfo
        """

        self._owner = owner

    @property
    def has_pending_owner(self):
        """Gets the has_pending_owner of this BTTeamSummaryInfo.  # noqa: E501


        :return: The has_pending_owner of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_pending_owner

    @has_pending_owner.setter
    def has_pending_owner(self, has_pending_owner):
        """Sets the has_pending_owner of this BTTeamSummaryInfo.


        :param has_pending_owner: The has_pending_owner of this BTTeamSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._has_pending_owner = has_pending_owner

    @property
    def tree_href(self):
        """Gets the tree_href of this BTTeamSummaryInfo.  # noqa: E501


        :return: The tree_href of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._tree_href

    @tree_href.setter
    def tree_href(self, tree_href):
        """Sets the tree_href of this BTTeamSummaryInfo.


        :param tree_href: The tree_href of this BTTeamSummaryInfo.  # noqa: E501
        :type: str
        """

        self._tree_href = tree_href

    @property
    def resource_type(self):
        """Gets the resource_type of this BTTeamSummaryInfo.  # noqa: E501


        :return: The resource_type of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BTTeamSummaryInfo.


        :param resource_type: The resource_type of this BTTeamSummaryInfo.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def is_mutable(self):
        """Gets the is_mutable of this BTTeamSummaryInfo.  # noqa: E501


        :return: The is_mutable of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_mutable

    @is_mutable.setter
    def is_mutable(self, is_mutable):
        """Sets the is_mutable of this BTTeamSummaryInfo.


        :param is_mutable: The is_mutable of this BTTeamSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._is_mutable = is_mutable

    @property
    def is_container(self):
        """Gets the is_container of this BTTeamSummaryInfo.  # noqa: E501


        :return: The is_container of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_container

    @is_container.setter
    def is_container(self, is_container):
        """Sets the is_container of this BTTeamSummaryInfo.


        :param is_container: The is_container of this BTTeamSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._is_container = is_container

    @property
    def can_move(self):
        """Gets the can_move of this BTTeamSummaryInfo.  # noqa: E501


        :return: The can_move of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._can_move

    @can_move.setter
    def can_move(self, can_move):
        """Sets the can_move of this BTTeamSummaryInfo.


        :param can_move: The can_move of this BTTeamSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._can_move = can_move

    @property
    def description(self):
        """Gets the description of this BTTeamSummaryInfo.  # noqa: E501


        :return: The description of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTTeamSummaryInfo.


        :param description: The description of this BTTeamSummaryInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this BTTeamSummaryInfo.  # noqa: E501


        :return: The project_id of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTTeamSummaryInfo.


        :param project_id: The project_id of this BTTeamSummaryInfo.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this BTTeamSummaryInfo.  # noqa: E501


        :return: The created_at of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BTTeamSummaryInfo.


        :param created_at: The created_at of this BTTeamSummaryInfo.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this BTTeamSummaryInfo.  # noqa: E501


        :return: The created_by of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: BTUserBasicSummaryInfo
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BTTeamSummaryInfo.


        :param created_by: The created_by of this BTTeamSummaryInfo.  # noqa: E501
        :type: BTUserBasicSummaryInfo
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this BTTeamSummaryInfo.  # noqa: E501


        :return: The modified_by of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: BTUserBasicSummaryInfo
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this BTTeamSummaryInfo.


        :param modified_by: The modified_by of this BTTeamSummaryInfo.  # noqa: E501
        :type: BTUserBasicSummaryInfo
        """

        self._modified_by = modified_by

    @property
    def modified_at(self):
        """Gets the modified_at of this BTTeamSummaryInfo.  # noqa: E501


        :return: The modified_at of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this BTTeamSummaryInfo.


        :param modified_at: The modified_at of this BTTeamSummaryInfo.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def is_enterprise_owned(self):
        """Gets the is_enterprise_owned of this BTTeamSummaryInfo.  # noqa: E501


        :return: The is_enterprise_owned of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_enterprise_owned

    @is_enterprise_owned.setter
    def is_enterprise_owned(self, is_enterprise_owned):
        """Sets the is_enterprise_owned of this BTTeamSummaryInfo.


        :param is_enterprise_owned: The is_enterprise_owned of this BTTeamSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._is_enterprise_owned = is_enterprise_owned

    @property
    def name(self):
        """Gets the name of this BTTeamSummaryInfo.  # noqa: E501


        :return: The name of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTTeamSummaryInfo.


        :param name: The name of this BTTeamSummaryInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTTeamSummaryInfo.  # noqa: E501


        :return: The id of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTTeamSummaryInfo.


        :param id: The id of this BTTeamSummaryInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def view_ref(self):
        """Gets the view_ref of this BTTeamSummaryInfo.  # noqa: E501


        :return: The view_ref of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTTeamSummaryInfo.


        :param view_ref: The view_ref of this BTTeamSummaryInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def href(self):
        """Gets the href of this BTTeamSummaryInfo.  # noqa: E501


        :return: The href of this BTTeamSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTTeamSummaryInfo.


        :param href: The href of this BTTeamSummaryInfo.  # noqa: E501
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
        if not isinstance(other, BTTeamSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
