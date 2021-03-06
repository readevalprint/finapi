# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.64.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import finapi
from finapi.api.mandator_administration_api import MandatorAdministrationApi  # noqa: E501
from finapi.rest import ApiException


class TestMandatorAdministrationApi(unittest.TestCase):
    """MandatorAdministrationApi unit test stubs"""

    def setUp(self):
        self.api = finapi.api.mandator_administration_api.MandatorAdministrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_client_credentials(self):
        """Test case for change_client_credentials

        Change client credentials  # noqa: E501
        """
        pass

    def test_create_iban_rules(self):
        """Test case for create_iban_rules

        Create IBAN rules  # noqa: E501
        """
        pass

    def test_create_keyword_rules(self):
        """Test case for create_keyword_rules

        Create keyword rules  # noqa: E501
        """
        pass

    def test_delete_iban_rules(self):
        """Test case for delete_iban_rules

        Delete IBAN rules  # noqa: E501
        """
        pass

    def test_delete_keyword_rules(self):
        """Test case for delete_keyword_rules

        Delete keyword rules  # noqa: E501
        """
        pass

    def test_delete_users(self):
        """Test case for delete_users

        Delete users  # noqa: E501
        """
        pass

    def test_get_iban_rule_list(self):
        """Test case for get_iban_rule_list

        Get IBAN rules  # noqa: E501
        """
        pass

    def test_get_keyword_rule_list(self):
        """Test case for get_keyword_rule_list

        Get keyword rules  # noqa: E501
        """
        pass

    def test_get_user_list(self):
        """Test case for get_user_list

        Get user list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
