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


class BTWorkflowStateInfo(object):
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
        'value': 'int',
        'notifier_source_property': 'str',
        'approver_source_property': 'str',
        'editable_properties': 'list[str]',
        'required_properties': 'list[str]',
        'display_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'notifier_source_property': 'notifierSourceProperty',
        'approver_source_property': 'approverSourceProperty',
        'editable_properties': 'editableProperties',
        'required_properties': 'requiredProperties',
        'display_name': 'displayName'
    }

    def __init__(self, name=None, value=None, notifier_source_property=None, approver_source_property=None, editable_properties=None, required_properties=None, display_name=None):  # noqa: E501
        """BTWorkflowStateInfo - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._value = None
        self._notifier_source_property = None
        self._approver_source_property = None
        self._editable_properties = None
        self._required_properties = None
        self._display_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if notifier_source_property is not None:
            self.notifier_source_property = notifier_source_property
        if approver_source_property is not None:
            self.approver_source_property = approver_source_property
        if editable_properties is not None:
            self.editable_properties = editable_properties
        if required_properties is not None:
            self.required_properties = required_properties
        if display_name is not None:
            self.display_name = display_name

    @property
    def name(self):
        """Gets the name of this BTWorkflowStateInfo.  # noqa: E501


        :return: The name of this BTWorkflowStateInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTWorkflowStateInfo.


        :param name: The name of this BTWorkflowStateInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this BTWorkflowStateInfo.  # noqa: E501


        :return: The value of this BTWorkflowStateInfo.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BTWorkflowStateInfo.


        :param value: The value of this BTWorkflowStateInfo.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def notifier_source_property(self):
        """Gets the notifier_source_property of this BTWorkflowStateInfo.  # noqa: E501


        :return: The notifier_source_property of this BTWorkflowStateInfo.  # noqa: E501
        :rtype: str
        """
        return self._notifier_source_property

    @notifier_source_property.setter
    def notifier_source_property(self, notifier_source_property):
        """Sets the notifier_source_property of this BTWorkflowStateInfo.


        :param notifier_source_property: The notifier_source_property of this BTWorkflowStateInfo.  # noqa: E501
        :type: str
        """

        self._notifier_source_property = notifier_source_property

    @property
    def approver_source_property(self):
        """Gets the approver_source_property of this BTWorkflowStateInfo.  # noqa: E501


        :return: The approver_source_property of this BTWorkflowStateInfo.  # noqa: E501
        :rtype: str
        """
        return self._approver_source_property

    @approver_source_property.setter
    def approver_source_property(self, approver_source_property):
        """Sets the approver_source_property of this BTWorkflowStateInfo.


        :param approver_source_property: The approver_source_property of this BTWorkflowStateInfo.  # noqa: E501
        :type: str
        """

        self._approver_source_property = approver_source_property

    @property
    def editable_properties(self):
        """Gets the editable_properties of this BTWorkflowStateInfo.  # noqa: E501


        :return: The editable_properties of this BTWorkflowStateInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._editable_properties

    @editable_properties.setter
    def editable_properties(self, editable_properties):
        """Sets the editable_properties of this BTWorkflowStateInfo.


        :param editable_properties: The editable_properties of this BTWorkflowStateInfo.  # noqa: E501
        :type: list[str]
        """

        self._editable_properties = editable_properties

    @property
    def required_properties(self):
        """Gets the required_properties of this BTWorkflowStateInfo.  # noqa: E501


        :return: The required_properties of this BTWorkflowStateInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_properties

    @required_properties.setter
    def required_properties(self, required_properties):
        """Sets the required_properties of this BTWorkflowStateInfo.


        :param required_properties: The required_properties of this BTWorkflowStateInfo.  # noqa: E501
        :type: list[str]
        """

        self._required_properties = required_properties

    @property
    def display_name(self):
        """Gets the display_name of this BTWorkflowStateInfo.  # noqa: E501


        :return: The display_name of this BTWorkflowStateInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BTWorkflowStateInfo.


        :param display_name: The display_name of this BTWorkflowStateInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if not isinstance(other, BTWorkflowStateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
