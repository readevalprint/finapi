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


class UpdateResult(object):
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
        'result': 'str',
        'error_message': 'str',
        'error_type': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'result': 'result',
        'error_message': 'errorMessage',
        'error_type': 'errorType',
        'timestamp': 'timestamp'
    }

    def __init__(self, result=None, error_message=None, error_type=None, timestamp=None):  # noqa: E501
        """UpdateResult - a model defined in Swagger"""  # noqa: E501

        self._result = None
        self._error_message = None
        self._error_type = None
        self._timestamp = None
        self.discriminator = None

        self.result = result
        if error_message is not None:
            self.error_message = error_message
        if error_type is not None:
            self.error_type = error_type
        self.timestamp = timestamp

    @property
    def result(self):
        """Gets the result of this UpdateResult.  # noqa: E501

        Note that 'OK' just means that finAPI could successfully connect and log in to the bank server. However, it does not necessarily mean that all accounts could be updated successfully. For the latter, please refer to the 'status' field of the Account resource.  # noqa: E501

        :return: The result of this UpdateResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this UpdateResult.

        Note that 'OK' just means that finAPI could successfully connect and log in to the bank server. However, it does not necessarily mean that all accounts could be updated successfully. For the latter, please refer to the 'status' field of the Account resource.  # noqa: E501

        :param result: The result of this UpdateResult.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501
        allowed_values = ["OK", "BANK_SERVER_REJECTION", "INTERNAL_SERVER_ERROR"]  # noqa: E501
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def error_message(self):
        """Gets the error_message of this UpdateResult.  # noqa: E501

        In case the update result is not <code>OK</code>, this field may contain an error message with details about why the update failed (it is not guaranteed that a message is available though). In case the update result is <code>OK</code>, the field will always be null.  # noqa: E501

        :return: The error_message of this UpdateResult.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this UpdateResult.

        In case the update result is not <code>OK</code>, this field may contain an error message with details about why the update failed (it is not guaranteed that a message is available though). In case the update result is <code>OK</code>, the field will always be null.  # noqa: E501

        :param error_message: The error_message of this UpdateResult.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def error_type(self):
        """Gets the error_type of this UpdateResult.  # noqa: E501

        In case the update result is not <code>OK</code>, this field contains the type of the error that occurred. BUSINESS means that the bank server responded with a non-technical error message for the user. TECHNICAL means that some internal error has occurred in finAPI or at the bank server.  # noqa: E501

        :return: The error_type of this UpdateResult.  # noqa: E501
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this UpdateResult.

        In case the update result is not <code>OK</code>, this field contains the type of the error that occurred. BUSINESS means that the bank server responded with a non-technical error message for the user. TECHNICAL means that some internal error has occurred in finAPI or at the bank server.  # noqa: E501

        :param error_type: The error_type of this UpdateResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUSINESS", "TECHNICAL"]  # noqa: E501
        if error_type not in allowed_values:
            raise ValueError(
                "Invalid value for `error_type` ({0}), must be one of {1}"  # noqa: E501
                .format(error_type, allowed_values)
            )

        self._error_type = error_type

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdateResult.  # noqa: E501

        Time of the update. The value is returned in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time).  # noqa: E501

        :return: The timestamp of this UpdateResult.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdateResult.

        Time of the update. The value is returned in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time).  # noqa: E501

        :param timestamp: The timestamp of this UpdateResult.  # noqa: E501
        :type: str
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if issubclass(UpdateResult, dict):
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
        if not isinstance(other, UpdateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
