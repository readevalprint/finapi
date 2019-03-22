# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.64.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from finapi.api_client import ApiClient


class SecuritiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_and_search_all_securities(self, **kwargs):  # noqa: E501
        """Get and search all securities  # noqa: E501

        Get securities of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those securities that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.<p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_and_search_all_securities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] ids: A comma-separated list of security identifiers. If specified, then only securities whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000.
        :param str search: If specified, then only those securities will be contained in the result whose 'name', 'isin' or 'wkn' contains the given search string (the matching works case-insensitive). If no securities contain the search string in any of these fields, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the searched fields in order for a security to get included into the result.
        :param list[int] account_ids: Comma-separated list of identifiers of accounts
        :param int page: Result page that you want to retrieve.
        :param int per_page: Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes.
        :param list[str] order: Determines the order of the results. You can order the results by next fields: 'id', 'name', 'isin', 'wkn', 'quote', 'quantityNominal', 'marketValue' and 'entryQuote'. The default order for all services is 'id,asc'. You can also order by multiple properties. In that case the order of the parameters passed is important. The general format is: 'property[,asc|desc]', with 'asc' being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC). 
        :return: PageableSecurityList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_and_search_all_securities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_and_search_all_securities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_and_search_all_securities_with_http_info(self, **kwargs):  # noqa: E501
        """Get and search all securities  # noqa: E501

        Get securities of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those securities that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.<p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_and_search_all_securities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] ids: A comma-separated list of security identifiers. If specified, then only securities whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000.
        :param str search: If specified, then only those securities will be contained in the result whose 'name', 'isin' or 'wkn' contains the given search string (the matching works case-insensitive). If no securities contain the search string in any of these fields, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the searched fields in order for a security to get included into the result.
        :param list[int] account_ids: Comma-separated list of identifiers of accounts
        :param int page: Result page that you want to retrieve.
        :param int per_page: Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes.
        :param list[str] order: Determines the order of the results. You can order the results by next fields: 'id', 'name', 'isin', 'wkn', 'quote', 'quantityNominal', 'marketValue' and 'entryQuote'. The default order for all services is 'id,asc'. You can also order by multiple properties. In that case the order of the parameters passed is important. The general format is: 'property[,asc|desc]', with 'asc' being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC). 
        :return: PageableSecurityList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'search', 'account_ids', 'page', 'per_page', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_and_search_all_securities" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_and_search_all_securities`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'per_page' in params and params['per_page'] > 500:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `get_and_search_all_securities`, must be a value less than or equal to `500`")  # noqa: E501
        if 'per_page' in params and params['per_page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `get_and_search_all_securities`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'account_ids' in params:
            query_params.append(('accountIds', params['account_ids']))  # noqa: E501
            collection_formats['accountIds'] = 'multi'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('perPage', params['per_page']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
            collection_formats['order'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['finapi_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/securities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageableSecurityList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_multiple_securities(self, ids, **kwargs):  # noqa: E501
        """Get multiple securities  # noqa: E501

        Get a list of multiple securities of the user that is authorized by the access_token. Must pass the securities' identifiers and the user's access_token. Securities whose identifiers do not exist or do not relate to the authorized user will not be contained in the result (If this applies to all of the given identifiers, then the result will be an empty list). <p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p><p>WARNING: This service is deprecated and will be removed at some point. If you want to get multiple securities, please instead use the service 'Get and search all securities' and pass a comma-separated list of identifiers as a parameter 'ids'.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_multiple_securities(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] ids: Comma-separated list of identifiers of requested securities (required)
        :return: SecurityList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_multiple_securities_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_multiple_securities_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def get_multiple_securities_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Get multiple securities  # noqa: E501

        Get a list of multiple securities of the user that is authorized by the access_token. Must pass the securities' identifiers and the user's access_token. Securities whose identifiers do not exist or do not relate to the authorized user will not be contained in the result (If this applies to all of the given identifiers, then the result will be an empty list). <p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p><p>WARNING: This service is deprecated and will be removed at some point. If you want to get multiple securities, please instead use the service 'Get and search all securities' and pass a comma-separated list of identifiers as a parameter 'ids'.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_multiple_securities_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] ids: Comma-separated list of identifiers of requested securities (required)
        :return: SecurityList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_multiple_securities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `get_multiple_securities`")  # noqa: E501

        if 'ids' in params and not re.search(r'[\d]+,[\d,]+', params['ids']):  # noqa: E501
            raise ValueError("Invalid value for parameter `ids` when calling `get_multiple_securities`, must conform to the pattern `/[\d]+,[\d,]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'ids' in params:
            path_params['ids'] = params['ids']  # noqa: E501
            collection_formats['ids'] = 'csv'  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['finapi_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/securities/{ids}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SecurityList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_security(self, id, **kwargs):  # noqa: E501
        """Get a security  # noqa: E501

        Get a single security for a specific user. Must pass the security's identifier and the user's access_token. <p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Security identifier (required)
        :return: Security
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_security_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_security_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_security_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a security  # noqa: E501

        Get a single security for a specific user. Must pass the security's identifier and the user's access_token. <p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_security_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Security identifier (required)
        :return: Security
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_security" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_security`")  # noqa: E501

        if 'id' in params and not re.search(r'[\d]+', params['id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `id` when calling `get_security`, must conform to the pattern `/[\d]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['finapi_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/securities/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Security',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
