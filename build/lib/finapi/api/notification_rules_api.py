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


class NotificationRulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_notification_rule(self, body, **kwargs):  # noqa: E501
        """Create a new notification rule  # noqa: E501

        Create a new notification rule for a specific user. Must pass the user's access_token.<br/><br/>Setting up notification rules for a user allows your client application to get notified about changes in the user's data, e.g. when new transactions were downloaded, an account's balance has changed, or the user's banking credentials are no longer correct. Note that currently, this feature is implemented only for finAPI's automatic batch update, i.e. notification rules are only relevant when the user has activated the automatic updates (and when the automatic batch update is activated in general for your client).<br/><br/>There are different kinds of notification rules. The kind of a rule is depicted by the 'triggerEvent'. The trigger event specifies what data you have to pass when creating a rule (specifically, the contents of the 'params' field), on which events finAPI will send notifications to your client application, as well as what data is contained in those notifications. The specifics of the different trigger events are documented in the following article on our Dev Portal: <a href='https://finapi.zendesk.com/hc/en-us/articles/232324608-How-to-create-notification-rules-and-receive-notifications' target='_blank'>How to create notification rules and receive notifications</a>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_notification_rule(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationRuleParams body: Notification rule parameters (required)
        :return: NotificationRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_notification_rule_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_notification_rule_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_notification_rule_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new notification rule  # noqa: E501

        Create a new notification rule for a specific user. Must pass the user's access_token.<br/><br/>Setting up notification rules for a user allows your client application to get notified about changes in the user's data, e.g. when new transactions were downloaded, an account's balance has changed, or the user's banking credentials are no longer correct. Note that currently, this feature is implemented only for finAPI's automatic batch update, i.e. notification rules are only relevant when the user has activated the automatic updates (and when the automatic batch update is activated in general for your client).<br/><br/>There are different kinds of notification rules. The kind of a rule is depicted by the 'triggerEvent'. The trigger event specifies what data you have to pass when creating a rule (specifically, the contents of the 'params' field), on which events finAPI will send notifications to your client application, as well as what data is contained in those notifications. The specifics of the different trigger events are documented in the following article on our Dev Portal: <a href='https://finapi.zendesk.com/hc/en-us/articles/232324608-How-to-create-notification-rules-and-receive-notifications' target='_blank'>How to create notification rules and receive notifications</a>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_notification_rule_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationRuleParams body: Notification rule parameters (required)
        :return: NotificationRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_notification_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_notification_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['finapi_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/notificationRules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_all_notification_rules(self, **kwargs):  # noqa: E501
        """Delete all notification rules  # noqa: E501

        Delete all notification rules of the user that is authorized by the access_token. Must pass the user's access_token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_notification_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdentifierList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_all_notification_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_notification_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_all_notification_rules_with_http_info(self, **kwargs):  # noqa: E501
        """Delete all notification rules  # noqa: E501

        Delete all notification rules of the user that is authorized by the access_token. Must pass the user's access_token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_notification_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: IdentifierList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_notification_rules" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['finapi_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/notificationRules', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdentifierList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_notification_rule(self, id, **kwargs):  # noqa: E501
        """Delete a notification rule  # noqa: E501

        Delete a single notification rule of the user that is authorized by the access_token. Must pass the notification rule's identifier and the user's access_token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_notification_rule(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifier of the notification rule to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_notification_rule_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_notification_rule_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_notification_rule_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a notification rule  # noqa: E501

        Delete a single notification rule of the user that is authorized by the access_token. Must pass the notification rule's identifier and the user's access_token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_notification_rule_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifier of the notification rule to delete (required)
        :return: None
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
                    " to method delete_notification_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_notification_rule`")  # noqa: E501

        if 'id' in params and not re.search(r'[\\d]+', params['id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `id` when calling `delete_notification_rule`, must conform to the pattern `/[\\d]+/`")  # noqa: E501
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
            '/api/v1/notificationRules/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_and_search_all_notification_rules(self, **kwargs):  # noqa: E501
        """Get and search all notification rules  # noqa: E501

        Get notification rules of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those notification rules that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_and_search_all_notification_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] ids: A comma-separated list of notification rule identifiers. If specified, then only notification rules whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000.
        :param str trigger_event: If specified, then only notification rules with given trigger event will be regarded.
        :param bool include_details: If specified, then only notification rules that include or not include details will be regarded.
        :return: NotificationRuleList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_and_search_all_notification_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_and_search_all_notification_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_and_search_all_notification_rules_with_http_info(self, **kwargs):  # noqa: E501
        """Get and search all notification rules  # noqa: E501

        Get notification rules of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those notification rules that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_and_search_all_notification_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] ids: A comma-separated list of notification rule identifiers. If specified, then only notification rules whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000.
        :param str trigger_event: If specified, then only notification rules with given trigger event will be regarded.
        :param bool include_details: If specified, then only notification rules that include or not include details will be regarded.
        :return: NotificationRuleList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'trigger_event', 'include_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_and_search_all_notification_rules" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501
        if 'trigger_event' in params:
            query_params.append(('triggerEvent', params['trigger_event']))  # noqa: E501
        if 'include_details' in params:
            query_params.append(('includeDetails', params['include_details']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['finapi_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/notificationRules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationRuleList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_notification_rule(self, id, **kwargs):  # noqa: E501
        """Get a notification rule  # noqa: E501

        Get a single notification rule of the user that is authorized by the access_token. Must pass the notification rule's identifier and the user's access_token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_rule(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifier of requested notification rule (required)
        :return: NotificationRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_notification_rule_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notification_rule_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_notification_rule_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a notification rule  # noqa: E501

        Get a single notification rule of the user that is authorized by the access_token. Must pass the notification rule's identifier and the user's access_token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_rule_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifier of requested notification rule (required)
        :return: NotificationRule
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
                    " to method get_notification_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_notification_rule`")  # noqa: E501

        if 'id' in params and not re.search(r'[\\d]+', params['id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `id` when calling `get_notification_rule`, must conform to the pattern `/[\\d]+/`")  # noqa: E501
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
            '/api/v1/notificationRules/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
