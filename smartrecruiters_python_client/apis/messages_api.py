# coding: utf-8

"""
    Unofficial python library for the SmartRecruiters API

    The SmartRecruiters API provides a platform to integrate services or applications, build apps and create fully customizable career sites. It exposes SmartRecruiters functionality and allows to connect and build software enhancing it.

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MessagesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def messages_shares_create(self, **kwargs):
        """
        Shares new messages on Hireloop with Users, Hiring Teams or Everyone and sends emails.
        How does it work: * In **content** field, provide a text to be shared. No HTML tags are allowed. * @-mention users to send them an email   * In **content** field use **@[USER:id]** to mention a User, e.g. @[USER:324132421] * Email responses are added as comments to your update * \\#-tag candidates to link updates to their profiles   * In **content** field use **#[CANDIDATE:id]** to tag a candidate, e.g. #[CANDIDATE:9847954623] * Use **shareWith** to share a feed update with individuals, hiring teams or everyone   * In **users** field, provide an array of User IDs with which you want to share, e.g. \"users\": [\"12343542356\",\"12343542357\"].   * In **hiringTeamOf** field, provide an array of Job IDs, this will share message with a full hiring team of those jobs, e.g. \"hiringTeamOf\": [\"123423432322\",\"123423432324\"].   * **everyone** flag allows sharing with everyone in a company. If not provided, defaults to **false**.   * **openNote** flag allows sharing with everyone in a company that has access to the candidate. If not provided, defaults to **false** 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_shares_create(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Message message: Message to post
        :return: MessageDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.messages_shares_create_with_http_info(**kwargs)
        else:
            (data) = self.messages_shares_create_with_http_info(**kwargs)
            return data

    def messages_shares_create_with_http_info(self, **kwargs):
        """
        Shares new messages on Hireloop with Users, Hiring Teams or Everyone and sends emails.
        How does it work: * In **content** field, provide a text to be shared. No HTML tags are allowed. * @-mention users to send them an email   * In **content** field use **@[USER:id]** to mention a User, e.g. @[USER:324132421] * Email responses are added as comments to your update * \\#-tag candidates to link updates to their profiles   * In **content** field use **#[CANDIDATE:id]** to tag a candidate, e.g. #[CANDIDATE:9847954623] * Use **shareWith** to share a feed update with individuals, hiring teams or everyone   * In **users** field, provide an array of User IDs with which you want to share, e.g. \"users\": [\"12343542356\",\"12343542357\"].   * In **hiringTeamOf** field, provide an array of Job IDs, this will share message with a full hiring team of those jobs, e.g. \"hiringTeamOf\": [\"123423432322\",\"123423432324\"].   * **everyone** flag allows sharing with everyone in a company. If not provided, defaults to **false**.   * **openNote** flag allows sharing with everyone in a company that has access to the candidate. If not provided, defaults to **false** 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_shares_create_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Message message: Message to post
        :return: MessageDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method messages_shares_create" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/messages/shares'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'message' in params:
            body_params = params['message']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='MessageDetails',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def messages_shares_delete(self, id, **kwargs):
        """
        Delete a message
        Delete a message with a given id. Deleted message is no longer visible on Hireloop.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_shares_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: identifier of a message (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.messages_shares_delete_with_http_info(id, **kwargs)
        else:
            (data) = self.messages_shares_delete_with_http_info(id, **kwargs)
            return data

    def messages_shares_delete_with_http_info(self, id, **kwargs):
        """
        Delete a message
        Delete a message with a given id. Deleted message is no longer visible on Hireloop.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_shares_delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: identifier of a message (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method messages_shares_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `messages_shares_delete`")


        collection_formats = {}

        resource_path = '/messages/shares/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
