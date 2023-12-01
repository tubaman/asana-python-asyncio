# asana_asyncio.OrganizationExportsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_export**](OrganizationExportsApi.md#create_organization_export) | **POST** /organization_exports | Create an organization export request
[**get_organization_export**](OrganizationExportsApi.md#get_organization_export) | **GET** /organization_exports/{organization_export_gid} | Get details on an org export request


# **create_organization_export**
> CreateOrganizationExport201Response create_organization_export(create_organization_export_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create an organization export request

This method creates a request to export an Organization. Asana will complete the export at some point after you create the request.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.create_organization_export201_response import CreateOrganizationExport201Response
from asana_asyncio.models.create_organization_export_request import CreateOrganizationExportRequest
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
    api_instance = asana_asyncio.OrganizationExportsApi(api_client)
    create_organization_export_request = asana_asyncio.CreateOrganizationExportRequest() # CreateOrganizationExportRequest | The organization to export.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"created_at\",\"download_url\",\"organization\",\"organization.name\",\"state\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create an organization export request
        api_response = await api_instance.create_organization_export(create_organization_export_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of OrganizationExportsApi->create_organization_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationExportsApi->create_organization_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_export_request** | [**CreateOrganizationExportRequest**](CreateOrganizationExportRequest.md)| The organization to export. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateOrganizationExport201Response**](CreateOrganizationExport201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created organization export request. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_export**
> CreateOrganizationExport201Response get_organization_export(organization_export_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get details on an org export request

Returns details of a previously-requested Organization export.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.create_organization_export201_response import CreateOrganizationExport201Response
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
    api_instance = asana_asyncio.OrganizationExportsApi(api_client)
    organization_export_gid = '12345' # str | Globally unique identifier for the organization export.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"created_at\",\"download_url\",\"organization\",\"organization.name\",\"state\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get details on an org export request
        api_response = await api_instance.get_organization_export(organization_export_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of OrganizationExportsApi->get_organization_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationExportsApi->get_organization_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_export_gid** | **str**| Globally unique identifier for the organization export. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateOrganizationExport201Response**](CreateOrganizationExport201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved organization export object. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

