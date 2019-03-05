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


class SecurityScheme(object):
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
        'type': 'str',
        'description': 'str',
        'name': 'str',
        'getref': 'str',
        '_in': 'str',
        'scheme': 'str',
        'bearer_format': 'str',
        'flows': 'OAuthFlows',
        'open_id_connect_url': 'str',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'description': 'description',
        'name': 'name',
        'getref': 'get$ref',
        '_in': 'in',
        'scheme': 'scheme',
        'bearer_format': 'bearerFormat',
        'flows': 'flows',
        'open_id_connect_url': 'openIdConnectUrl',
        'extensions': 'extensions'
    }

    def __init__(self, type=None, description=None, name=None, getref=None, _in=None, scheme=None, bearer_format=None, flows=None, open_id_connect_url=None, extensions=None):  # noqa: E501
        """SecurityScheme - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._description = None
        self._name = None
        self._getref = None
        self.__in = None
        self._scheme = None
        self._bearer_format = None
        self._flows = None
        self._open_id_connect_url = None
        self._extensions = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if getref is not None:
            self.getref = getref
        if _in is not None:
            self._in = _in
        if scheme is not None:
            self.scheme = scheme
        if bearer_format is not None:
            self.bearer_format = bearer_format
        if flows is not None:
            self.flows = flows
        if open_id_connect_url is not None:
            self.open_id_connect_url = open_id_connect_url
        if extensions is not None:
            self.extensions = extensions

    @property
    def type(self):
        """Gets the type of this SecurityScheme.  # noqa: E501


        :return: The type of this SecurityScheme.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SecurityScheme.


        :param type: The type of this SecurityScheme.  # noqa: E501
        :type: str
        """
        allowed_values = ["apiKey", "http", "oauth2", "openIdConnect"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self):
        """Gets the description of this SecurityScheme.  # noqa: E501


        :return: The description of this SecurityScheme.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityScheme.


        :param description: The description of this SecurityScheme.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this SecurityScheme.  # noqa: E501


        :return: The name of this SecurityScheme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityScheme.


        :param name: The name of this SecurityScheme.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def getref(self):
        """Gets the getref of this SecurityScheme.  # noqa: E501


        :return: The getref of this SecurityScheme.  # noqa: E501
        :rtype: str
        """
        return self._getref

    @getref.setter
    def getref(self, getref):
        """Sets the getref of this SecurityScheme.


        :param getref: The getref of this SecurityScheme.  # noqa: E501
        :type: str
        """

        self._getref = getref

    @property
    def _in(self):
        """Gets the _in of this SecurityScheme.  # noqa: E501


        :return: The _in of this SecurityScheme.  # noqa: E501
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this SecurityScheme.


        :param _in: The _in of this SecurityScheme.  # noqa: E501
        :type: str
        """
        allowed_values = ["cookie", "header", "query"]  # noqa: E501
        if _in not in allowed_values:
            raise ValueError(
                "Invalid value for `_in` ({0}), must be one of {1}"  # noqa: E501
                .format(_in, allowed_values)
            )

        self.__in = _in

    @property
    def scheme(self):
        """Gets the scheme of this SecurityScheme.  # noqa: E501


        :return: The scheme of this SecurityScheme.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this SecurityScheme.


        :param scheme: The scheme of this SecurityScheme.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

    @property
    def bearer_format(self):
        """Gets the bearer_format of this SecurityScheme.  # noqa: E501


        :return: The bearer_format of this SecurityScheme.  # noqa: E501
        :rtype: str
        """
        return self._bearer_format

    @bearer_format.setter
    def bearer_format(self, bearer_format):
        """Sets the bearer_format of this SecurityScheme.


        :param bearer_format: The bearer_format of this SecurityScheme.  # noqa: E501
        :type: str
        """

        self._bearer_format = bearer_format

    @property
    def flows(self):
        """Gets the flows of this SecurityScheme.  # noqa: E501


        :return: The flows of this SecurityScheme.  # noqa: E501
        :rtype: OAuthFlows
        """
        return self._flows

    @flows.setter
    def flows(self, flows):
        """Sets the flows of this SecurityScheme.


        :param flows: The flows of this SecurityScheme.  # noqa: E501
        :type: OAuthFlows
        """

        self._flows = flows

    @property
    def open_id_connect_url(self):
        """Gets the open_id_connect_url of this SecurityScheme.  # noqa: E501


        :return: The open_id_connect_url of this SecurityScheme.  # noqa: E501
        :rtype: str
        """
        return self._open_id_connect_url

    @open_id_connect_url.setter
    def open_id_connect_url(self, open_id_connect_url):
        """Sets the open_id_connect_url of this SecurityScheme.


        :param open_id_connect_url: The open_id_connect_url of this SecurityScheme.  # noqa: E501
        :type: str
        """

        self._open_id_connect_url = open_id_connect_url

    @property
    def extensions(self):
        """Gets the extensions of this SecurityScheme.  # noqa: E501


        :return: The extensions of this SecurityScheme.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this SecurityScheme.


        :param extensions: The extensions of this SecurityScheme.  # noqa: E501
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
        if not isinstance(other, SecurityScheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
