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


class BTUserUpdateSpecsParams(object):
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
        'spec_signature_to_version': 'dict(str, str)'
    }

    attribute_map = {
        'spec_signature_to_version': 'specSignatureToVersion'
    }

    def __init__(self, spec_signature_to_version=None):  # noqa: E501
        """BTUserUpdateSpecsParams - a model defined in OpenAPI"""  # noqa: E501

        self._spec_signature_to_version = None
        self.discriminator = None

        if spec_signature_to_version is not None:
            self.spec_signature_to_version = spec_signature_to_version

    @property
    def spec_signature_to_version(self):
        """Gets the spec_signature_to_version of this BTUserUpdateSpecsParams.  # noqa: E501


        :return: The spec_signature_to_version of this BTUserUpdateSpecsParams.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._spec_signature_to_version

    @spec_signature_to_version.setter
    def spec_signature_to_version(self, spec_signature_to_version):
        """Sets the spec_signature_to_version of this BTUserUpdateSpecsParams.


        :param spec_signature_to_version: The spec_signature_to_version of this BTUserUpdateSpecsParams.  # noqa: E501
        :type: dict(str, str)
        """

        self._spec_signature_to_version = spec_signature_to_version

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
        if not isinstance(other, BTUserUpdateSpecsParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
