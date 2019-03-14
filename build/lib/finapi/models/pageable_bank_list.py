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

from finapi.models.bank import Bank  # noqa: F401,E501
from finapi.models.paging import Paging  # noqa: F401,E501


class PageableBankList(object):
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
        'banks': 'list[Bank]',
        'paging': 'Paging'
    }

    attribute_map = {
        'banks': 'banks',
        'paging': 'paging'
    }

    def __init__(self, banks=None, paging=None):  # noqa: E501
        """PageableBankList - a model defined in Swagger"""  # noqa: E501

        self._banks = None
        self._paging = None
        self.discriminator = None

        self.banks = banks
        self.paging = paging

    @property
    def banks(self):
        """Gets the banks of this PageableBankList.  # noqa: E501

        Banks data  # noqa: E501

        :return: The banks of this PageableBankList.  # noqa: E501
        :rtype: list[Bank]
        """
        return self._banks

    @banks.setter
    def banks(self, banks):
        """Sets the banks of this PageableBankList.

        Banks data  # noqa: E501

        :param banks: The banks of this PageableBankList.  # noqa: E501
        :type: list[Bank]
        """
        if banks is None:
            raise ValueError("Invalid value for `banks`, must not be `None`")  # noqa: E501

        self._banks = banks

    @property
    def paging(self):
        """Gets the paging of this PageableBankList.  # noqa: E501

        Information for pagination  # noqa: E501

        :return: The paging of this PageableBankList.  # noqa: E501
        :rtype: Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this PageableBankList.

        Information for pagination  # noqa: E501

        :param paging: The paging of this PageableBankList.  # noqa: E501
        :type: Paging
        """
        if paging is None:
            raise ValueError("Invalid value for `paging`, must not be `None`")  # noqa: E501

        self._paging = paging

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
        if issubclass(PageableBankList, dict):
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
        if not isinstance(other, PageableBankList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
