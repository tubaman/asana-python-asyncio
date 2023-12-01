# asana_asyncio.CustomFieldSettingsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_field_settings_for_portfolio**](CustomFieldSettingsApi.md#get_custom_field_settings_for_portfolio) | **GET** /portfolios/{portfolio_gid}/custom_field_settings | Get a portfolio&#39;s custom fields
[**get_custom_field_settings_for_project**](CustomFieldSettingsApi.md#get_custom_field_settings_for_project) | **GET** /projects/{project_gid}/custom_field_settings | Get a project&#39;s custom fields


# **get_custom_field_settings_for_portfolio**
> GetCustomFieldSettingsForProject200Response get_custom_field_settings_for_portfolio(portfolio_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get a portfolio's custom fields

Returns a list of all of the custom fields settings on a portfolio, in compact form.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_custom_field_settings_for_project200_response import GetCustomFieldSettingsForProject200Response
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
    api_instance = asana_asyncio.CustomFieldSettingsApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ['[\"custom_field\",\"custom_field.asana_created_field\",\"custom_field.created_by\",\"custom_field.created_by.name\",\"custom_field.currency_code\",\"custom_field.custom_label\",\"custom_field.custom_label_position\",\"custom_field.date_value\",\"custom_field.date_value.date\",\"custom_field.date_value.date_time\",\"custom_field.description\",\"custom_field.display_value\",\"custom_field.enabled\",\"custom_field.enum_options\",\"custom_field.enum_options.color\",\"custom_field.enum_options.enabled\",\"custom_field.enum_options.name\",\"custom_field.enum_value\",\"custom_field.enum_value.color\",\"custom_field.enum_value.enabled\",\"custom_field.enum_value.name\",\"custom_field.format\",\"custom_field.has_notifications_enabled\",\"custom_field.id_prefix\",\"custom_field.is_formula_field\",\"custom_field.is_global_to_workspace\",\"custom_field.is_value_read_only\",\"custom_field.multi_enum_values\",\"custom_field.multi_enum_values.color\",\"custom_field.multi_enum_values.enabled\",\"custom_field.multi_enum_values.name\",\"custom_field.name\",\"custom_field.number_value\",\"custom_field.people_value\",\"custom_field.people_value.name\",\"custom_field.precision\",\"custom_field.representation_type\",\"custom_field.resource_subtype\",\"custom_field.text_value\",\"custom_field.type\",\"is_important\",\"offset\",\"parent\",\"parent.name\",\"path\",\"project\",\"project.name\",\"uri\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a portfolio's custom fields
        api_response = await api_instance.get_custom_field_settings_for_portfolio(portfolio_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of CustomFieldSettingsApi->get_custom_field_settings_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSettingsApi->get_custom_field_settings_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetCustomFieldSettingsForProject200Response**](GetCustomFieldSettingsForProject200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved custom field settings objects for a portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field_settings_for_project**
> GetCustomFieldSettingsForProject200Response get_custom_field_settings_for_project(project_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get a project's custom fields

Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [documentation for input/output options](https://developers.asana.com/docs/inputoutput-options) for more information.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_custom_field_settings_for_project200_response import GetCustomFieldSettingsForProject200Response
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
    api_instance = asana_asyncio.CustomFieldSettingsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ['[\"custom_field\",\"custom_field.asana_created_field\",\"custom_field.created_by\",\"custom_field.created_by.name\",\"custom_field.currency_code\",\"custom_field.custom_label\",\"custom_field.custom_label_position\",\"custom_field.date_value\",\"custom_field.date_value.date\",\"custom_field.date_value.date_time\",\"custom_field.description\",\"custom_field.display_value\",\"custom_field.enabled\",\"custom_field.enum_options\",\"custom_field.enum_options.color\",\"custom_field.enum_options.enabled\",\"custom_field.enum_options.name\",\"custom_field.enum_value\",\"custom_field.enum_value.color\",\"custom_field.enum_value.enabled\",\"custom_field.enum_value.name\",\"custom_field.format\",\"custom_field.has_notifications_enabled\",\"custom_field.id_prefix\",\"custom_field.is_formula_field\",\"custom_field.is_global_to_workspace\",\"custom_field.is_value_read_only\",\"custom_field.multi_enum_values\",\"custom_field.multi_enum_values.color\",\"custom_field.multi_enum_values.enabled\",\"custom_field.multi_enum_values.name\",\"custom_field.name\",\"custom_field.number_value\",\"custom_field.people_value\",\"custom_field.people_value.name\",\"custom_field.precision\",\"custom_field.representation_type\",\"custom_field.resource_subtype\",\"custom_field.text_value\",\"custom_field.type\",\"is_important\",\"offset\",\"parent\",\"parent.name\",\"path\",\"project\",\"project.name\",\"uri\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a project's custom fields
        api_response = await api_instance.get_custom_field_settings_for_project(project_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of CustomFieldSettingsApi->get_custom_field_settings_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldSettingsApi->get_custom_field_settings_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetCustomFieldSettingsForProject200Response**](GetCustomFieldSettingsForProject200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved custom field settings objects for a project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

