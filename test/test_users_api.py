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
from finapi.api.users_api import UsersApi  # noqa: E501
from finapi.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = finapi.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a new user  # noqa: E501
        """
        pass

    def test_delete_authorized_user(self):
        """Test case for delete_authorized_user

        Delete the authorized user  # noqa: E501
        """
        pass

    def test_delete_unverified_user(self):
        """Test case for delete_unverified_user

        Delete an unverified user  # noqa: E501
        """
        pass

    def test_edit_authorized_user(self):
        """Test case for edit_authorized_user

        Edit the authorized user  # noqa: E501
        """
        pass

    def test_execute_password_change(self):
        """Test case for execute_password_change

        Execute password change  # noqa: E501
        """
        pass

    def test_get_authorized_user(self):
        """Test case for get_authorized_user

        Get the authorized user  # noqa: E501
        """
        pass

    def test_get_verification_status(self):
        """Test case for get_verification_status

        Get a user's verification status  # noqa: E501
        """
        pass

    def test_request_password_change(self):
        """Test case for request_password_change

        Request password change  # noqa: E501
        """
        pass

    def test_verify_user(self):
        """Test case for verify_user

        Verify a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
