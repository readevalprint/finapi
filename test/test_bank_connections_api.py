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
from finapi.api.bank_connections_api import BankConnectionsApi  # noqa: E501
from finapi.rest import ApiException


class TestBankConnectionsApi(unittest.TestCase):
    """BankConnectionsApi unit test stubs"""

    def setUp(self):
        self.api = finapi.api.bank_connections_api.BankConnectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_all_bank_connections(self):
        """Test case for delete_all_bank_connections

        Delete all bank connections  # noqa: E501
        """
        pass

    def test_delete_bank_connection(self):
        """Test case for delete_bank_connection

        Delete a bank connection  # noqa: E501
        """
        pass

    def test_edit_bank_connection(self):
        """Test case for edit_bank_connection

        Edit a bank connection  # noqa: E501
        """
        pass

    def test_get_all_bank_connections(self):
        """Test case for get_all_bank_connections

        Get all bank connections  # noqa: E501
        """
        pass

    def test_get_bank_connection(self):
        """Test case for get_bank_connection

        Get a bank connection  # noqa: E501
        """
        pass

    def test_get_multiple_bank_connections(self):
        """Test case for get_multiple_bank_connections

        Get multiple bank connections  # noqa: E501
        """
        pass

    def test_import_bank_connection(self):
        """Test case for import_bank_connection

        Import a new bank connection  # noqa: E501
        """
        pass

    def test_update_bank_connection(self):
        """Test case for update_bank_connection

        Update a bank connection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
