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
from finapi.api.authorization_api import AuthorizationApi  # noqa: E501
from finapi.rest import ApiException


class TestAuthorizationApi(unittest.TestCase):
    """AuthorizationApi unit test stubs"""

    def setUp(self):
        self.api = finapi.api.authorization_api.AuthorizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_token(self):
        """Test case for get_token

        Get tokens  # noqa: E501
        """
        pass

    def test_revoke_token(self):
        """Test case for revoke_token

        Revoke a token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()