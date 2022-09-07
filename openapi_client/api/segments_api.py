"""
    Klaviyo API (Beta)

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2022-09-07.pre
    Contact: developers@klaviyo.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.get_catalog_items4_xx_response import GetCatalogItems4XXResponse
from openapi_client.model.segment_partial_update_query import SegmentPartialUpdateQuery


class SegmentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_segment_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/segments/{id}/',
                'operation_id': 'get_segment',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'fields_segment',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'fields_segment',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('fields_segment',): {

                        "NAME": "name",
                        "CREATED": "created",
                        "UPDATED": "updated"
                    },
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'fields_segment':
                        ([str],),
                },
                'attribute_map': {
                    'id': 'id',
                    'fields_segment': 'fields[segment]',
                },
                'location_map': {
                    'id': 'path',
                    'fields_segment': 'query',
                },
                'collection_format_map': {
                    'fields_segment': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_segment_profiles_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/segments/{segment_id}/profiles/',
                'operation_id': 'get_segment_profiles',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'segment_id',
                    'filter',
                    'page_cursor',
                ],
                'required': [
                    'segment_id',
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
                    'segment_id':
                        (str,),
                    'filter':
                        (str,),
                    'page_cursor':
                        (str,),
                },
                'attribute_map': {
                    'segment_id': 'segment_id',
                    'filter': 'filter',
                    'page_cursor': 'page[cursor]',
                },
                'location_map': {
                    'segment_id': 'path',
                    'filter': 'query',
                    'page_cursor': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_segment_relationships_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/segments/{id}/relationships/{related_resource}/',
                'operation_id': 'get_segment_relationships',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'related_resource',
                    'page_cursor',
                ],
                'required': [
                    'id',
                    'related_resource',
                ],
                'nullable': [
                ],
                'enum': [
                    'related_resource',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('related_resource',): {

                        "PROFILES": "profiles"
                    },
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'related_resource':
                        (str,),
                    'page_cursor':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'related_resource': 'related_resource',
                    'page_cursor': 'page[cursor]',
                },
                'location_map': {
                    'id': 'path',
                    'related_resource': 'path',
                    'page_cursor': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_segments_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/segments/',
                'operation_id': 'get_segments',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'fields_segment',
                    'filter',
                    'page_cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'fields_segment',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('fields_segment',): {

                        "NAME": "name",
                        "CREATED": "created",
                        "UPDATED": "updated"
                    },
                },
                'openapi_types': {
                    'fields_segment':
                        ([str],),
                    'filter':
                        (str,),
                    'page_cursor':
                        (str,),
                },
                'attribute_map': {
                    'fields_segment': 'fields[segment]',
                    'filter': 'filter',
                    'page_cursor': 'page[cursor]',
                },
                'location_map': {
                    'fields_segment': 'query',
                    'filter': 'query',
                    'page_cursor': 'query',
                },
                'collection_format_map': {
                    'fields_segment': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_segment_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/segments/{id}/',
                'operation_id': 'update_segment',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'segment_partial_update_query',
                ],
                'required': [
                    'id',
                    'segment_partial_update_query',
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
                    'id':
                        (str,),
                    'segment_partial_update_query':
                        (SegmentPartialUpdateQuery,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'segment_partial_update_query': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_segment(
        self,
        id,
        **kwargs
    ):
        """Get Segment  # noqa: E501

        Get a single segment by ID<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_segment(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): 

        Keyword Args:
            fields_segment ([str]): For more information please visit https://developers.klaviyo.com/en/v2022-09-07.pre/reference/api-overview#filtering. [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['id'] = \
            id
        return self.get_segment_endpoint.call_with_http_info(**kwargs)

    def get_segment_profiles(
        self,
        segment_id,
        **kwargs
    ):
        """Get Segment Profiles  # noqa: E501

        Returns a list of all profiles inside a given segment, that can optionally be filtered by email, phone number, and push token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_segment_profiles(segment_id, async_req=True)
        >>> result = thread.get()

        Args:
            segment_id (str): 

        Keyword Args:
            filter (str): For more information please visit https://developers.klaviyo.com/en/v2022-09-07.pre/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`email`: `any`<br>`phone_number`: `any`<br>`push_token`: `any`<br>`_kx`: `equals`. [optional]
            page_cursor (str): For more information please visit https://developers.klaviyo.com/en/v2022-09-07.pre/reference/api-overview#pagination. [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['segment_id'] = \
            segment_id
        return self.get_segment_profiles_endpoint.call_with_http_info(**kwargs)

    def get_segment_relationships(
        self,
        id,
        related_resource="profiles",
        **kwargs
    ):
        """Get Segment Relationships  # noqa: E501

        Returns a list of profile membership relationships for a given segment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_segment_relationships(id, related_resource="profiles", async_req=True)
        >>> result = thread.get()

        Args:
            id (str): 
            related_resource (str): . defaults to "profiles", must be one of ["profiles"]

        Keyword Args:
            page_cursor (str): For more information please visit https://developers.klaviyo.com/en/v2022-09-07.pre/reference/api-overview#pagination. [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['id'] = \
            id
        kwargs['related_resource'] = \
            related_resource
        return self.get_segment_relationships_endpoint.call_with_http_info(**kwargs)

    def get_segments(
        self,
        **kwargs
    ):
        """Get Segments  # noqa: E501

        Get some or all segments.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_segments(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            fields_segment ([str]): For more information please visit https://developers.klaviyo.com/en/v2022-09-07.pre/reference/api-overview#filtering. [optional]
            filter (str): For more information please visit https://developers.klaviyo.com/en/v2022-09-07.pre/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`name`: `any`, `equals`<br>`created`: `greater-than`<br>`updated`: `greater-than`. [optional]
            page_cursor (str): For more information please visit https://developers.klaviyo.com/en/v2022-09-07.pre/reference/api-overview#pagination. [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_segments_endpoint.call_with_http_info(**kwargs)

    def update_segment(
        self,
        id,
        segment_partial_update_query,
        **kwargs
    ):
        """Update Segment  # noqa: E501

        Update segment name or other attributes by ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_segment(id, segment_partial_update_query, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): 
            segment_partial_update_query (SegmentPartialUpdateQuery):

        Keyword Args:
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['id'] = \
            id
        kwargs['segment_partial_update_query'] = \
            segment_partial_update_query
        return self.update_segment_endpoint.call_with_http_info(**kwargs)

