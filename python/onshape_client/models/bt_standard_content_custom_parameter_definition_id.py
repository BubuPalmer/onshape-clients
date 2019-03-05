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


class BTStandardContentCustomParameterDefinitionId(object):
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
        'property_id': 'str',
        'owner_id': 'str',
        'owner_type': 'int',
        'parameter_name': 'str',
        'standard': 'str',
        'category': 'str',
        'types': 'str',
        'type': 'str'
    }

    attribute_map = {
        'property_id': 'propertyId',
        'owner_id': 'ownerId',
        'owner_type': 'ownerType',
        'parameter_name': 'parameterName',
        'standard': 'standard',
        'category': 'category',
        'types': 'types',
        'type': 'type'
    }

    def __init__(self, property_id=None, owner_id=None, owner_type=None, parameter_name=None, standard=None, category=None, types=None, type=None):  # noqa: E501
        """BTStandardContentCustomParameterDefinitionId - a model defined in OpenAPI"""  # noqa: E501

        self._property_id = None
        self._owner_id = None
        self._owner_type = None
        self._parameter_name = None
        self._standard = None
        self._category = None
        self._types = None
        self._type = None
        self.discriminator = None

        if property_id is not None:
            self.property_id = property_id
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_type is not None:
            self.owner_type = owner_type
        if parameter_name is not None:
            self.parameter_name = parameter_name
        if standard is not None:
            self.standard = standard
        if category is not None:
            self.category = category
        if types is not None:
            self.types = types
        if type is not None:
            self.type = type

    @property
    def property_id(self):
        """Gets the property_id of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501


        :return: The property_id of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this BTStandardContentCustomParameterDefinitionId.


        :param property_id: The property_id of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :type: str
        """

        self._property_id = property_id

    @property
    def owner_id(self):
        """Gets the owner_id of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501


        :return: The owner_id of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BTStandardContentCustomParameterDefinitionId.


        :param owner_id: The owner_id of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def owner_type(self):
        """Gets the owner_type of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501


        :return: The owner_type of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :rtype: int
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this BTStandardContentCustomParameterDefinitionId.


        :param owner_type: The owner_type of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :type: int
        """

        self._owner_type = owner_type

    @property
    def parameter_name(self):
        """Gets the parameter_name of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501


        :return: The parameter_name of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this BTStandardContentCustomParameterDefinitionId.


        :param parameter_name: The parameter_name of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :type: str
        """

        self._parameter_name = parameter_name

    @property
    def standard(self):
        """Gets the standard of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501


        :return: The standard of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this BTStandardContentCustomParameterDefinitionId.


        :param standard: The standard of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :type: str
        """

        self._standard = standard

    @property
    def category(self):
        """Gets the category of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501


        :return: The category of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this BTStandardContentCustomParameterDefinitionId.


        :param category: The category of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def types(self):
        """Gets the types of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501


        :return: The types of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :rtype: str
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this BTStandardContentCustomParameterDefinitionId.


        :param types: The types of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :type: str
        """

        self._types = types

    @property
    def type(self):
        """Gets the type of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501


        :return: The type of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTStandardContentCustomParameterDefinitionId.


        :param type: The type of this BTStandardContentCustomParameterDefinitionId.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, BTStandardContentCustomParameterDefinitionId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
