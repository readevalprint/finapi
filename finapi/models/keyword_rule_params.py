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


class KeywordRuleParams(object):
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
        'category_id': 'int',
        'direction': 'str',
        'keywords': 'list[str]'
    }

    attribute_map = {
        'category_id': 'categoryId',
        'direction': 'direction',
        'keywords': 'keywords'
    }

    def __init__(self, category_id=None, direction=None, keywords=None):  # noqa: E501
        """KeywordRuleParams - a model defined in Swagger"""  # noqa: E501

        self._category_id = None
        self._direction = None
        self._keywords = None
        self.discriminator = None

        self.category_id = category_id
        self.direction = direction
        self.keywords = keywords

    @property
    def category_id(self):
        """Gets the category_id of this KeywordRuleParams.  # noqa: E501

        ID of the category that this rule should assign to the matching transactions  # noqa: E501

        :return: The category_id of this KeywordRuleParams.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this KeywordRuleParams.

        ID of the category that this rule should assign to the matching transactions  # noqa: E501

        :param category_id: The category_id of this KeywordRuleParams.  # noqa: E501
        :type: int
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def direction(self):
        """Gets the direction of this KeywordRuleParams.  # noqa: E501

        Direction for the rule. 'Income' means that the rule applies to transactions with a positive amount only, 'Spending' means it applies to transactions with a negative amount only. 'Both' means that it applies to both kind of transactions. Note that in case of 'Both', finAPI will create two individual rules (one with direction 'Income' and one with direction 'Spending').  # noqa: E501

        :return: The direction of this KeywordRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this KeywordRuleParams.

        Direction for the rule. 'Income' means that the rule applies to transactions with a positive amount only, 'Spending' means it applies to transactions with a negative amount only. 'Both' means that it applies to both kind of transactions. Note that in case of 'Both', finAPI will create two individual rules (one with direction 'Income' and one with direction 'Spending').  # noqa: E501

        :param direction: The direction of this KeywordRuleParams.  # noqa: E501
        :type: str
        """
        if direction is None:
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501
        allowed_values = ["Income", "Spending", "Both"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def keywords(self):
        """Gets the keywords of this KeywordRuleParams.  # noqa: E501

        Set of keywords for the rule (Keywords are regarded case-insensitive). The minimum number of keywords is 1. The maximum number of keywords is 100.  # noqa: E501

        :return: The keywords of this KeywordRuleParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this KeywordRuleParams.

        Set of keywords for the rule (Keywords are regarded case-insensitive). The minimum number of keywords is 1. The maximum number of keywords is 100.  # noqa: E501

        :param keywords: The keywords of this KeywordRuleParams.  # noqa: E501
        :type: list[str]
        """
        if keywords is None:
            raise ValueError("Invalid value for `keywords`, must not be `None`")  # noqa: E501

        self._keywords = keywords

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
        if issubclass(KeywordRuleParams, dict):
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
        if not isinstance(other, KeywordRuleParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
