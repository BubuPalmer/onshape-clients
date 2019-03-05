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


class BTIdentity(object):
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
        'identity_id': 'str',
        'identity_type': 'str'
    }

    attribute_map = {
        'identity_id': 'identityId',
        'identity_type': 'identityType'
    }

    def __init__(self, identity_id=None, identity_type=None):  # noqa: E501
        """BTIdentity - a model defined in OpenAPI"""  # noqa: E501

        self._identity_id = None
        self._identity_type = None
        self.discriminator = None

        if identity_id is not None:
            self.identity_id = identity_id
        if identity_type is not None:
            self.identity_type = identity_type

    @property
    def identity_id(self):
        """Gets the identity_id of this BTIdentity.  # noqa: E501


        :return: The identity_id of this BTIdentity.  # noqa: E501
        :rtype: str
        """
        return self._identity_id

    @identity_id.setter
    def identity_id(self, identity_id):
        """Sets the identity_id of this BTIdentity.


        :param identity_id: The identity_id of this BTIdentity.  # noqa: E501
        :type: str
        """

        self._identity_id = identity_id

    @property
    def identity_type(self):
        """Gets the identity_type of this BTIdentity.  # noqa: E501


        :return: The identity_type of this BTIdentity.  # noqa: E501
        :rtype: str
        """
        return self._identity_type

    @identity_type.setter
    def identity_type(self, identity_type):
        """Sets the identity_type of this BTIdentity.


        :param identity_type: The identity_type of this BTIdentity.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER", "TEAM"]  # noqa: E501
        if identity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `identity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(identity_type, allowed_values)
            )

        self._identity_type = identity_type

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
        if not isinstance(other, BTIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
