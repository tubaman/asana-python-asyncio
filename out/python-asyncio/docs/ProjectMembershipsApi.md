# asana_asyncio.ProjectMembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_membership**](ProjectMembershipsApi.md#get_project_membership) | **GET** /project_memberships/{project_membership_gid} | Get a project membership
[**get_project_memberships_for_project**](ProjectMembershipsApi.md#get_project_memberships_for_project) | **GET** /projects/{project_gid}/project_memberships | Get memberships from a project


# **get_project_membership**
> GetProjectMembership200Response get_project_membership(project_membership_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a project membership

Returns the complete project record for a single project membership.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_project_membership200_response import GetProjectMembership200Response
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
    api_instance = asana_asyncio.ProjectMembershipsApi(api_client)
    project_membership_gid = '1331' # str | 
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"access_level\",\"member\",\"member.name\",\"parent\",\"parent.name\",\"project\",\"project.name\",\"user\",\"user.name\",\"write_access\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a project membership
        api_response = await api_instance.get_project_membership(project_membership_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectMembershipsApi->get_project_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectMembershipsApi->get_project_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_membership_gid** | **str**|  | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetProjectMembership200Response**](GetProjectMembership200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested project membership. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_memberships_for_project**
> GetProjectMembershipsForProject200Response get_project_memberships_for_project(project_gid, user=user, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get memberships from a project

Returns the compact project membership records for the project.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_project_memberships_for_project200_response import GetProjectMembershipsForProject200Response
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
    api_instance = asana_asyncio.ProjectMembershipsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    user = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (optional)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ['[\"access_level\",\"member\",\"member.name\",\"offset\",\"parent\",\"parent.name\",\"path\",\"uri\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get memberships from a project
        api_response = await api_instance.get_project_memberships_for_project(project_gid, user=user, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of ProjectMembershipsApi->get_project_memberships_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectMembershipsApi->get_project_memberships_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **user** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetProjectMembershipsForProject200Response**](GetProjectMembershipsForProject200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested project&#39;s memberships. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

