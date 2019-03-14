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

from finapi.models.iban_rule_params import IbanRuleParams  # noqa: F401,E501


class IbanRulesParams(object):
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
        'iban_rules': 'list[IbanRuleParams]'
    }

    attribute_map = {
        'iban_rules': 'ibanRules'
    }

    def __init__(self, iban_rules=None):  # noqa: E501
        """IbanRulesParams - a model defined in Swagger"""  # noqa: E501

        self._iban_rules = None
        self.discriminator = None

        self.iban_rules = iban_rules

    @property
    def iban_rules(self):
        """Gets the iban_rules of this IbanRulesParams.  # noqa: E501

        IBAN rule definitions. The minimum number of rule definitions is 1. The maximum number of rule definitions is 100.  # noqa: E501

        :return: The iban_rules of this IbanRulesParams.  # noqa: E501
        :rtype: list[IbanRuleParams]
        """
        return self._iban_rules

    @iban_rules.setter
    def iban_rules(self, iban_rules):
        """Sets the iban_rules of this IbanRulesParams.

        IBAN rule definitions. The minimum number of rule definitions is 1. The maximum number of rule definitions is 100.  # noqa: E501

        :param iban_rules: The iban_rules of this IbanRulesParams.  # noqa: E501
        :type: list[IbanRuleParams]
        """
        if iban_rules is None:
            raise ValueError("Invalid value for `iban_rules`, must not be `None`")  # noqa: E501

        self._iban_rules = iban_rules

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
        if issubclass(IbanRulesParams, dict):
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
        if not isinstance(other, IbanRulesParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other