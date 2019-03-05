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


class BTMatchingStandardContentHierarchyInfo(object):
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
        'type': 'list[str]',
        'standard_default': 'str',
        'category_default': 'str',
        'types_default': 'str',
        'type_default': 'str',
        'category': 'list[str]',
        'types': 'list[str]',
        'component_document_id': 'str',
        'standard': 'list[str]',
        'name': 'str',
        'id': 'str',
        'view_ref': 'str',
        'href': 'str'
    }

    attribute_map = {
        'type': 'type',
        'standard_default': 'standardDefault',
        'category_default': 'categoryDefault',
        'types_default': 'typesDefault',
        'type_default': 'typeDefault',
        'category': 'category',
        'types': 'types',
        'component_document_id': 'componentDocumentId',
        'standard': 'standard',
        'name': 'name',
        'id': 'id',
        'view_ref': 'viewRef',
        'href': 'href'
    }

    def __init__(self, type=None, standard_default=None, category_default=None, types_default=None, type_default=None, category=None, types=None, component_document_id=None, standard=None, name=None, id=None, view_ref=None, href=None):  # noqa: E501
        """BTMatchingStandardContentHierarchyInfo - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._standard_default = None
        self._category_default = None
        self._types_default = None
        self._type_default = None
        self._category = None
        self._types = None
        self._component_document_id = None
        self._standard = None
        self._name = None
        self._id = None
        self._view_ref = None
        self._href = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if standard_default is not None:
            self.standard_default = standard_default
        if category_default is not None:
            self.category_default = category_default
        if types_default is not None:
            self.types_default = types_default
        if type_default is not None:
            self.type_default = type_default
        if category is not None:
            self.category = category
        if types is not None:
            self.types = types
        if component_document_id is not None:
            self.component_document_id = component_document_id
        if standard is not None:
            self.standard = standard
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if view_ref is not None:
            self.view_ref = view_ref
        if href is not None:
            self.href = href

    @property
    def type(self):
        """Gets the type of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The type of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTMatchingStandardContentHierarchyInfo.


        :param type: The type of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def standard_default(self):
        """Gets the standard_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The standard_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._standard_default

    @standard_default.setter
    def standard_default(self, standard_default):
        """Sets the standard_default of this BTMatchingStandardContentHierarchyInfo.


        :param standard_default: The standard_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._standard_default = standard_default

    @property
    def category_default(self):
        """Gets the category_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The category_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._category_default

    @category_default.setter
    def category_default(self, category_default):
        """Sets the category_default of this BTMatchingStandardContentHierarchyInfo.


        :param category_default: The category_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._category_default = category_default

    @property
    def types_default(self):
        """Gets the types_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The types_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._types_default

    @types_default.setter
    def types_default(self, types_default):
        """Sets the types_default of this BTMatchingStandardContentHierarchyInfo.


        :param types_default: The types_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._types_default = types_default

    @property
    def type_default(self):
        """Gets the type_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The type_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._type_default

    @type_default.setter
    def type_default(self, type_default):
        """Sets the type_default of this BTMatchingStandardContentHierarchyInfo.


        :param type_default: The type_default of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._type_default = type_default

    @property
    def category(self):
        """Gets the category of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The category of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this BTMatchingStandardContentHierarchyInfo.


        :param category: The category of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: list[str]
        """

        self._category = category

    @property
    def types(self):
        """Gets the types of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The types of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this BTMatchingStandardContentHierarchyInfo.


        :param types: The types of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: list[str]
        """

        self._types = types

    @property
    def component_document_id(self):
        """Gets the component_document_id of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The component_document_id of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._component_document_id

    @component_document_id.setter
    def component_document_id(self, component_document_id):
        """Sets the component_document_id of this BTMatchingStandardContentHierarchyInfo.


        :param component_document_id: The component_document_id of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._component_document_id = component_document_id

    @property
    def standard(self):
        """Gets the standard of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The standard of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this BTMatchingStandardContentHierarchyInfo.


        :param standard: The standard of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: list[str]
        """

        self._standard = standard

    @property
    def name(self):
        """Gets the name of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The name of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTMatchingStandardContentHierarchyInfo.


        :param name: The name of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The id of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTMatchingStandardContentHierarchyInfo.


        :param id: The id of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def view_ref(self):
        """Gets the view_ref of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The view_ref of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTMatchingStandardContentHierarchyInfo.


        :param view_ref: The view_ref of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def href(self):
        """Gets the href of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501


        :return: The href of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTMatchingStandardContentHierarchyInfo.


        :param href: The href of this BTMatchingStandardContentHierarchyInfo.  # noqa: E501
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
        if not isinstance(other, BTMatchingStandardContentHierarchyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
