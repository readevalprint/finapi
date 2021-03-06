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
from finapi.api.banks_api import BanksApi  # noqa: E501
from finapi.rest import ApiException


class TestBanksApi(unittest.TestCase):
    """BanksApi unit test stubs"""

    def setUp(self):
        self.api = finapi.api.banks_api.BanksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_and_search_all_banks(self):
        """Test case for get_and_search_all_banks

        Get and search all banks  # noqa: E501
        """
        pass

    def test_get_bank(self):
        """Test case for get_bank

        Get a bank  # noqa: E501
        """
        pass

    def test_get_multiple_banks(self):
        """Test case for get_multiple_banks

        Get multiple banks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
