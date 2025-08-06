# asana_asyncio.WebhooksApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Establish a webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhook_gid} | Delete a webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhook_gid} | Get a webhook
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /webhooks | Get multiple webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /webhooks/{webhook_gid} | Update a webhook


# **create_webhook**
> CreateWebhook201Response create_webhook(create_webhook_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Establish a webhook

<b>Required scope: </b><code>webhooks:write</code>

Establishing a webhook is a two-part process. First, a simple HTTP POST
request initiates the creation similar to creating any other resource.

Next, in the middle of this request comes the confirmation handshake.
When a webhook is created, we will send a test POST to the target with an
`X-Hook-Secret` header. The target must respond with a `200 OK` or `204
No Content` and a matching `X-Hook-Secret` header to confirm that this
webhook subscription is indeed expected. We strongly recommend storing
this secret to be used to verify future webhook event signatures.

The POST request to create the webhook will then return with the status
of the request. If you do not acknowledge the webhook’s confirmation
handshake it will fail to setup, and you will receive an error in
response to your attempt to create it. This means you need to be able to
receive and complete the webhook *while* the POST request is in-flight
(in other words, have a server that can handle requests asynchronously).

Invalid hostnames like localhost will receive a 403 Forbidden status code.

```
# Request
curl -H "Authorization: Bearer <personal_access_token>" \
-X POST https://app.asana.com/api/1.0/webhooks \
-d "resource=8675309" \
-d "target=https://example.com/receive-webhook/7654"
```

```
# Handshake sent to https://example.com/
POST /receive-webhook/7654
X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81
```

```
# Handshake response sent by example.com
HTTP/1.1 200
X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81
```

```
# Response
HTTP/1.1 201
{
  "data": {
    "gid": "43214",
    "resource": {
      "gid": "8675309",
      "name": "Bugs"
    },
    "target": "https://example.com/receive-webhook/7654",
    "active": false,
    "last_success_at": null,
    "last_failure_at": null,
    "last_failure_content": null
  },
  "X-Hook-Secret": "b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81"
}
```

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_webhook201_response import CreateWebhook201Response
from asana_asyncio.models.create_webhook_request import CreateWebhookRequest
from asana_asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.asana.com/api/1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = asana_asyncio.Configuration(
    host = "https://app.asana.com/api/1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.WebhooksApi(api_client)
    create_webhook_request = asana_asyncio.CreateWebhookRequest() # CreateWebhookRequest | The webhook workspace and target.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"active\",\"created_at\",\"delivery_retry_count\",\"failure_deletion_timestamp\",\"filters\",\"filters.action\",\"filters.fields\",\"filters.resource_subtype\",\"last_failure_at\",\"last_failure_content\",\"last_success_at\",\"next_attempt_after\",\"resource\",\"resource.name\",\"target\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Establish a webhook
        api_response = await api_instance.create_webhook(create_webhook_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of WebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)| The webhook workspace and target. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateWebhook201Response**](CreateWebhook201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the requested webhook. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> DeleteAllocation200Response delete_webhook(webhook_gid, opt_pretty=opt_pretty)

Delete a webhook

<b>Required scope: </b><code>webhooks:delete</code>

This method *permanently* removes a webhook. Note that it may be possible to receive a request that was already in flight after deleting the webhook, but no further requests will be issued.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.delete_allocation200_response import DeleteAllocation200Response
from asana_asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.asana.com/api/1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = asana_asyncio.Configuration(
    host = "https://app.asana.com/api/1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.WebhooksApi(api_client)
    webhook_gid = '12345' # str | Globally unique identifier for the webhook.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a webhook
        api_response = await api_instance.delete_webhook(webhook_gid, opt_pretty=opt_pretty)
        print("The response of WebhooksApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_gid** | **str**| Globally unique identifier for the webhook. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 

### Return type

[**DeleteAllocation200Response**](DeleteAllocation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested webhook. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> GetWebhook200Response get_webhook(webhook_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a webhook

<b>Required scope: </b><code>webhooks:read</code>

Returns the full record for the given webhook.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_webhook200_response import GetWebhook200Response
from asana_asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.asana.com/api/1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = asana_asyncio.Configuration(
    host = "https://app.asana.com/api/1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.WebhooksApi(api_client)
    webhook_gid = '12345' # str | Globally unique identifier for the webhook.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"active\",\"created_at\",\"delivery_retry_count\",\"failure_deletion_timestamp\",\"filters\",\"filters.action\",\"filters.fields\",\"filters.resource_subtype\",\"last_failure_at\",\"last_failure_content\",\"last_success_at\",\"next_attempt_after\",\"resource\",\"resource.name\",\"target\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a webhook
        api_response = await api_instance.get_webhook(webhook_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of WebhooksApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_gid** | **str**| Globally unique identifier for the webhook. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetWebhook200Response**](GetWebhook200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested webhook. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> GetWebhooks200Response get_webhooks(workspace, opt_pretty=opt_pretty, limit=limit, offset=offset, resource=resource, opt_fields=opt_fields)

Get multiple webhooks

<b>Required scope: </b><code>webhooks:read</code>

Get the compact representation of all webhooks your app has registered for the authenticated user in the given workspace.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_webhooks200_response import GetWebhooks200Response
from asana_asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.asana.com/api/1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = asana_asyncio.Configuration(
    host = "https://app.asana.com/api/1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.WebhooksApi(api_client)
    workspace = '1331' # str | The workspace to query for webhooks in.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    resource = '51648' # str | Only return webhooks for the given resource. (optional)
    opt_fields = ['[\"active\",\"created_at\",\"delivery_retry_count\",\"failure_deletion_timestamp\",\"filters\",\"filters.action\",\"filters.fields\",\"filters.resource_subtype\",\"last_failure_at\",\"last_failure_content\",\"last_success_at\",\"next_attempt_after\",\"offset\",\"path\",\"resource\",\"resource.name\",\"target\",\"uri\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get multiple webhooks
        api_response = await api_instance.get_webhooks(workspace, opt_pretty=opt_pretty, limit=limit, offset=offset, resource=resource, opt_fields=opt_fields)
        print("The response of WebhooksApi->get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace to query for webhooks in. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **resource** | **str**| Only return webhooks for the given resource. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetWebhooks200Response**](GetWebhooks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested webhooks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> GetWebhook200Response update_webhook(webhook_gid, update_webhook_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Update a webhook

<b>Required scope: </b><code>webhooks:write</code>

An existing webhook's filters can be updated by making a PUT request on the URL for that webhook. Note that the webhook's previous `filters` array will be completely overwritten by the `filters` sent in the PUT request.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_webhook200_response import GetWebhook200Response
from asana_asyncio.models.update_webhook_request import UpdateWebhookRequest
from asana_asyncio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.asana.com/api/1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = asana_asyncio.Configuration(
    host = "https://app.asana.com/api/1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.WebhooksApi(api_client)
    webhook_gid = '12345' # str | Globally unique identifier for the webhook.
    update_webhook_request = asana_asyncio.UpdateWebhookRequest() # UpdateWebhookRequest | The updated filters for the webhook.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"active\",\"created_at\",\"delivery_retry_count\",\"failure_deletion_timestamp\",\"filters\",\"filters.action\",\"filters.fields\",\"filters.resource_subtype\",\"last_failure_at\",\"last_failure_content\",\"last_success_at\",\"next_attempt_after\",\"resource\",\"resource.name\",\"target\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Update a webhook
        api_response = await api_instance.update_webhook(webhook_gid, update_webhook_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of WebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_gid** | **str**| Globally unique identifier for the webhook. | 
 **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)| The updated filters for the webhook. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetWebhook200Response**](GetWebhook200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the webhook. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

