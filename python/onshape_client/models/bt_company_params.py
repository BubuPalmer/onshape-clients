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


class BTCompanyParams(object):
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
        'id': 'str',
        'address': 'BTAddressInfo',
        'description': 'str',
        'domain_prefix': 'str',
        'owner_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'address': 'address',
        'description': 'description',
        'domain_prefix': 'domainPrefix',
        'owner_id': 'ownerId'
    }

    def __init__(self, name=None, id=None, address=None, description=None, domain_prefix=None, owner_id=None):  # noqa: E501
        """BTCompanyParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._id = None
        self._address = None
        self._description = None
        self._domain_prefix = None
        self._owner_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if description is not None:
            self.description = description
        if domain_prefix is not None:
            self.domain_prefix = domain_prefix
        if owner_id is not None:
            self.owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this BTCompanyParams.  # noqa: E501


        :return: The name of this BTCompanyParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTCompanyParams.


        :param name: The name of this BTCompanyParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTCompanyParams.  # noqa: E501


        :return: The id of this BTCompanyParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTCompanyParams.


        :param id: The id of this BTCompanyParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this BTCompanyParams.  # noqa: E501


        :return: The address of this BTCompanyParams.  # noqa: E501
        :rtype: BTAddressInfo
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BTCompanyParams.


        :param address: The address of this BTCompanyParams.  # noqa: E501
        :type: BTAddressInfo
        """

        self._address = address

    @property
    def description(self):
        """Gets the description of this BTCompanyParams.  # noqa: E501


        :return: The description of this BTCompanyParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTCompanyParams.


        :param description: The description of this BTCompanyParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def domain_prefix(self):
        """Gets the domain_prefix of this BTCompanyParams.  # noqa: E501


        :return: The domain_prefix of this BTCompanyParams.  # noqa: E501
        :rtype: str
        """
        return self._domain_prefix

    @domain_prefix.setter
    def domain_prefix(self, domain_prefix):
        """Sets the domain_prefix of this BTCompanyParams.


        :param domain_prefix: The domain_prefix of this BTCompanyParams.  # noqa: E501
        :type: str
        """

        self._domain_prefix = domain_prefix

    @property
    def owner_id(self):
        """Gets the owner_id of this BTCompanyParams.  # noqa: E501


        :return: The owner_id of this BTCompanyParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BTCompanyParams.


        :param owner_id: The owner_id of this BTCompanyParams.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

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
        if not isinstance(other, BTCompanyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
