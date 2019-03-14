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


class WebForm(object):
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
        'id': 'int',
        'token': 'str',
        'status': 'str',
        'service_response_code': 'int',
        'service_response_body': 'str'
    }

    attribute_map = {
        'id': 'id',
        'token': 'token',
        'status': 'status',
        'service_response_code': 'serviceResponseCode',
        'service_response_body': 'serviceResponseBody'
    }

    def __init__(self, id=None, token=None, status=None, service_response_code=None, service_response_body=None):  # noqa: E501
        """WebForm - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._token = None
        self._status = None
        self._service_response_code = None
        self._service_response_body = None
        self.discriminator = None

        self.id = id
        self.token = token
        self.status = status
        if service_response_code is not None:
            self.service_response_code = service_response_code
        if service_response_body is not None:
            self.service_response_body = service_response_body

    @property
    def id(self):
        """Gets the id of this WebForm.  # noqa: E501

        Web form identifier, as returned in the 451 response of the REST service call that initiated the web form flow.  # noqa: E501

        :return: The id of this WebForm.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebForm.

        Web form identifier, as returned in the 451 response of the REST service call that initiated the web form flow.  # noqa: E501

        :param id: The id of this WebForm.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def token(self):
        """Gets the token of this WebForm.  # noqa: E501

        Token for the finAPI web form page, as contained in the 451 response of the REST service call that initiated the web form flow (in the 'Location' header).  # noqa: E501

        :return: The token of this WebForm.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this WebForm.

        Token for the finAPI web form page, as contained in the 451 response of the REST service call that initiated the web form flow (in the 'Location' header).  # noqa: E501

        :param token: The token of this WebForm.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def status(self):
        """Gets the status of this WebForm.  # noqa: E501

        Status of a web form. Possible values are:<br/>&bull; NOT_YET_OPENED - the web form URL was not yet called;<br/>&bull; IN_PROGRESS - the web form has been opened but not yet submitted by the user;<br/>&bull; COMPLETED - the user has opened and submitted the web form;<br/>&bull; ABORTED - the user has opened but then aborted the web form, or the web form was aborted by the finAPI system because it has expired (this is the case when a web form is opened and then not submitted within 20 minutes)  # noqa: E501

        :return: The status of this WebForm.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebForm.

        Status of a web form. Possible values are:<br/>&bull; NOT_YET_OPENED - the web form URL was not yet called;<br/>&bull; IN_PROGRESS - the web form has been opened but not yet submitted by the user;<br/>&bull; COMPLETED - the user has opened and submitted the web form;<br/>&bull; ABORTED - the user has opened but then aborted the web form, or the web form was aborted by the finAPI system because it has expired (this is the case when a web form is opened and then not submitted within 20 minutes)  # noqa: E501

        :param status: The status of this WebForm.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["NOT_YET_OPENED", "IN_PROGRESS", "COMPLETED", "ABORTED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def service_response_code(self):
        """Gets the service_response_code of this WebForm.  # noqa: E501

        HTTP response code of the REST service call that initiated the web form flow. This field can be queried as soon as the status becomes COMPLETED or ABORTED. Note that it is still not guaranteed in this case that the field has a value, i.e. it might be null.  # noqa: E501

        :return: The service_response_code of this WebForm.  # noqa: E501
        :rtype: int
        """
        return self._service_response_code

    @service_response_code.setter
    def service_response_code(self, service_response_code):
        """Sets the service_response_code of this WebForm.

        HTTP response code of the REST service call that initiated the web form flow. This field can be queried as soon as the status becomes COMPLETED or ABORTED. Note that it is still not guaranteed in this case that the field has a value, i.e. it might be null.  # noqa: E501

        :param service_response_code: The service_response_code of this WebForm.  # noqa: E501
        :type: int
        """

        self._service_response_code = service_response_code

    @property
    def service_response_body(self):
        """Gets the service_response_body of this WebForm.  # noqa: E501

        HTTP response body of the REST service call that initiated the web form flow. This field can be queried as soon as the status becomes COMPLETED or ABORTED. Note that it is still not guaranteed in this case that the field has a value, i.e. it might be null.  # noqa: E501

        :return: The service_response_body of this WebForm.  # noqa: E501
        :rtype: str
        """
        return self._service_response_body

    @service_response_body.setter
    def service_response_body(self, service_response_body):
        """Sets the service_response_body of this WebForm.

        HTTP response body of the REST service call that initiated the web form flow. This field can be queried as soon as the status becomes COMPLETED or ABORTED. Note that it is still not guaranteed in this case that the field has a value, i.e. it might be null.  # noqa: E501

        :param service_response_body: The service_response_body of this WebForm.  # noqa: E501
        :type: str
        """

        self._service_response_body = service_response_body

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
        if issubclass(WebForm, dict):
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
        if not isinstance(other, WebForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
