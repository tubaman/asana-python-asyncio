# asana_asyncio.ProjectBriefsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_brief**](ProjectBriefsApi.md#create_project_brief) | **POST** /projects/{project_gid}/project_briefs | Create a project brief
[**delete_project_brief**](ProjectBriefsApi.md#delete_project_brief) | **DELETE** /project_briefs/{project_brief_gid} | Delete a project brief
[**get_project_brief**](ProjectBriefsApi.md#get_project_brief) | **GET** /project_briefs/{project_brief_gid} | Get a project brief
[**update_project_brief**](ProjectBriefsApi.md#update_project_brief) | **PUT** /project_briefs/{project_brief_gid} | Update a project brief


# **create_project_brief**
> GetProjectBrief200Response create_project_brief(project_gid, update_project_brief_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a project brief

Creates a new project brief.  Returns the full record of the newly created project brief.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_project_brief200_response import GetProjectBrief200Response
from asana_asyncio.models.update_project_brief_request import UpdateProjectBriefRequest
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
    api_instance = asana_asyncio.ProjectBriefsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    update_project_brief_request = asana_asyncio.UpdateProjectBriefRequest() # UpdateProjectBriefRequest | The project brief to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"html_text\",\"permalink_url\",\"project\",\"project.name\",\"text\",\"title\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a project brief
        api_response = await api_instance.create_project_brief(project_gid, update_project_brief_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectBriefsApi->create_project_brief:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBriefsApi->create_project_brief: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **update_project_brief_request** | [**UpdateProjectBriefRequest**](UpdateProjectBriefRequest.md)| The project brief to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetProjectBrief200Response**](GetProjectBrief200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new project brief. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_brief**
> DeleteAttachment200Response delete_project_brief(project_brief_gid, opt_pretty=opt_pretty)

Delete a project brief

Deletes a specific, existing project brief.  Returns an empty data record.

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
    api_instance = asana_asyncio.ProjectBriefsApi(api_client)
    project_brief_gid = '12345' # str | Globally unique identifier for the project brief.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a project brief
        api_response = await api_instance.delete_project_brief(project_brief_gid, opt_pretty=opt_pretty)
        print("The response of ProjectBriefsApi->delete_project_brief:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBriefsApi->delete_project_brief: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 
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
**200** | Successfully deleted the specified project brief. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_brief**
> GetProjectBrief200Response get_project_brief(project_brief_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a project brief

Get the full record for a project brief.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_project_brief200_response import GetProjectBrief200Response
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
    api_instance = asana_asyncio.ProjectBriefsApi(api_client)
    project_brief_gid = '12345' # str | Globally unique identifier for the project brief.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"html_text\",\"permalink_url\",\"project\",\"project.name\",\"text\",\"title\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a project brief
        api_response = await api_instance.get_project_brief(project_brief_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectBriefsApi->get_project_brief:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBriefsApi->get_project_brief: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetProjectBrief200Response**](GetProjectBrief200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the record for a project brief. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**424** | You have exceeded one of the enforced rate limits in the API. See the [documentation on rate limiting](https://developers.asana.com/docs/#rate-limits) for more information. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |
**501** | There is an issue between the load balancers and Asana&#39;s API. |  -  |
**503** | Either the upstream service is unavailable to the API, or the API has been intentionally shut off. |  -  |
**504** | This request took too long to complete. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_brief**
> GetProjectBrief200Response update_project_brief(project_brief_gid, update_project_brief_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Update a project brief

An existing project brief can be updated by making a PUT request on the URL for that project brief. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated project brief record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_project_brief200_response import GetProjectBrief200Response
from asana_asyncio.models.update_project_brief_request import UpdateProjectBriefRequest
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
    api_instance = asana_asyncio.ProjectBriefsApi(api_client)
    project_brief_gid = '12345' # str | Globally unique identifier for the project brief.
    update_project_brief_request = asana_asyncio.UpdateProjectBriefRequest() # UpdateProjectBriefRequest | The updated fields for the project brief.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"html_text\",\"permalink_url\",\"project\",\"project.name\",\"text\",\"title\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Update a project brief
        api_response = await api_instance.update_project_brief(project_brief_gid, update_project_brief_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectBriefsApi->update_project_brief:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBriefsApi->update_project_brief: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 
 **update_project_brief_request** | [**UpdateProjectBriefRequest**](UpdateProjectBriefRequest.md)| The updated fields for the project brief. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetProjectBrief200Response**](GetProjectBrief200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the project brief. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

