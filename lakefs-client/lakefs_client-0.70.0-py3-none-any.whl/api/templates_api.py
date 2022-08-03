"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lakefs_client.api_client import ApiClient, Endpoint as _Endpoint
from lakefs_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lakefs_client.model.error import Error


class TemplatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.expand_template_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth'
                ],
                'endpoint_path': '/templates/{template_location}',
                'operation_id': 'expand_template',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'template_location',
                    'params',
                ],
                'required': [
                    'template_location',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'template_location':
                        (str,),
                    'params':
                        ({str: (str,)},),
                },
                'attribute_map': {
                    'template_location': 'template_location',
                    'params': 'params',
                },
                'location_map': {
                    'template_location': 'path',
                    'params': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def expand_template(
        self,
        template_location,
        **kwargs
    ):
        """expand_template  # noqa: E501

        fetch and expand template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.expand_template(template_location, async_req=True)
        >>> result = thread.get()

        Args:
            template_location (str): URL of the template; must be relative (to a URL configured on the server).

        Keyword Args:
            params ({str: (str,)}): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['template_location'] = \
            template_location
        return self.expand_template_endpoint.call_with_http_info(**kwargs)

