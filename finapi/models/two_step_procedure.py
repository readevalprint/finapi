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


class TwoStepProcedure(object):
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
        'procedure_id': 'str',
        'procedure_name': 'str',
        'procedure_challenge_type': 'str',
        'implicit_execute': 'bool'
    }

    attribute_map = {
        'procedure_id': 'procedureId',
        'procedure_name': 'procedureName',
        'procedure_challenge_type': 'procedureChallengeType',
        'implicit_execute': 'implicitExecute'
    }

    def __init__(self, procedure_id=None, procedure_name=None, procedure_challenge_type=None, implicit_execute=None):  # noqa: E501
        """TwoStepProcedure - a model defined in Swagger"""  # noqa: E501

        self._procedure_id = None
        self._procedure_name = None
        self._procedure_challenge_type = None
        self._implicit_execute = None
        self.discriminator = None

        self.procedure_id = procedure_id
        self.procedure_name = procedure_name
        if procedure_challenge_type is not None:
            self.procedure_challenge_type = procedure_challenge_type
        self.implicit_execute = implicit_execute

    @property
    def procedure_id(self):
        """Gets the procedure_id of this TwoStepProcedure.  # noqa: E501

        Bank-given ID of the procedure  # noqa: E501

        :return: The procedure_id of this TwoStepProcedure.  # noqa: E501
        :rtype: str
        """
        return self._procedure_id

    @procedure_id.setter
    def procedure_id(self, procedure_id):
        """Sets the procedure_id of this TwoStepProcedure.

        Bank-given ID of the procedure  # noqa: E501

        :param procedure_id: The procedure_id of this TwoStepProcedure.  # noqa: E501
        :type: str
        """
        if procedure_id is None:
            raise ValueError("Invalid value for `procedure_id`, must not be `None`")  # noqa: E501

        self._procedure_id = procedure_id

    @property
    def procedure_name(self):
        """Gets the procedure_name of this TwoStepProcedure.  # noqa: E501

        Bank-given name of the procedure  # noqa: E501

        :return: The procedure_name of this TwoStepProcedure.  # noqa: E501
        :rtype: str
        """
        return self._procedure_name

    @procedure_name.setter
    def procedure_name(self, procedure_name):
        """Sets the procedure_name of this TwoStepProcedure.

        Bank-given name of the procedure  # noqa: E501

        :param procedure_name: The procedure_name of this TwoStepProcedure.  # noqa: E501
        :type: str
        """
        if procedure_name is None:
            raise ValueError("Invalid value for `procedure_name`, must not be `None`")  # noqa: E501

        self._procedure_name = procedure_name

    @property
    def procedure_challenge_type(self):
        """Gets the procedure_challenge_type of this TwoStepProcedure.  # noqa: E501

        The challenge type of the procedure. Possible values are:<br/><br/>&bull; <code>TEXT</code> - the challenge will be a text that contains instructions for the user on how to retrieve the TAN.<br/>&bull; <code>PHOTO</code> - the challenge will contain a BASE-64 string depicting a photo (or any kind of QR-code-like data) that must be shown to the user.<br/>&bull; <code>FLICKER_CODE</code> - the challenge will contain a BASE-64 string depicting a flicker code animation that must be shown to the user.<br/><br/>Note that this challenge type information does not originate from the bank server, but is determined by finAPI internally. There is no guarantee that the determined challenge type is correct. Note also that this field may not be set, meaning that finAPI could not determine the challenge type of the procedure.<br/><br/>For further information on how to deal with the challenges, please see <a href='https://finapi.zendesk.com/hc/en-us/articles/219117247-SEPA-Money-Transfer'>this article</a> on our Dev Portal.  # noqa: E501

        :return: The procedure_challenge_type of this TwoStepProcedure.  # noqa: E501
        :rtype: str
        """
        return self._procedure_challenge_type

    @procedure_challenge_type.setter
    def procedure_challenge_type(self, procedure_challenge_type):
        """Sets the procedure_challenge_type of this TwoStepProcedure.

        The challenge type of the procedure. Possible values are:<br/><br/>&bull; <code>TEXT</code> - the challenge will be a text that contains instructions for the user on how to retrieve the TAN.<br/>&bull; <code>PHOTO</code> - the challenge will contain a BASE-64 string depicting a photo (or any kind of QR-code-like data) that must be shown to the user.<br/>&bull; <code>FLICKER_CODE</code> - the challenge will contain a BASE-64 string depicting a flicker code animation that must be shown to the user.<br/><br/>Note that this challenge type information does not originate from the bank server, but is determined by finAPI internally. There is no guarantee that the determined challenge type is correct. Note also that this field may not be set, meaning that finAPI could not determine the challenge type of the procedure.<br/><br/>For further information on how to deal with the challenges, please see <a href='https://finapi.zendesk.com/hc/en-us/articles/219117247-SEPA-Money-Transfer'>this article</a> on our Dev Portal.  # noqa: E501

        :param procedure_challenge_type: The procedure_challenge_type of this TwoStepProcedure.  # noqa: E501
        :type: str
        """

        self._procedure_challenge_type = procedure_challenge_type

    @property
    def implicit_execute(self):
        """Gets the implicit_execute of this TwoStepProcedure.  # noqa: E501

        If 'true', then requesting a SEPA order with this procedure will implicitly trigger the execution of the order. For example, if you do a money transfer with this procedure, then calling the /requestSepaMoneyTransfer service will immediately execute the order (a call to /executeSepaMoneyTransfer will not be necessary). On the other hand, if this flag is 'false', then doing a money transfer with this procedure will require you to first call /requestSepaMoneyTransfer, and then call /executeSepaMoneyTransfer.  # noqa: E501

        :return: The implicit_execute of this TwoStepProcedure.  # noqa: E501
        :rtype: bool
        """
        return self._implicit_execute

    @implicit_execute.setter
    def implicit_execute(self, implicit_execute):
        """Sets the implicit_execute of this TwoStepProcedure.

        If 'true', then requesting a SEPA order with this procedure will implicitly trigger the execution of the order. For example, if you do a money transfer with this procedure, then calling the /requestSepaMoneyTransfer service will immediately execute the order (a call to /executeSepaMoneyTransfer will not be necessary). On the other hand, if this flag is 'false', then doing a money transfer with this procedure will require you to first call /requestSepaMoneyTransfer, and then call /executeSepaMoneyTransfer.  # noqa: E501

        :param implicit_execute: The implicit_execute of this TwoStepProcedure.  # noqa: E501
        :type: bool
        """
        if implicit_execute is None:
            raise ValueError("Invalid value for `implicit_execute`, must not be `None`")  # noqa: E501

        self._implicit_execute = implicit_execute

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
        if issubclass(TwoStepProcedure, dict):
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
        if not isinstance(other, TwoStepProcedure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
