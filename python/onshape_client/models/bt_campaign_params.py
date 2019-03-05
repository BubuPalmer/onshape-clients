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


class BTCampaignParams(object):
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
        'terminated': 'bool',
        'campaign_name': 'str',
        'messages': 'list[Message]'
    }

    attribute_map = {
        'terminated': 'terminated',
        'campaign_name': 'campaignName',
        'messages': 'messages'
    }

    def __init__(self, terminated=None, campaign_name=None, messages=None):  # noqa: E501
        """BTCampaignParams - a model defined in OpenAPI"""  # noqa: E501

        self._terminated = None
        self._campaign_name = None
        self._messages = None
        self.discriminator = None

        if terminated is not None:
            self.terminated = terminated
        if campaign_name is not None:
            self.campaign_name = campaign_name
        if messages is not None:
            self.messages = messages

    @property
    def terminated(self):
        """Gets the terminated of this BTCampaignParams.  # noqa: E501


        :return: The terminated of this BTCampaignParams.  # noqa: E501
        :rtype: bool
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this BTCampaignParams.


        :param terminated: The terminated of this BTCampaignParams.  # noqa: E501
        :type: bool
        """

        self._terminated = terminated

    @property
    def campaign_name(self):
        """Gets the campaign_name of this BTCampaignParams.  # noqa: E501


        :return: The campaign_name of this BTCampaignParams.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this BTCampaignParams.


        :param campaign_name: The campaign_name of this BTCampaignParams.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def messages(self):
        """Gets the messages of this BTCampaignParams.  # noqa: E501


        :return: The messages of this BTCampaignParams.  # noqa: E501
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this BTCampaignParams.


        :param messages: The messages of this BTCampaignParams.  # noqa: E501
        :type: list[Message]
        """

        self._messages = messages

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
        if not isinstance(other, BTCampaignParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
