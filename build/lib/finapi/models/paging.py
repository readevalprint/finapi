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


class Paging(object):
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
        'page': 'int',
        'per_page': 'int',
        'page_count': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'page': 'page',
        'per_page': 'perPage',
        'page_count': 'pageCount',
        'total_count': 'totalCount'
    }

    def __init__(self, page=None, per_page=None, page_count=None, total_count=None):  # noqa: E501
        """Paging - a model defined in Swagger"""  # noqa: E501

        self._page = None
        self._per_page = None
        self._page_count = None
        self._total_count = None
        self.discriminator = None

        self.page = page
        self.per_page = per_page
        self.page_count = page_count
        self.total_count = total_count

    @property
    def page(self):
        """Gets the page of this Paging.  # noqa: E501

        Current page number  # noqa: E501

        :return: The page of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this Paging.

        Current page number  # noqa: E501

        :param page: The page of this Paging.  # noqa: E501
        :type: int
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this Paging.  # noqa: E501

        Current page size (number of entries in this page)  # noqa: E501

        :return: The per_page of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this Paging.

        Current page size (number of entries in this page)  # noqa: E501

        :param per_page: The per_page of this Paging.  # noqa: E501
        :type: int
        """
        if per_page is None:
            raise ValueError("Invalid value for `per_page`, must not be `None`")  # noqa: E501

        self._per_page = per_page

    @property
    def page_count(self):
        """Gets the page_count of this Paging.  # noqa: E501

        Total number of pages  # noqa: E501

        :return: The page_count of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this Paging.

        Total number of pages  # noqa: E501

        :param page_count: The page_count of this Paging.  # noqa: E501
        :type: int
        """
        if page_count is None:
            raise ValueError("Invalid value for `page_count`, must not be `None`")  # noqa: E501

        self._page_count = page_count

    @property
    def total_count(self):
        """Gets the total_count of this Paging.  # noqa: E501

        Total number of entries across all pages  # noqa: E501

        :return: The total_count of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this Paging.

        Total number of entries across all pages  # noqa: E501

        :param total_count: The total_count of this Paging.  # noqa: E501
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

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
        if issubclass(Paging, dict):
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
        if not isinstance(other, Paging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
