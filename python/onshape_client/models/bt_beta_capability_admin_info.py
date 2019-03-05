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


class BTBetaCapabilityAdminInfo(object):
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
        'capability_name': 'str',
        'approvals_per_hour': 'float',
        'auto_approve': 'bool',
        'auto_approve_paid': 'bool',
        'auto_approve_onshape': 'bool',
        'self_service_disabled': 'bool',
        'user_count': 'int',
        'user_limit': 'int',
        'eula': 'str',
        'welcome_html': 'str',
        'upgradable': 'bool',
        'user_state': 'int',
        'description': 'str',
        'user_based': 'bool',
        'name': 'str',
        'id': 'str',
        'view_ref': 'str',
        'href': 'str'
    }

    attribute_map = {
        'capability_name': 'capabilityName',
        'approvals_per_hour': 'approvalsPerHour',
        'auto_approve': 'autoApprove',
        'auto_approve_paid': 'autoApprovePaid',
        'auto_approve_onshape': 'autoApproveOnshape',
        'self_service_disabled': 'selfServiceDisabled',
        'user_count': 'userCount',
        'user_limit': 'userLimit',
        'eula': 'eula',
        'welcome_html': 'welcomeHTML',
        'upgradable': 'upgradable',
        'user_state': 'userState',
        'description': 'description',
        'user_based': 'userBased',
        'name': 'name',
        'id': 'id',
        'view_ref': 'viewRef',
        'href': 'href'
    }

    def __init__(self, capability_name=None, approvals_per_hour=None, auto_approve=None, auto_approve_paid=None, auto_approve_onshape=None, self_service_disabled=None, user_count=None, user_limit=None, eula=None, welcome_html=None, upgradable=None, user_state=None, description=None, user_based=None, name=None, id=None, view_ref=None, href=None):  # noqa: E501
        """BTBetaCapabilityAdminInfo - a model defined in OpenAPI"""  # noqa: E501

        self._capability_name = None
        self._approvals_per_hour = None
        self._auto_approve = None
        self._auto_approve_paid = None
        self._auto_approve_onshape = None
        self._self_service_disabled = None
        self._user_count = None
        self._user_limit = None
        self._eula = None
        self._welcome_html = None
        self._upgradable = None
        self._user_state = None
        self._description = None
        self._user_based = None
        self._name = None
        self._id = None
        self._view_ref = None
        self._href = None
        self.discriminator = None

        if capability_name is not None:
            self.capability_name = capability_name
        if approvals_per_hour is not None:
            self.approvals_per_hour = approvals_per_hour
        if auto_approve is not None:
            self.auto_approve = auto_approve
        if auto_approve_paid is not None:
            self.auto_approve_paid = auto_approve_paid
        if auto_approve_onshape is not None:
            self.auto_approve_onshape = auto_approve_onshape
        if self_service_disabled is not None:
            self.self_service_disabled = self_service_disabled
        if user_count is not None:
            self.user_count = user_count
        if user_limit is not None:
            self.user_limit = user_limit
        if eula is not None:
            self.eula = eula
        if welcome_html is not None:
            self.welcome_html = welcome_html
        if upgradable is not None:
            self.upgradable = upgradable
        if user_state is not None:
            self.user_state = user_state
        if description is not None:
            self.description = description
        if user_based is not None:
            self.user_based = user_based
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if view_ref is not None:
            self.view_ref = view_ref
        if href is not None:
            self.href = href

    @property
    def capability_name(self):
        """Gets the capability_name of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The capability_name of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: str
        """
        return self._capability_name

    @capability_name.setter
    def capability_name(self, capability_name):
        """Sets the capability_name of this BTBetaCapabilityAdminInfo.


        :param capability_name: The capability_name of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: str
        """

        self._capability_name = capability_name

    @property
    def approvals_per_hour(self):
        """Gets the approvals_per_hour of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The approvals_per_hour of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: float
        """
        return self._approvals_per_hour

    @approvals_per_hour.setter
    def approvals_per_hour(self, approvals_per_hour):
        """Sets the approvals_per_hour of this BTBetaCapabilityAdminInfo.


        :param approvals_per_hour: The approvals_per_hour of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: float
        """

        self._approvals_per_hour = approvals_per_hour

    @property
    def auto_approve(self):
        """Gets the auto_approve of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The auto_approve of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approve

    @auto_approve.setter
    def auto_approve(self, auto_approve):
        """Sets the auto_approve of this BTBetaCapabilityAdminInfo.


        :param auto_approve: The auto_approve of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: bool
        """

        self._auto_approve = auto_approve

    @property
    def auto_approve_paid(self):
        """Gets the auto_approve_paid of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The auto_approve_paid of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approve_paid

    @auto_approve_paid.setter
    def auto_approve_paid(self, auto_approve_paid):
        """Sets the auto_approve_paid of this BTBetaCapabilityAdminInfo.


        :param auto_approve_paid: The auto_approve_paid of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: bool
        """

        self._auto_approve_paid = auto_approve_paid

    @property
    def auto_approve_onshape(self):
        """Gets the auto_approve_onshape of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The auto_approve_onshape of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approve_onshape

    @auto_approve_onshape.setter
    def auto_approve_onshape(self, auto_approve_onshape):
        """Sets the auto_approve_onshape of this BTBetaCapabilityAdminInfo.


        :param auto_approve_onshape: The auto_approve_onshape of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: bool
        """

        self._auto_approve_onshape = auto_approve_onshape

    @property
    def self_service_disabled(self):
        """Gets the self_service_disabled of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The self_service_disabled of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: bool
        """
        return self._self_service_disabled

    @self_service_disabled.setter
    def self_service_disabled(self, self_service_disabled):
        """Sets the self_service_disabled of this BTBetaCapabilityAdminInfo.


        :param self_service_disabled: The self_service_disabled of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: bool
        """

        self._self_service_disabled = self_service_disabled

    @property
    def user_count(self):
        """Gets the user_count of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The user_count of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this BTBetaCapabilityAdminInfo.


        :param user_count: The user_count of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def user_limit(self):
        """Gets the user_limit of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The user_limit of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_limit

    @user_limit.setter
    def user_limit(self, user_limit):
        """Sets the user_limit of this BTBetaCapabilityAdminInfo.


        :param user_limit: The user_limit of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: int
        """

        self._user_limit = user_limit

    @property
    def eula(self):
        """Gets the eula of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The eula of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: str
        """
        return self._eula

    @eula.setter
    def eula(self, eula):
        """Sets the eula of this BTBetaCapabilityAdminInfo.


        :param eula: The eula of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: str
        """

        self._eula = eula

    @property
    def welcome_html(self):
        """Gets the welcome_html of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The welcome_html of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: str
        """
        return self._welcome_html

    @welcome_html.setter
    def welcome_html(self, welcome_html):
        """Sets the welcome_html of this BTBetaCapabilityAdminInfo.


        :param welcome_html: The welcome_html of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: str
        """

        self._welcome_html = welcome_html

    @property
    def upgradable(self):
        """Gets the upgradable of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The upgradable of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: bool
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        """Sets the upgradable of this BTBetaCapabilityAdminInfo.


        :param upgradable: The upgradable of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: bool
        """

        self._upgradable = upgradable

    @property
    def user_state(self):
        """Gets the user_state of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The user_state of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_state

    @user_state.setter
    def user_state(self, user_state):
        """Sets the user_state of this BTBetaCapabilityAdminInfo.


        :param user_state: The user_state of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: int
        """

        self._user_state = user_state

    @property
    def description(self):
        """Gets the description of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The description of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTBetaCapabilityAdminInfo.


        :param description: The description of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def user_based(self):
        """Gets the user_based of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The user_based of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: bool
        """
        return self._user_based

    @user_based.setter
    def user_based(self, user_based):
        """Sets the user_based of this BTBetaCapabilityAdminInfo.


        :param user_based: The user_based of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: bool
        """

        self._user_based = user_based

    @property
    def name(self):
        """Gets the name of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The name of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTBetaCapabilityAdminInfo.


        :param name: The name of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The id of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTBetaCapabilityAdminInfo.


        :param id: The id of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def view_ref(self):
        """Gets the view_ref of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The view_ref of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTBetaCapabilityAdminInfo.


        :param view_ref: The view_ref of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def href(self):
        """Gets the href of this BTBetaCapabilityAdminInfo.  # noqa: E501


        :return: The href of this BTBetaCapabilityAdminInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTBetaCapabilityAdminInfo.


        :param href: The href of this BTBetaCapabilityAdminInfo.  # noqa: E501
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
        if not isinstance(other, BTBetaCapabilityAdminInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
