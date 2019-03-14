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

from finapi.models.keyword_rule import KeywordRule  # noqa: F401,E501
from finapi.models.paging import Paging  # noqa: F401,E501


class PageableKeywordRuleList(object):
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
        'keyword_rules': 'list[KeywordRule]',
        'paging': 'Paging'
    }

    attribute_map = {
        'keyword_rules': 'keywordRules',
        'paging': 'paging'
    }

    def __init__(self, keyword_rules=None, paging=None):  # noqa: E501
        """PageableKeywordRuleList - a model defined in Swagger"""  # noqa: E501

        self._keyword_rules = None
        self._paging = None
        self.discriminator = None

        self.keyword_rules = keyword_rules
        self.paging = paging

    @property
    def keyword_rules(self):
        """Gets the keyword_rules of this PageableKeywordRuleList.  # noqa: E501

        List of keyword rules  # noqa: E501

        :return: The keyword_rules of this PageableKeywordRuleList.  # noqa: E501
        :rtype: list[KeywordRule]
        """
        return self._keyword_rules

    @keyword_rules.setter
    def keyword_rules(self, keyword_rules):
        """Sets the keyword_rules of this PageableKeywordRuleList.

        List of keyword rules  # noqa: E501

        :param keyword_rules: The keyword_rules of this PageableKeywordRuleList.  # noqa: E501
        :type: list[KeywordRule]
        """
        if keyword_rules is None:
            raise ValueError("Invalid value for `keyword_rules`, must not be `None`")  # noqa: E501

        self._keyword_rules = keyword_rules

    @property
    def paging(self):
        """Gets the paging of this PageableKeywordRuleList.  # noqa: E501

        Information for pagination  # noqa: E501

        :return: The paging of this PageableKeywordRuleList.  # noqa: E501
        :rtype: Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this PageableKeywordRuleList.

        Information for pagination  # noqa: E501

        :param paging: The paging of this PageableKeywordRuleList.  # noqa: E501
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
        if issubclass(PageableKeywordRuleList, dict):
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
        if not isinstance(other, PageableKeywordRuleList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
