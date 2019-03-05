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


class Header(object):
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
        'description': 'str',
        'getref': 'str',
        'required': 'bool',
        'deprecated': 'bool',
        'style': 'str',
        'explode': 'bool',
        'schema': 'Schema',
        'examples': 'dict(str, Example)',
        'example': 'object',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'description': 'description',
        'getref': 'get$ref',
        'required': 'required',
        'deprecated': 'deprecated',
        'style': 'style',
        'explode': 'explode',
        'schema': 'schema',
        'examples': 'examples',
        'example': 'example',
        'extensions': 'extensions'
    }

    def __init__(self, description=None, getref=None, required=None, deprecated=None, style=None, explode=None, schema=None, examples=None, example=None, extensions=None):  # noqa: E501
        """Header - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._getref = None
        self._required = None
        self._deprecated = None
        self._style = None
        self._explode = None
        self._schema = None
        self._examples = None
        self._example = None
        self._extensions = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if getref is not None:
            self.getref = getref
        if required is not None:
            self.required = required
        if deprecated is not None:
            self.deprecated = deprecated
        if style is not None:
            self.style = style
        if explode is not None:
            self.explode = explode
        if schema is not None:
            self.schema = schema
        if examples is not None:
            self.examples = examples
        if example is not None:
            self.example = example
        if extensions is not None:
            self.extensions = extensions

    @property
    def description(self):
        """Gets the description of this Header.  # noqa: E501


        :return: The description of this Header.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Header.


        :param description: The description of this Header.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def getref(self):
        """Gets the getref of this Header.  # noqa: E501


        :return: The getref of this Header.  # noqa: E501
        :rtype: str
        """
        return self._getref

    @getref.setter
    def getref(self, getref):
        """Sets the getref of this Header.


        :param getref: The getref of this Header.  # noqa: E501
        :type: str
        """

        self._getref = getref

    @property
    def required(self):
        """Gets the required of this Header.  # noqa: E501


        :return: The required of this Header.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Header.


        :param required: The required of this Header.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def deprecated(self):
        """Gets the deprecated of this Header.  # noqa: E501


        :return: The deprecated of this Header.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this Header.


        :param deprecated: The deprecated of this Header.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def style(self):
        """Gets the style of this Header.  # noqa: E501


        :return: The style of this Header.  # noqa: E501
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this Header.


        :param style: The style of this Header.  # noqa: E501
        :type: str
        """
        allowed_values = ["simple"]  # noqa: E501
        if style not in allowed_values:
            raise ValueError(
                "Invalid value for `style` ({0}), must be one of {1}"  # noqa: E501
                .format(style, allowed_values)
            )

        self._style = style

    @property
    def explode(self):
        """Gets the explode of this Header.  # noqa: E501


        :return: The explode of this Header.  # noqa: E501
        :rtype: bool
        """
        return self._explode

    @explode.setter
    def explode(self, explode):
        """Sets the explode of this Header.


        :param explode: The explode of this Header.  # noqa: E501
        :type: bool
        """

        self._explode = explode

    @property
    def schema(self):
        """Gets the schema of this Header.  # noqa: E501


        :return: The schema of this Header.  # noqa: E501
        :rtype: Schema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this Header.


        :param schema: The schema of this Header.  # noqa: E501
        :type: Schema
        """

        self._schema = schema

    @property
    def examples(self):
        """Gets the examples of this Header.  # noqa: E501


        :return: The examples of this Header.  # noqa: E501
        :rtype: dict(str, Example)
        """
        return self._examples

    @examples.setter
    def examples(self, examples):
        """Sets the examples of this Header.


        :param examples: The examples of this Header.  # noqa: E501
        :type: dict(str, Example)
        """

        self._examples = examples

    @property
    def example(self):
        """Gets the example of this Header.  # noqa: E501


        :return: The example of this Header.  # noqa: E501
        :rtype: object
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this Header.


        :param example: The example of this Header.  # noqa: E501
        :type: object
        """

        self._example = example

    @property
    def extensions(self):
        """Gets the extensions of this Header.  # noqa: E501


        :return: The extensions of this Header.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this Header.


        :param extensions: The extensions of this Header.  # noqa: E501
        :type: dict(str, object)
        """

        self._extensions = extensions

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
        if not isinstance(other, Header):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
