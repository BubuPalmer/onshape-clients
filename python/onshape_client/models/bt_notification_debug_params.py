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


class BTNotificationDebugParams(object):
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
        'debug_submitted': 'bool'
    }

    attribute_map = {
        'debug_submitted': 'debugSubmitted'
    }

    def __init__(self, debug_submitted=None):  # noqa: E501
        """BTNotificationDebugParams - a model defined in OpenAPI"""  # noqa: E501

        self._debug_submitted = None
        self.discriminator = None

        if debug_submitted is not None:
            self.debug_submitted = debug_submitted

    @property
    def debug_submitted(self):
        """Gets the debug_submitted of this BTNotificationDebugParams.  # noqa: E501


        :return: The debug_submitted of this BTNotificationDebugParams.  # noqa: E501
        :rtype: bool
        """
        return self._debug_submitted

    @debug_submitted.setter
    def debug_submitted(self, debug_submitted):
        """Sets the debug_submitted of this BTNotificationDebugParams.


        :param debug_submitted: The debug_submitted of this BTNotificationDebugParams.  # noqa: E501
        :type: bool
        """

        self._debug_submitted = debug_submitted

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
        if not isinstance(other, BTNotificationDebugParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
