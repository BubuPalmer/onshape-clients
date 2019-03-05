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


class BTDBViewerCollectionConfig(object):
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
        'collection': 'str',
        'db': 'str',
        'query_fields': 'list[str]',
        'hidden_fields': 'list[str]',
        'binary_fields': 'list[str]',
        'has_created_date': 'bool'
    }

    attribute_map = {
        'collection': 'collection',
        'db': 'db',
        'query_fields': 'queryFields',
        'hidden_fields': 'hiddenFields',
        'binary_fields': 'binaryFields',
        'has_created_date': 'hasCreatedDate'
    }

    def __init__(self, collection=None, db=None, query_fields=None, hidden_fields=None, binary_fields=None, has_created_date=None):  # noqa: E501
        """BTDBViewerCollectionConfig - a model defined in OpenAPI"""  # noqa: E501

        self._collection = None
        self._db = None
        self._query_fields = None
        self._hidden_fields = None
        self._binary_fields = None
        self._has_created_date = None
        self.discriminator = None

        if collection is not None:
            self.collection = collection
        if db is not None:
            self.db = db
        if query_fields is not None:
            self.query_fields = query_fields
        if hidden_fields is not None:
            self.hidden_fields = hidden_fields
        if binary_fields is not None:
            self.binary_fields = binary_fields
        if has_created_date is not None:
            self.has_created_date = has_created_date

    @property
    def collection(self):
        """Gets the collection of this BTDBViewerCollectionConfig.  # noqa: E501


        :return: The collection of this BTDBViewerCollectionConfig.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this BTDBViewerCollectionConfig.


        :param collection: The collection of this BTDBViewerCollectionConfig.  # noqa: E501
        :type: str
        """

        self._collection = collection

    @property
    def db(self):
        """Gets the db of this BTDBViewerCollectionConfig.  # noqa: E501


        :return: The db of this BTDBViewerCollectionConfig.  # noqa: E501
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this BTDBViewerCollectionConfig.


        :param db: The db of this BTDBViewerCollectionConfig.  # noqa: E501
        :type: str
        """

        self._db = db

    @property
    def query_fields(self):
        """Gets the query_fields of this BTDBViewerCollectionConfig.  # noqa: E501


        :return: The query_fields of this BTDBViewerCollectionConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._query_fields

    @query_fields.setter
    def query_fields(self, query_fields):
        """Sets the query_fields of this BTDBViewerCollectionConfig.


        :param query_fields: The query_fields of this BTDBViewerCollectionConfig.  # noqa: E501
        :type: list[str]
        """

        self._query_fields = query_fields

    @property
    def hidden_fields(self):
        """Gets the hidden_fields of this BTDBViewerCollectionConfig.  # noqa: E501


        :return: The hidden_fields of this BTDBViewerCollectionConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._hidden_fields

    @hidden_fields.setter
    def hidden_fields(self, hidden_fields):
        """Sets the hidden_fields of this BTDBViewerCollectionConfig.


        :param hidden_fields: The hidden_fields of this BTDBViewerCollectionConfig.  # noqa: E501
        :type: list[str]
        """

        self._hidden_fields = hidden_fields

    @property
    def binary_fields(self):
        """Gets the binary_fields of this BTDBViewerCollectionConfig.  # noqa: E501


        :return: The binary_fields of this BTDBViewerCollectionConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._binary_fields

    @binary_fields.setter
    def binary_fields(self, binary_fields):
        """Sets the binary_fields of this BTDBViewerCollectionConfig.


        :param binary_fields: The binary_fields of this BTDBViewerCollectionConfig.  # noqa: E501
        :type: list[str]
        """

        self._binary_fields = binary_fields

    @property
    def has_created_date(self):
        """Gets the has_created_date of this BTDBViewerCollectionConfig.  # noqa: E501


        :return: The has_created_date of this BTDBViewerCollectionConfig.  # noqa: E501
        :rtype: bool
        """
        return self._has_created_date

    @has_created_date.setter
    def has_created_date(self, has_created_date):
        """Sets the has_created_date of this BTDBViewerCollectionConfig.


        :param has_created_date: The has_created_date of this BTDBViewerCollectionConfig.  # noqa: E501
        :type: bool
        """

        self._has_created_date = has_created_date

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
        if not isinstance(other, BTDBViewerCollectionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
