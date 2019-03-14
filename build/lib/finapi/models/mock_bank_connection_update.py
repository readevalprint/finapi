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

from finapi.models.mock_account_data import MockAccountData  # noqa: F401,E501


class MockBankConnectionUpdate(object):
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
        'bank_connection_id': 'int',
        'simulate_bank_login_error': 'bool',
        'mock_accounts_data': 'list[MockAccountData]'
    }

    attribute_map = {
        'bank_connection_id': 'bankConnectionId',
        'simulate_bank_login_error': 'simulateBankLoginError',
        'mock_accounts_data': 'mockAccountsData'
    }

    def __init__(self, bank_connection_id=None, simulate_bank_login_error=False, mock_accounts_data=None):  # noqa: E501
        """MockBankConnectionUpdate - a model defined in Swagger"""  # noqa: E501

        self._bank_connection_id = None
        self._simulate_bank_login_error = None
        self._mock_accounts_data = None
        self.discriminator = None

        self.bank_connection_id = bank_connection_id
        if simulate_bank_login_error is not None:
            self.simulate_bank_login_error = simulate_bank_login_error
        if mock_accounts_data is not None:
            self.mock_accounts_data = mock_accounts_data

    @property
    def bank_connection_id(self):
        """Gets the bank_connection_id of this MockBankConnectionUpdate.  # noqa: E501

        Bank connection identifier  # noqa: E501

        :return: The bank_connection_id of this MockBankConnectionUpdate.  # noqa: E501
        :rtype: int
        """
        return self._bank_connection_id

    @bank_connection_id.setter
    def bank_connection_id(self, bank_connection_id):
        """Sets the bank_connection_id of this MockBankConnectionUpdate.

        Bank connection identifier  # noqa: E501

        :param bank_connection_id: The bank_connection_id of this MockBankConnectionUpdate.  # noqa: E501
        :type: int
        """
        if bank_connection_id is None:
            raise ValueError("Invalid value for `bank_connection_id`, must not be `None`")  # noqa: E501

        self._bank_connection_id = bank_connection_id

    @property
    def simulate_bank_login_error(self):
        """Gets the simulate_bank_login_error of this MockBankConnectionUpdate.  # noqa: E501

        Whether to simulate the case that the update fails due to incorrect banking credentials. Note that there is no real communication to any bank server involved, so you won't lock your accounts when enabling this flag. Default value is 'false'.  # noqa: E501

        :return: The simulate_bank_login_error of this MockBankConnectionUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._simulate_bank_login_error

    @simulate_bank_login_error.setter
    def simulate_bank_login_error(self, simulate_bank_login_error):
        """Sets the simulate_bank_login_error of this MockBankConnectionUpdate.

        Whether to simulate the case that the update fails due to incorrect banking credentials. Note that there is no real communication to any bank server involved, so you won't lock your accounts when enabling this flag. Default value is 'false'.  # noqa: E501

        :param simulate_bank_login_error: The simulate_bank_login_error of this MockBankConnectionUpdate.  # noqa: E501
        :type: bool
        """

        self._simulate_bank_login_error = simulate_bank_login_error

    @property
    def mock_accounts_data(self):
        """Gets the mock_accounts_data of this MockBankConnectionUpdate.  # noqa: E501

        Mock accounts data. Note that for accounts that exist in a bank connection but that you do not specify in this list, the service will act like those accounts are not received by the bank servers. This means that any accounts that you do not specify here will be marked as deprecated. If you do not specify this list at all, all accounts in the bank connection will be marked as deprecated.  # noqa: E501

        :return: The mock_accounts_data of this MockBankConnectionUpdate.  # noqa: E501
        :rtype: list[MockAccountData]
        """
        return self._mock_accounts_data

    @mock_accounts_data.setter
    def mock_accounts_data(self, mock_accounts_data):
        """Sets the mock_accounts_data of this MockBankConnectionUpdate.

        Mock accounts data. Note that for accounts that exist in a bank connection but that you do not specify in this list, the service will act like those accounts are not received by the bank servers. This means that any accounts that you do not specify here will be marked as deprecated. If you do not specify this list at all, all accounts in the bank connection will be marked as deprecated.  # noqa: E501

        :param mock_accounts_data: The mock_accounts_data of this MockBankConnectionUpdate.  # noqa: E501
        :type: list[MockAccountData]
        """

        self._mock_accounts_data = mock_accounts_data

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
        if issubclass(MockBankConnectionUpdate, dict):
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
        if not isinstance(other, MockBankConnectionUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other