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


class Coupon(object):
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
        'id': 'str',
        'object': 'str',
        'amount_off': 'int',
        'created': 'int',
        'currency': 'str',
        'duration': 'str',
        'duration_in_months': 'int',
        'livemode': 'bool',
        'max_redemptions': 'int',
        'metadata': 'dict(str, str)',
        'percent_off': 'int',
        'redeem_by': 'int',
        'times_redeemed': 'int',
        'valid': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'object': 'object',
        'amount_off': 'amountOff',
        'created': 'created',
        'currency': 'currency',
        'duration': 'duration',
        'duration_in_months': 'durationInMonths',
        'livemode': 'livemode',
        'max_redemptions': 'maxRedemptions',
        'metadata': 'metadata',
        'percent_off': 'percentOff',
        'redeem_by': 'redeemBy',
        'times_redeemed': 'timesRedeemed',
        'valid': 'valid'
    }

    def __init__(self, id=None, object=None, amount_off=None, created=None, currency=None, duration=None, duration_in_months=None, livemode=None, max_redemptions=None, metadata=None, percent_off=None, redeem_by=None, times_redeemed=None, valid=None):  # noqa: E501
        """Coupon - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._object = None
        self._amount_off = None
        self._created = None
        self._currency = None
        self._duration = None
        self._duration_in_months = None
        self._livemode = None
        self._max_redemptions = None
        self._metadata = None
        self._percent_off = None
        self._redeem_by = None
        self._times_redeemed = None
        self._valid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if object is not None:
            self.object = object
        if amount_off is not None:
            self.amount_off = amount_off
        if created is not None:
            self.created = created
        if currency is not None:
            self.currency = currency
        if duration is not None:
            self.duration = duration
        if duration_in_months is not None:
            self.duration_in_months = duration_in_months
        if livemode is not None:
            self.livemode = livemode
        if max_redemptions is not None:
            self.max_redemptions = max_redemptions
        if metadata is not None:
            self.metadata = metadata
        if percent_off is not None:
            self.percent_off = percent_off
        if redeem_by is not None:
            self.redeem_by = redeem_by
        if times_redeemed is not None:
            self.times_redeemed = times_redeemed
        if valid is not None:
            self.valid = valid

    @property
    def id(self):
        """Gets the id of this Coupon.  # noqa: E501


        :return: The id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Coupon.


        :param id: The id of this Coupon.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """Gets the object of this Coupon.  # noqa: E501


        :return: The object of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Coupon.


        :param object: The object of this Coupon.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def amount_off(self):
        """Gets the amount_off of this Coupon.  # noqa: E501


        :return: The amount_off of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._amount_off

    @amount_off.setter
    def amount_off(self, amount_off):
        """Sets the amount_off of this Coupon.


        :param amount_off: The amount_off of this Coupon.  # noqa: E501
        :type: int
        """

        self._amount_off = amount_off

    @property
    def created(self):
        """Gets the created of this Coupon.  # noqa: E501


        :return: The created of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Coupon.


        :param created: The created of this Coupon.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def currency(self):
        """Gets the currency of this Coupon.  # noqa: E501


        :return: The currency of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Coupon.


        :param currency: The currency of this Coupon.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def duration(self):
        """Gets the duration of this Coupon.  # noqa: E501


        :return: The duration of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Coupon.


        :param duration: The duration of this Coupon.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def duration_in_months(self):
        """Gets the duration_in_months of this Coupon.  # noqa: E501


        :return: The duration_in_months of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._duration_in_months

    @duration_in_months.setter
    def duration_in_months(self, duration_in_months):
        """Sets the duration_in_months of this Coupon.


        :param duration_in_months: The duration_in_months of this Coupon.  # noqa: E501
        :type: int
        """

        self._duration_in_months = duration_in_months

    @property
    def livemode(self):
        """Gets the livemode of this Coupon.  # noqa: E501


        :return: The livemode of this Coupon.  # noqa: E501
        :rtype: bool
        """
        return self._livemode

    @livemode.setter
    def livemode(self, livemode):
        """Sets the livemode of this Coupon.


        :param livemode: The livemode of this Coupon.  # noqa: E501
        :type: bool
        """

        self._livemode = livemode

    @property
    def max_redemptions(self):
        """Gets the max_redemptions of this Coupon.  # noqa: E501


        :return: The max_redemptions of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._max_redemptions

    @max_redemptions.setter
    def max_redemptions(self, max_redemptions):
        """Sets the max_redemptions of this Coupon.


        :param max_redemptions: The max_redemptions of this Coupon.  # noqa: E501
        :type: int
        """

        self._max_redemptions = max_redemptions

    @property
    def metadata(self):
        """Gets the metadata of this Coupon.  # noqa: E501


        :return: The metadata of this Coupon.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Coupon.


        :param metadata: The metadata of this Coupon.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def percent_off(self):
        """Gets the percent_off of this Coupon.  # noqa: E501


        :return: The percent_off of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._percent_off

    @percent_off.setter
    def percent_off(self, percent_off):
        """Sets the percent_off of this Coupon.


        :param percent_off: The percent_off of this Coupon.  # noqa: E501
        :type: int
        """

        self._percent_off = percent_off

    @property
    def redeem_by(self):
        """Gets the redeem_by of this Coupon.  # noqa: E501


        :return: The redeem_by of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._redeem_by

    @redeem_by.setter
    def redeem_by(self, redeem_by):
        """Sets the redeem_by of this Coupon.


        :param redeem_by: The redeem_by of this Coupon.  # noqa: E501
        :type: int
        """

        self._redeem_by = redeem_by

    @property
    def times_redeemed(self):
        """Gets the times_redeemed of this Coupon.  # noqa: E501


        :return: The times_redeemed of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._times_redeemed

    @times_redeemed.setter
    def times_redeemed(self, times_redeemed):
        """Sets the times_redeemed of this Coupon.


        :param times_redeemed: The times_redeemed of this Coupon.  # noqa: E501
        :type: int
        """

        self._times_redeemed = times_redeemed

    @property
    def valid(self):
        """Gets the valid of this Coupon.  # noqa: E501


        :return: The valid of this Coupon.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this Coupon.


        :param valid: The valid of this Coupon.  # noqa: E501
        :type: bool
        """

        self._valid = valid

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
        if not isinstance(other, Coupon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
