# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from datetime import datetime

from pydantic import StrictStr, field_validator

from typing import Optional

from asana_asyncio.models.get_audit_log_events200_response import GetAuditLogEvents200Response

from asana_asyncio.api_client import ApiClient
from asana_asyncio.api_response import ApiResponse
from asana_asyncio.rest import RESTResponseType


class AuditLogAPIApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def get_audit_log_events(
        self,
        workspace_gid: Annotated[StrictStr, Field(description="Globally unique identifier for the workspace or organization.")],
        start_at: Annotated[Optional[datetime], Field(description="Filter to events created after this time (inclusive).")] = None,
        end_at: Annotated[Optional[datetime], Field(description="Filter to events created before this time (exclusive).")] = None,
        event_type: Annotated[Optional[StrictStr], Field(description="Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values.")] = None,
        actor_type: Annotated[Optional[StrictStr], Field(description="Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.")] = None,
        actor_gid: Annotated[Optional[StrictStr], Field(description="Filter to events triggered by the actor with this ID.")] = None,
        resource_gid: Annotated[Optional[StrictStr], Field(description="Filter to events with this resource ID.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Results per page. The number of objects to return per page. The value must be between 1 and 100.")] = None,
        offset: Annotated[Optional[StrictStr], Field(description="Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetAuditLogEvents200Response:
        """Get audit log events

        Retrieve the audit log events that have been captured in your domain.  This endpoint will return a list of [AuditLogEvent](/reference/audit-log-api) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.  There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/reference/audit-log-api) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.  The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.  *Note: If the filters you provided match events in your domain and `next_page` is present in the response, we will continue to send `next_page` on subsequent requests even when there are no more events that match the filters. This was put in place so that you can implement an audit log stream that will return future events that match these filters. If you are not interested in future events that match the filters you have defined, you can rely on checking empty `data` response for the end of current events that match your filters.*  When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/reference/audit-log-api) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.

        :param workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :type workspace_gid: str
        :param start_at: Filter to events created after this time (inclusive).
        :type start_at: datetime
        :param end_at: Filter to events created before this time (exclusive).
        :type end_at: datetime
        :param event_type: Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values.
        :type event_type: str
        :param actor_type: Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.
        :type actor_type: str
        :param actor_gid: Filter to events triggered by the actor with this ID.
        :type actor_gid: str
        :param resource_gid: Filter to events with this resource ID.
        :type resource_gid: str
        :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :type limit: int
        :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :type offset: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_log_events_serialize(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetAuditLogEvents200Response",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def get_audit_log_events_with_http_info(
        self,
        workspace_gid: Annotated[StrictStr, Field(description="Globally unique identifier for the workspace or organization.")],
        start_at: Annotated[Optional[datetime], Field(description="Filter to events created after this time (inclusive).")] = None,
        end_at: Annotated[Optional[datetime], Field(description="Filter to events created before this time (exclusive).")] = None,
        event_type: Annotated[Optional[StrictStr], Field(description="Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values.")] = None,
        actor_type: Annotated[Optional[StrictStr], Field(description="Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.")] = None,
        actor_gid: Annotated[Optional[StrictStr], Field(description="Filter to events triggered by the actor with this ID.")] = None,
        resource_gid: Annotated[Optional[StrictStr], Field(description="Filter to events with this resource ID.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Results per page. The number of objects to return per page. The value must be between 1 and 100.")] = None,
        offset: Annotated[Optional[StrictStr], Field(description="Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GetAuditLogEvents200Response]:
        """Get audit log events

        Retrieve the audit log events that have been captured in your domain.  This endpoint will return a list of [AuditLogEvent](/reference/audit-log-api) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.  There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/reference/audit-log-api) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.  The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.  *Note: If the filters you provided match events in your domain and `next_page` is present in the response, we will continue to send `next_page` on subsequent requests even when there are no more events that match the filters. This was put in place so that you can implement an audit log stream that will return future events that match these filters. If you are not interested in future events that match the filters you have defined, you can rely on checking empty `data` response for the end of current events that match your filters.*  When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/reference/audit-log-api) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.

        :param workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :type workspace_gid: str
        :param start_at: Filter to events created after this time (inclusive).
        :type start_at: datetime
        :param end_at: Filter to events created before this time (exclusive).
        :type end_at: datetime
        :param event_type: Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values.
        :type event_type: str
        :param actor_type: Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.
        :type actor_type: str
        :param actor_gid: Filter to events triggered by the actor with this ID.
        :type actor_gid: str
        :param resource_gid: Filter to events with this resource ID.
        :type resource_gid: str
        :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :type limit: int
        :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :type offset: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_log_events_serialize(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetAuditLogEvents200Response",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def get_audit_log_events_without_preload_content(
        self,
        workspace_gid: Annotated[StrictStr, Field(description="Globally unique identifier for the workspace or organization.")],
        start_at: Annotated[Optional[datetime], Field(description="Filter to events created after this time (inclusive).")] = None,
        end_at: Annotated[Optional[datetime], Field(description="Filter to events created before this time (exclusive).")] = None,
        event_type: Annotated[Optional[StrictStr], Field(description="Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values.")] = None,
        actor_type: Annotated[Optional[StrictStr], Field(description="Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.")] = None,
        actor_gid: Annotated[Optional[StrictStr], Field(description="Filter to events triggered by the actor with this ID.")] = None,
        resource_gid: Annotated[Optional[StrictStr], Field(description="Filter to events with this resource ID.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Results per page. The number of objects to return per page. The value must be between 1 and 100.")] = None,
        offset: Annotated[Optional[StrictStr], Field(description="Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get audit log events

        Retrieve the audit log events that have been captured in your domain.  This endpoint will return a list of [AuditLogEvent](/reference/audit-log-api) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.  There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/reference/audit-log-api) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.  The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.  *Note: If the filters you provided match events in your domain and `next_page` is present in the response, we will continue to send `next_page` on subsequent requests even when there are no more events that match the filters. This was put in place so that you can implement an audit log stream that will return future events that match these filters. If you are not interested in future events that match the filters you have defined, you can rely on checking empty `data` response for the end of current events that match your filters.*  When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/reference/audit-log-api) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.

        :param workspace_gid: Globally unique identifier for the workspace or organization. (required)
        :type workspace_gid: str
        :param start_at: Filter to events created after this time (inclusive).
        :type start_at: datetime
        :param end_at: Filter to events created before this time (exclusive).
        :type end_at: datetime
        :param event_type: Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values.
        :type event_type: str
        :param actor_type: Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.
        :type actor_type: str
        :param actor_gid: Filter to events triggered by the actor with this ID.
        :type actor_gid: str
        :param resource_gid: Filter to events with this resource ID.
        :type resource_gid: str
        :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :type limit: int
        :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :type offset: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_log_events_serialize(
            workspace_gid=workspace_gid,
            start_at=start_at,
            end_at=end_at,
            event_type=event_type,
            actor_type=actor_type,
            actor_gid=actor_gid,
            resource_gid=resource_gid,
            limit=limit,
            offset=offset,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetAuditLogEvents200Response",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_audit_log_events_serialize(
        self,
        workspace_gid,
        start_at,
        end_at,
        event_type,
        actor_type,
        actor_gid,
        resource_gid,
        limit,
        offset,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if workspace_gid is not None:
            _path_params['workspace_gid'] = workspace_gid
        # process the query parameters
        if start_at is not None:
            if isinstance(start_at, datetime):
                _query_params.append(
                    (
                        'start_at',
                        start_at.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('start_at', start_at))
            
        if end_at is not None:
            if isinstance(end_at, datetime):
                _query_params.append(
                    (
                        'end_at',
                        end_at.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('end_at', end_at))
            
        if event_type is not None:
            
            _query_params.append(('event_type', event_type))
            
        if actor_type is not None:
            
            _query_params.append(('actor_type', actor_type))
            
        if actor_gid is not None:
            
            _query_params.append(('actor_gid', actor_gid))
            
        if resource_gid is not None:
            
            _query_params.append(('resource_gid', resource_gid))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'personalAccessToken', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/workspaces/{workspace_gid}/audit_log_events',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


