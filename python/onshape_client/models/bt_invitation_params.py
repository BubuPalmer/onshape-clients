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


class BTInvitationParams(object):
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
        'message': 'str',
        'id': 'str',
        'state': 'int',
        'source': 'int',
        'description': 'str',
        'password': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'default_company_name': 'str',
        'plan_id': 'str',
        'seats': 'int',
        'role': 'int',
        'company_user_emails': 'list[str]',
        'approve_user': 'bool',
        'privacy_consent_accepted': 'bool',
        'cad_system_at_signup': 'str',
        'company_plan': 'bool',
        'eula_accepted': 'bool',
        'country_code': 'str',
        'phone_number': 'str',
        'recaptcha': 'str',
        'invite_friend_request': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'message': 'message',
        'id': 'id',
        'state': 'state',
        'source': 'source',
        'description': 'description',
        'password': 'password',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'default_company_name': 'defaultCompanyName',
        'plan_id': 'planId',
        'seats': 'seats',
        'role': 'role',
        'company_user_emails': 'companyUserEmails',
        'approve_user': 'approveUser',
        'privacy_consent_accepted': 'privacyConsentAccepted',
        'cad_system_at_signup': 'cadSystemAtSignup',
        'company_plan': 'companyPlan',
        'eula_accepted': 'eulaAccepted',
        'country_code': 'countryCode',
        'phone_number': 'phoneNumber',
        'recaptcha': 'recaptcha',
        'invite_friend_request': 'inviteFriendRequest'
    }

    def __init__(self, name=None, message=None, id=None, state=None, source=None, description=None, password=None, first_name=None, last_name=None, email=None, default_company_name=None, plan_id=None, seats=None, role=None, company_user_emails=None, approve_user=None, privacy_consent_accepted=None, cad_system_at_signup=None, company_plan=None, eula_accepted=None, country_code=None, phone_number=None, recaptcha=None, invite_friend_request=None):  # noqa: E501
        """BTInvitationParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._message = None
        self._id = None
        self._state = None
        self._source = None
        self._description = None
        self._password = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._default_company_name = None
        self._plan_id = None
        self._seats = None
        self._role = None
        self._company_user_emails = None
        self._approve_user = None
        self._privacy_consent_accepted = None
        self._cad_system_at_signup = None
        self._company_plan = None
        self._eula_accepted = None
        self._country_code = None
        self._phone_number = None
        self._recaptcha = None
        self._invite_friend_request = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if message is not None:
            self.message = message
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if source is not None:
            self.source = source
        if description is not None:
            self.description = description
        if password is not None:
            self.password = password
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if default_company_name is not None:
            self.default_company_name = default_company_name
        if plan_id is not None:
            self.plan_id = plan_id
        if seats is not None:
            self.seats = seats
        if role is not None:
            self.role = role
        if company_user_emails is not None:
            self.company_user_emails = company_user_emails
        if approve_user is not None:
            self.approve_user = approve_user
        if privacy_consent_accepted is not None:
            self.privacy_consent_accepted = privacy_consent_accepted
        if cad_system_at_signup is not None:
            self.cad_system_at_signup = cad_system_at_signup
        if company_plan is not None:
            self.company_plan = company_plan
        if eula_accepted is not None:
            self.eula_accepted = eula_accepted
        if country_code is not None:
            self.country_code = country_code
        if phone_number is not None:
            self.phone_number = phone_number
        if recaptcha is not None:
            self.recaptcha = recaptcha
        if invite_friend_request is not None:
            self.invite_friend_request = invite_friend_request

    @property
    def name(self):
        """Gets the name of this BTInvitationParams.  # noqa: E501


        :return: The name of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTInvitationParams.


        :param name: The name of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def message(self):
        """Gets the message of this BTInvitationParams.  # noqa: E501


        :return: The message of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BTInvitationParams.


        :param message: The message of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def id(self):
        """Gets the id of this BTInvitationParams.  # noqa: E501


        :return: The id of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTInvitationParams.


        :param id: The id of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this BTInvitationParams.  # noqa: E501


        :return: The state of this BTInvitationParams.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTInvitationParams.


        :param state: The state of this BTInvitationParams.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def source(self):
        """Gets the source of this BTInvitationParams.  # noqa: E501


        :return: The source of this BTInvitationParams.  # noqa: E501
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BTInvitationParams.


        :param source: The source of this BTInvitationParams.  # noqa: E501
        :type: int
        """

        self._source = source

    @property
    def description(self):
        """Gets the description of this BTInvitationParams.  # noqa: E501


        :return: The description of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTInvitationParams.


        :param description: The description of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def password(self):
        """Gets the password of this BTInvitationParams.  # noqa: E501


        :return: The password of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this BTInvitationParams.


        :param password: The password of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def first_name(self):
        """Gets the first_name of this BTInvitationParams.  # noqa: E501


        :return: The first_name of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BTInvitationParams.


        :param first_name: The first_name of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BTInvitationParams.  # noqa: E501


        :return: The last_name of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BTInvitationParams.


        :param last_name: The last_name of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this BTInvitationParams.  # noqa: E501


        :return: The email of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTInvitationParams.


        :param email: The email of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def default_company_name(self):
        """Gets the default_company_name of this BTInvitationParams.  # noqa: E501


        :return: The default_company_name of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._default_company_name

    @default_company_name.setter
    def default_company_name(self, default_company_name):
        """Sets the default_company_name of this BTInvitationParams.


        :param default_company_name: The default_company_name of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._default_company_name = default_company_name

    @property
    def plan_id(self):
        """Gets the plan_id of this BTInvitationParams.  # noqa: E501


        :return: The plan_id of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this BTInvitationParams.


        :param plan_id: The plan_id of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def seats(self):
        """Gets the seats of this BTInvitationParams.  # noqa: E501


        :return: The seats of this BTInvitationParams.  # noqa: E501
        :rtype: int
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this BTInvitationParams.


        :param seats: The seats of this BTInvitationParams.  # noqa: E501
        :type: int
        """

        self._seats = seats

    @property
    def role(self):
        """Gets the role of this BTInvitationParams.  # noqa: E501


        :return: The role of this BTInvitationParams.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this BTInvitationParams.


        :param role: The role of this BTInvitationParams.  # noqa: E501
        :type: int
        """

        self._role = role

    @property
    def company_user_emails(self):
        """Gets the company_user_emails of this BTInvitationParams.  # noqa: E501


        :return: The company_user_emails of this BTInvitationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._company_user_emails

    @company_user_emails.setter
    def company_user_emails(self, company_user_emails):
        """Sets the company_user_emails of this BTInvitationParams.


        :param company_user_emails: The company_user_emails of this BTInvitationParams.  # noqa: E501
        :type: list[str]
        """

        self._company_user_emails = company_user_emails

    @property
    def approve_user(self):
        """Gets the approve_user of this BTInvitationParams.  # noqa: E501


        :return: The approve_user of this BTInvitationParams.  # noqa: E501
        :rtype: bool
        """
        return self._approve_user

    @approve_user.setter
    def approve_user(self, approve_user):
        """Sets the approve_user of this BTInvitationParams.


        :param approve_user: The approve_user of this BTInvitationParams.  # noqa: E501
        :type: bool
        """

        self._approve_user = approve_user

    @property
    def privacy_consent_accepted(self):
        """Gets the privacy_consent_accepted of this BTInvitationParams.  # noqa: E501


        :return: The privacy_consent_accepted of this BTInvitationParams.  # noqa: E501
        :rtype: bool
        """
        return self._privacy_consent_accepted

    @privacy_consent_accepted.setter
    def privacy_consent_accepted(self, privacy_consent_accepted):
        """Sets the privacy_consent_accepted of this BTInvitationParams.


        :param privacy_consent_accepted: The privacy_consent_accepted of this BTInvitationParams.  # noqa: E501
        :type: bool
        """

        self._privacy_consent_accepted = privacy_consent_accepted

    @property
    def cad_system_at_signup(self):
        """Gets the cad_system_at_signup of this BTInvitationParams.  # noqa: E501


        :return: The cad_system_at_signup of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._cad_system_at_signup

    @cad_system_at_signup.setter
    def cad_system_at_signup(self, cad_system_at_signup):
        """Sets the cad_system_at_signup of this BTInvitationParams.


        :param cad_system_at_signup: The cad_system_at_signup of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._cad_system_at_signup = cad_system_at_signup

    @property
    def company_plan(self):
        """Gets the company_plan of this BTInvitationParams.  # noqa: E501


        :return: The company_plan of this BTInvitationParams.  # noqa: E501
        :rtype: bool
        """
        return self._company_plan

    @company_plan.setter
    def company_plan(self, company_plan):
        """Sets the company_plan of this BTInvitationParams.


        :param company_plan: The company_plan of this BTInvitationParams.  # noqa: E501
        :type: bool
        """

        self._company_plan = company_plan

    @property
    def eula_accepted(self):
        """Gets the eula_accepted of this BTInvitationParams.  # noqa: E501


        :return: The eula_accepted of this BTInvitationParams.  # noqa: E501
        :rtype: bool
        """
        return self._eula_accepted

    @eula_accepted.setter
    def eula_accepted(self, eula_accepted):
        """Sets the eula_accepted of this BTInvitationParams.


        :param eula_accepted: The eula_accepted of this BTInvitationParams.  # noqa: E501
        :type: bool
        """

        self._eula_accepted = eula_accepted

    @property
    def country_code(self):
        """Gets the country_code of this BTInvitationParams.  # noqa: E501


        :return: The country_code of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this BTInvitationParams.


        :param country_code: The country_code of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def phone_number(self):
        """Gets the phone_number of this BTInvitationParams.  # noqa: E501


        :return: The phone_number of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this BTInvitationParams.


        :param phone_number: The phone_number of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def recaptcha(self):
        """Gets the recaptcha of this BTInvitationParams.  # noqa: E501


        :return: The recaptcha of this BTInvitationParams.  # noqa: E501
        :rtype: str
        """
        return self._recaptcha

    @recaptcha.setter
    def recaptcha(self, recaptcha):
        """Sets the recaptcha of this BTInvitationParams.


        :param recaptcha: The recaptcha of this BTInvitationParams.  # noqa: E501
        :type: str
        """

        self._recaptcha = recaptcha

    @property
    def invite_friend_request(self):
        """Gets the invite_friend_request of this BTInvitationParams.  # noqa: E501


        :return: The invite_friend_request of this BTInvitationParams.  # noqa: E501
        :rtype: bool
        """
        return self._invite_friend_request

    @invite_friend_request.setter
    def invite_friend_request(self, invite_friend_request):
        """Sets the invite_friend_request of this BTInvitationParams.


        :param invite_friend_request: The invite_friend_request of this BTInvitationParams.  # noqa: E501
        :type: bool
        """

        self._invite_friend_request = invite_friend_request

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
        if not isinstance(other, BTInvitationParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
