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


class NotificationRuleParams(object):
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
        'trigger_event': 'str',
        'params': 'dict(str, str)',
        'callback_handle': 'str',
        'include_details': 'bool'
    }

    attribute_map = {
        'trigger_event': 'triggerEvent',
        'params': 'params',
        'callback_handle': 'callbackHandle',
        'include_details': 'includeDetails'
    }

    def __init__(self, trigger_event=None, params=None, callback_handle=None, include_details=False):  # noqa: E501
        """NotificationRuleParams - a model defined in Swagger"""  # noqa: E501

        self._trigger_event = None
        self._params = None
        self._callback_handle = None
        self._include_details = None
        self.discriminator = None

        self.trigger_event = trigger_event
        if params is not None:
            self.params = params
        if callback_handle is not None:
            self.callback_handle = callback_handle
        if include_details is not None:
            self.include_details = include_details

    @property
    def trigger_event(self):
        """Gets the trigger_event of this NotificationRuleParams.  # noqa: E501

        Trigger event type  # noqa: E501

        :return: The trigger_event of this NotificationRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._trigger_event

    @trigger_event.setter
    def trigger_event(self, trigger_event):
        """Sets the trigger_event of this NotificationRuleParams.

        Trigger event type  # noqa: E501

        :param trigger_event: The trigger_event of this NotificationRuleParams.  # noqa: E501
        :type: str
        """
        if trigger_event is None:
            raise ValueError("Invalid value for `trigger_event`, must not be `None`")  # noqa: E501
        allowed_values = ["NEW_ACCOUNT_BALANCE", "NEW_TRANSACTIONS", "BANK_LOGIN_ERROR", "FOREIGN_MONEY_TRANSFER", "LOW_ACCOUNT_BALANCE", "HIGH_TRANSACTION_AMOUNT", "CATEGORY_CASH_FLOW", "NEW_TERMS_AND_CONDITIONS"]  # noqa: E501
        if trigger_event not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_event` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_event, allowed_values)
            )

        self._trigger_event = trigger_event

    @property
    def params(self):
        """Gets the params of this NotificationRuleParams.  # noqa: E501

        Additional parameters that are specific to the chosen trigger event type. Please refer to the documentation for details.  # noqa: E501

        :return: The params of this NotificationRuleParams.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this NotificationRuleParams.

        Additional parameters that are specific to the chosen trigger event type. Please refer to the documentation for details.  # noqa: E501

        :param params: The params of this NotificationRuleParams.  # noqa: E501
        :type: dict(str, str)
        """

        self._params = params

    @property
    def callback_handle(self):
        """Gets the callback_handle of this NotificationRuleParams.  # noqa: E501

        An arbitrary string that finAPI will include into the notifications that it sends based on this rule and that you can use to identify the notification in your application. For instance, you could include the identifier of the user that you create this rule for. Maximum allowed length of the string is 512 characters.<br/><br/>Note that for this parameter, you can pass the symbols '/', '=', '%' and '\"' in addition to the symbols that are generally allowed in finAPI (see https://finapi.zendesk.com/hc/en-us/articles/222013148). This was done to enable you to set Base64 encoded strings and JSON structures for the callback handle.  # noqa: E501

        :return: The callback_handle of this NotificationRuleParams.  # noqa: E501
        :rtype: str
        """
        return self._callback_handle

    @callback_handle.setter
    def callback_handle(self, callback_handle):
        """Sets the callback_handle of this NotificationRuleParams.

        An arbitrary string that finAPI will include into the notifications that it sends based on this rule and that you can use to identify the notification in your application. For instance, you could include the identifier of the user that you create this rule for. Maximum allowed length of the string is 512 characters.<br/><br/>Note that for this parameter, you can pass the symbols '/', '=', '%' and '\"' in addition to the symbols that are generally allowed in finAPI (see https://finapi.zendesk.com/hc/en-us/articles/222013148). This was done to enable you to set Base64 encoded strings and JSON structures for the callback handle.  # noqa: E501

        :param callback_handle: The callback_handle of this NotificationRuleParams.  # noqa: E501
        :type: str
        """
        if callback_handle is not None and not re.search(r'[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€\/=%\"]*', callback_handle):  # noqa: E501
            raise ValueError(r"Invalid value for `callback_handle`, must be a follow pattern or equal to `/[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€\/=%\"]*/`")  # noqa: E501

        self._callback_handle = callback_handle

    @property
    def include_details(self):
        """Gets the include_details of this NotificationRuleParams.  # noqa: E501

        Whether the notification messages that will be sent based on this rule should contain encrypted detailed data or not  # noqa: E501

        :return: The include_details of this NotificationRuleParams.  # noqa: E501
        :rtype: bool
        """
        return self._include_details

    @include_details.setter
    def include_details(self, include_details):
        """Sets the include_details of this NotificationRuleParams.

        Whether the notification messages that will be sent based on this rule should contain encrypted detailed data or not  # noqa: E501

        :param include_details: The include_details of this NotificationRuleParams.  # noqa: E501
        :type: bool
        """

        self._include_details = include_details

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
        if issubclass(NotificationRuleParams, dict):
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
        if not isinstance(other, NotificationRuleParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
