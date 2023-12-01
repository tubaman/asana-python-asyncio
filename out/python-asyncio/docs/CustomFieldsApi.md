# asana_asyncio.CustomFieldsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_field**](CustomFieldsApi.md#create_custom_field) | **POST** /custom_fields | Create a custom field
[**create_enum_option_for_custom_field**](CustomFieldsApi.md#create_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options | Create an enum option
[**delete_custom_field**](CustomFieldsApi.md#delete_custom_field) | **DELETE** /custom_fields/{custom_field_gid} | Delete a custom field
[**get_custom_field**](CustomFieldsApi.md#get_custom_field) | **GET** /custom_fields/{custom_field_gid} | Get a custom field
[**get_custom_fields_for_workspace**](CustomFieldsApi.md#get_custom_fields_for_workspace) | **GET** /workspaces/{workspace_gid}/custom_fields | Get a workspace&#39;s custom fields
[**insert_enum_option_for_custom_field**](CustomFieldsApi.md#insert_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options/insert | Reorder a custom field&#39;s enum
[**update_custom_field**](CustomFieldsApi.md#update_custom_field) | **PUT** /custom_fields/{custom_field_gid} | Update a custom field
[**update_enum_option**](CustomFieldsApi.md#update_enum_option) | **PUT** /enum_options/{enum_option_gid} | Update an enum option


# **create_custom_field**
> CreateCustomField201Response create_custom_field(create_custom_field_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a custom field

Creates a new custom field in a workspace. Every custom field is required to be created in a specific workspace, and this workspace cannot be changed once set.  A custom field’s name must be unique within a workspace and not conflict with names of existing task properties such as `Due Date` or `Assignee`. A custom field’s type must be one of `text`, `enum`, `multi_enum`, `number`, `date`, or `people`.  Returns the full record of the newly created custom field.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.create_custom_field201_response import CreateCustomField201Response
from asana_asyncio.models.create_custom_field_request import CreateCustomFieldRequest
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.CustomFieldsApi(api_client)
    create_custom_field_request = asana_asyncio.CreateCustomFieldRequest() # CreateCustomFieldRequest | The custom field object to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"asana_created_field\",\"created_by\",\"created_by.name\",\"currency_code\",\"custom_label\",\"custom_label_position\",\"date_value\",\"date_value.date\",\"date_value.date_time\",\"description\",\"display_value\",\"enabled\",\"enum_options\",\"enum_options.color\",\"enum_options.enabled\",\"enum_options.name\",\"enum_value\",\"enum_value.color\",\"enum_value.enabled\",\"enum_value.name\",\"format\",\"has_notifications_enabled\",\"id_prefix\",\"is_formula_field\",\"is_global_to_workspace\",\"is_value_read_only\",\"multi_enum_values\",\"multi_enum_values.color\",\"multi_enum_values.enabled\",\"multi_enum_values.name\",\"name\",\"number_value\",\"people_value\",\"people_value.name\",\"precision\",\"representation_type\",\"resource_subtype\",\"text_value\",\"type\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a custom field
        api_response = await api_instance.create_custom_field(create_custom_field_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of CustomFieldsApi->create_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->create_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_field_request** | [**CreateCustomFieldRequest**](CreateCustomFieldRequest.md)| The custom field object to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateCustomField201Response**](CreateCustomField201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Custom field successfully created. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_enum_option_for_custom_field**
> CreateEnumOptionForCustomField201Response create_enum_option_for_custom_field(custom_field_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, create_enum_option_for_custom_field_request=create_enum_option_for_custom_field_request)

Create an enum option

Creates an enum option and adds it to this custom field’s list of enum options. A custom field can have at most 500 enum options (including disabled options). By default new enum options are inserted at the end of a custom field’s list. Locked custom fields can only have enum options added by the user who locked the field. Returns the full record of the newly created enum option.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.create_enum_option_for_custom_field201_response import CreateEnumOptionForCustomField201Response
from asana_asyncio.models.create_enum_option_for_custom_field_request import CreateEnumOptionForCustomFieldRequest
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.CustomFieldsApi(api_client)
    custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"color\",\"enabled\",\"name\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)
    create_enum_option_for_custom_field_request = asana_asyncio.CreateEnumOptionForCustomFieldRequest() # CreateEnumOptionForCustomFieldRequest | The enum option object to create. (optional)

    try:
        # Create an enum option
        api_response = await api_instance.create_enum_option_for_custom_field(custom_field_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, create_enum_option_for_custom_field_request=create_enum_option_for_custom_field_request)
        print("The response of CustomFieldsApi->create_enum_option_for_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->create_enum_option_for_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 
 **create_enum_option_for_custom_field_request** | [**CreateEnumOptionForCustomFieldRequest**](CreateEnumOptionForCustomFieldRequest.md)| The enum option object to create. | [optional] 

### Return type

[**CreateEnumOptionForCustomField201Response**](CreateEnumOptionForCustomField201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Custom field enum option successfully created. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> DeleteAttachment200Response delete_custom_field(custom_field_gid, opt_pretty=opt_pretty)

Delete a custom field

A specific, existing custom field can be deleted by making a DELETE request on the URL for that custom field. Locked custom fields can only be deleted by the user who locked the field. Returns an empty data record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.delete_attachment200_response import DeleteAttachment200Response
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.CustomFieldsApi(api_client)
    custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a custom field
        api_response = await api_instance.delete_custom_field(custom_field_gid, opt_pretty=opt_pretty)
        print("The response of CustomFieldsApi->delete_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->delete_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custom field was successfully deleted. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> CreateCustomField201Response get_custom_field(custom_field_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a custom field

Get the complete definition of a custom field’s metadata.  Since custom fields can be defined for one of a number of types, and these types have different data and behaviors, there are fields that are relevant to a particular type. For instance, as noted above, enum_options is only relevant for the enum type and defines the set of choices that the enum could represent. The examples below show some of these type-specific custom field definitions.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.create_custom_field201_response import CreateCustomField201Response
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.CustomFieldsApi(api_client)
    custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"asana_created_field\",\"created_by\",\"created_by.name\",\"currency_code\",\"custom_label\",\"custom_label_position\",\"date_value\",\"date_value.date\",\"date_value.date_time\",\"description\",\"display_value\",\"enabled\",\"enum_options\",\"enum_options.color\",\"enum_options.enabled\",\"enum_options.name\",\"enum_value\",\"enum_value.color\",\"enum_value.enabled\",\"enum_value.name\",\"format\",\"has_notifications_enabled\",\"id_prefix\",\"is_formula_field\",\"is_global_to_workspace\",\"is_value_read_only\",\"multi_enum_values\",\"multi_enum_values.color\",\"multi_enum_values.enabled\",\"multi_enum_values.name\",\"name\",\"number_value\",\"people_value\",\"people_value.name\",\"precision\",\"representation_type\",\"resource_subtype\",\"text_value\",\"type\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a custom field
        api_response = await api_instance.get_custom_field(custom_field_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of CustomFieldsApi->get_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->get_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateCustomField201Response**](CreateCustomField201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the complete definition of a custom field’s metadata. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields_for_workspace**
> GetCustomFieldsForWorkspace200Response get_custom_fields_for_workspace(workspace_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get a workspace's custom fields

Returns a list of the compact representation of all of the custom fields in a workspace.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_custom_fields_for_workspace200_response import GetCustomFieldsForWorkspace200Response
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.CustomFieldsApi(api_client)
    workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ['[\"asana_created_field\",\"created_by\",\"created_by.name\",\"currency_code\",\"custom_label\",\"custom_label_position\",\"date_value\",\"date_value.date\",\"date_value.date_time\",\"description\",\"display_value\",\"enabled\",\"enum_options\",\"enum_options.color\",\"enum_options.enabled\",\"enum_options.name\",\"enum_value\",\"enum_value.color\",\"enum_value.enabled\",\"enum_value.name\",\"format\",\"has_notifications_enabled\",\"id_prefix\",\"is_formula_field\",\"is_global_to_workspace\",\"is_value_read_only\",\"multi_enum_values\",\"multi_enum_values.color\",\"multi_enum_values.enabled\",\"multi_enum_values.name\",\"name\",\"number_value\",\"offset\",\"path\",\"people_value\",\"people_value.name\",\"precision\",\"representation_type\",\"resource_subtype\",\"text_value\",\"type\",\"uri\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a workspace's custom fields
        api_response = await api_instance.get_custom_fields_for_workspace(workspace_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of CustomFieldsApi->get_custom_fields_for_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->get_custom_fields_for_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetCustomFieldsForWorkspace200Response**](GetCustomFieldsForWorkspace200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved all custom fields for the given workspace. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_enum_option_for_custom_field**
> CreateEnumOptionForCustomField201Response insert_enum_option_for_custom_field(custom_field_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, insert_enum_option_for_custom_field_request=insert_enum_option_for_custom_field_request)

Reorder a custom field's enum

Moves a particular enum option to be either before or after another specified enum option in the custom field. Locked custom fields can only be reordered by the user who locked the field.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.create_enum_option_for_custom_field201_response import CreateEnumOptionForCustomField201Response
from asana_asyncio.models.insert_enum_option_for_custom_field_request import InsertEnumOptionForCustomFieldRequest
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.CustomFieldsApi(api_client)
    custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"color\",\"enabled\",\"name\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)
    insert_enum_option_for_custom_field_request = asana_asyncio.InsertEnumOptionForCustomFieldRequest() # InsertEnumOptionForCustomFieldRequest | The enum option object to create. (optional)

    try:
        # Reorder a custom field's enum
        api_response = await api_instance.insert_enum_option_for_custom_field(custom_field_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, insert_enum_option_for_custom_field_request=insert_enum_option_for_custom_field_request)
        print("The response of CustomFieldsApi->insert_enum_option_for_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->insert_enum_option_for_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 
 **insert_enum_option_for_custom_field_request** | [**InsertEnumOptionForCustomFieldRequest**](InsertEnumOptionForCustomFieldRequest.md)| The enum option object to create. | [optional] 

### Return type

[**CreateEnumOptionForCustomField201Response**](CreateEnumOptionForCustomField201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field enum option successfully reordered. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> CreateCustomField201Response update_custom_field(custom_field_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, create_custom_field_request=create_custom_field_request)

Update a custom field

A specific, existing custom field can be updated by making a PUT request on the URL for that custom field. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the custom field. A custom field’s `type` cannot be updated. An enum custom field’s `enum_options` cannot be updated with this endpoint. Instead see “Work With Enum Options” for information on how to update `enum_options`. Locked custom fields can only be updated by the user who locked the field. Returns the complete updated custom field record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.create_custom_field201_response import CreateCustomField201Response
from asana_asyncio.models.create_custom_field_request import CreateCustomFieldRequest
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.CustomFieldsApi(api_client)
    custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"asana_created_field\",\"created_by\",\"created_by.name\",\"currency_code\",\"custom_label\",\"custom_label_position\",\"date_value\",\"date_value.date\",\"date_value.date_time\",\"description\",\"display_value\",\"enabled\",\"enum_options\",\"enum_options.color\",\"enum_options.enabled\",\"enum_options.name\",\"enum_value\",\"enum_value.color\",\"enum_value.enabled\",\"enum_value.name\",\"format\",\"has_notifications_enabled\",\"id_prefix\",\"is_formula_field\",\"is_global_to_workspace\",\"is_value_read_only\",\"multi_enum_values\",\"multi_enum_values.color\",\"multi_enum_values.enabled\",\"multi_enum_values.name\",\"name\",\"number_value\",\"people_value\",\"people_value.name\",\"precision\",\"representation_type\",\"resource_subtype\",\"text_value\",\"type\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)
    create_custom_field_request = asana_asyncio.CreateCustomFieldRequest() # CreateCustomFieldRequest | The custom field object with all updated properties. (optional)

    try:
        # Update a custom field
        api_response = await api_instance.update_custom_field(custom_field_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, create_custom_field_request=create_custom_field_request)
        print("The response of CustomFieldsApi->update_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->update_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 
 **create_custom_field_request** | [**CreateCustomFieldRequest**](CreateCustomFieldRequest.md)| The custom field object with all updated properties. | [optional] 

### Return type

[**CreateCustomField201Response**](CreateCustomField201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custom field was successfully updated. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_enum_option**
> CreateEnumOptionForCustomField201Response update_enum_option(enum_option_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, update_enum_option_request=update_enum_option_request)

Update an enum option

Updates an existing enum option. Enum custom fields require at least one enabled enum option. Locked custom fields can only be updated by the user who locked the field. Returns the full record of the updated enum option.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.create_enum_option_for_custom_field201_response import CreateEnumOptionForCustomField201Response
from asana_asyncio.models.update_enum_option_request import UpdateEnumOptionRequest
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.CustomFieldsApi(api_client)
    enum_option_gid = '124578' # str | Globally unique identifier for the enum option.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"color\",\"enabled\",\"name\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)
    update_enum_option_request = asana_asyncio.UpdateEnumOptionRequest() # UpdateEnumOptionRequest | The enum option object to update (optional)

    try:
        # Update an enum option
        api_response = await api_instance.update_enum_option(enum_option_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, update_enum_option_request=update_enum_option_request)
        print("The response of CustomFieldsApi->update_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->update_enum_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enum_option_gid** | **str**| Globally unique identifier for the enum option. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 
 **update_enum_option_request** | [**UpdateEnumOptionRequest**](UpdateEnumOptionRequest.md)| The enum option object to update | [optional] 

### Return type

[**CreateEnumOptionForCustomField201Response**](CreateEnumOptionForCustomField201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the specified custom field enum. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

