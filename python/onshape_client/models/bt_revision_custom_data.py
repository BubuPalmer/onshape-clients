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


class BTRevisionCustomData(object):
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
        'valid_revision_reference': 'bool',
        'revision': 'str',
        'part_number': 'str',
        'export_type_name': 'str',
        'connection_source': 'BTConnection',
        'unknown_class': 'bool',
        'type_id': 'int'
    }

    attribute_map = {
        'valid_revision_reference': 'validRevisionReference',
        'revision': 'revision',
        'part_number': 'partNumber',
        'export_type_name': 'exportTypeName',
        'connection_source': 'connectionSource',
        'unknown_class': 'unknownClass',
        'type_id': 'typeId'
    }

    def __init__(self, valid_revision_reference=None, revision=None, part_number=None, export_type_name=None, connection_source=None, unknown_class=None, type_id=None):  # noqa: E501
        """BTRevisionCustomData - a model defined in OpenAPI"""  # noqa: E501

        self._valid_revision_reference = None
        self._revision = None
        self._part_number = None
        self._export_type_name = None
        self._connection_source = None
        self._unknown_class = None
        self._type_id = None
        self.discriminator = None

        if valid_revision_reference is not None:
            self.valid_revision_reference = valid_revision_reference
        if revision is not None:
            self.revision = revision
        if part_number is not None:
            self.part_number = part_number
        if export_type_name is not None:
            self.export_type_name = export_type_name
        if connection_source is not None:
            self.connection_source = connection_source
        if unknown_class is not None:
            self.unknown_class = unknown_class
        if type_id is not None:
            self.type_id = type_id

    @property
    def valid_revision_reference(self):
        """Gets the valid_revision_reference of this BTRevisionCustomData.  # noqa: E501


        :return: The valid_revision_reference of this BTRevisionCustomData.  # noqa: E501
        :rtype: bool
        """
        return self._valid_revision_reference

    @valid_revision_reference.setter
    def valid_revision_reference(self, valid_revision_reference):
        """Sets the valid_revision_reference of this BTRevisionCustomData.


        :param valid_revision_reference: The valid_revision_reference of this BTRevisionCustomData.  # noqa: E501
        :type: bool
        """

        self._valid_revision_reference = valid_revision_reference

    @property
    def revision(self):
        """Gets the revision of this BTRevisionCustomData.  # noqa: E501


        :return: The revision of this BTRevisionCustomData.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this BTRevisionCustomData.


        :param revision: The revision of this BTRevisionCustomData.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def part_number(self):
        """Gets the part_number of this BTRevisionCustomData.  # noqa: E501


        :return: The part_number of this BTRevisionCustomData.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTRevisionCustomData.


        :param part_number: The part_number of this BTRevisionCustomData.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def export_type_name(self):
        """Gets the export_type_name of this BTRevisionCustomData.  # noqa: E501


        :return: The export_type_name of this BTRevisionCustomData.  # noqa: E501
        :rtype: str
        """
        return self._export_type_name

    @export_type_name.setter
    def export_type_name(self, export_type_name):
        """Sets the export_type_name of this BTRevisionCustomData.


        :param export_type_name: The export_type_name of this BTRevisionCustomData.  # noqa: E501
        :type: str
        """

        self._export_type_name = export_type_name

    @property
    def connection_source(self):
        """Gets the connection_source of this BTRevisionCustomData.  # noqa: E501


        :return: The connection_source of this BTRevisionCustomData.  # noqa: E501
        :rtype: BTConnection
        """
        return self._connection_source

    @connection_source.setter
    def connection_source(self, connection_source):
        """Sets the connection_source of this BTRevisionCustomData.


        :param connection_source: The connection_source of this BTRevisionCustomData.  # noqa: E501
        :type: BTConnection
        """

        self._connection_source = connection_source

    @property
    def unknown_class(self):
        """Gets the unknown_class of this BTRevisionCustomData.  # noqa: E501


        :return: The unknown_class of this BTRevisionCustomData.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_class

    @unknown_class.setter
    def unknown_class(self, unknown_class):
        """Sets the unknown_class of this BTRevisionCustomData.


        :param unknown_class: The unknown_class of this BTRevisionCustomData.  # noqa: E501
        :type: bool
        """

        self._unknown_class = unknown_class

    @property
    def type_id(self):
        """Gets the type_id of this BTRevisionCustomData.  # noqa: E501


        :return: The type_id of this BTRevisionCustomData.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this BTRevisionCustomData.


        :param type_id: The type_id of this BTRevisionCustomData.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

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
        if not isinstance(other, BTRevisionCustomData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
