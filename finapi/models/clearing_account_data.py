# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.64.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClearingAccountData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'clearing_account_id': 'str',
        'clearing_account_name': 'str'
    }

    attribute_map = {
        'clearing_account_id': 'clearingAccountId',
        'clearing_account_name': 'clearingAccountName'
    }

    def __init__(self, clearing_account_id=None, clearing_account_name=None):  # noqa: E501
        """ClearingAccountData - a model defined in Swagger"""  # noqa: E501

        self._clearing_account_id = None
        self._clearing_account_name = None
        self.discriminator = None

        self.clearing_account_id = clearing_account_id
        self.clearing_account_name = clearing_account_name

    @property
    def clearing_account_id(self):
        """Gets the clearing_account_id of this ClearingAccountData.  # noqa: E501

        Technical identifier of the clearing account  # noqa: E501

        :return: The clearing_account_id of this ClearingAccountData.  # noqa: E501
        :rtype: str
        """
        return self._clearing_account_id

    @clearing_account_id.setter
    def clearing_account_id(self, clearing_account_id):
        """Sets the clearing_account_id of this ClearingAccountData.

        Technical identifier of the clearing account  # noqa: E501

        :param clearing_account_id: The clearing_account_id of this ClearingAccountData.  # noqa: E501
        :type: str
        """
        if clearing_account_id is None:
            raise ValueError("Invalid value for `clearing_account_id`, must not be `None`")  # noqa: E501

        self._clearing_account_id = clearing_account_id

    @property
    def clearing_account_name(self):
        """Gets the clearing_account_name of this ClearingAccountData.  # noqa: E501

        Name of the clearing account  # noqa: E501

        :return: The clearing_account_name of this ClearingAccountData.  # noqa: E501
        :rtype: str
        """
        return self._clearing_account_name

    @clearing_account_name.setter
    def clearing_account_name(self, clearing_account_name):
        """Sets the clearing_account_name of this ClearingAccountData.

        Name of the clearing account  # noqa: E501

        :param clearing_account_name: The clearing_account_name of this ClearingAccountData.  # noqa: E501
        :type: str
        """
        if clearing_account_name is None:
            raise ValueError("Invalid value for `clearing_account_name`, must not be `None`")  # noqa: E501

        self._clearing_account_name = clearing_account_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ClearingAccountData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClearingAccountData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
