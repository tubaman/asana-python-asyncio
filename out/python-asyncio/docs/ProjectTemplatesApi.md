# asana_asyncio.ProjectTemplatesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_template**](ProjectTemplatesApi.md#delete_project_template) | **DELETE** /project_templates/{project_template_gid} | Delete a project template
[**get_project_template**](ProjectTemplatesApi.md#get_project_template) | **GET** /project_templates/{project_template_gid} | Get a project template
[**get_project_templates**](ProjectTemplatesApi.md#get_project_templates) | **GET** /project_templates | Get multiple project templates
[**get_project_templates_for_team**](ProjectTemplatesApi.md#get_project_templates_for_team) | **GET** /teams/{team_gid}/project_templates | Get a team&#39;s project templates
[**instantiate_project**](ProjectTemplatesApi.md#instantiate_project) | **POST** /project_templates/{project_template_gid}/instantiateProject | Instantiate a project from a project template


# **delete_project_template**
> DeleteAllocation200Response delete_project_template(project_template_gid, opt_pretty=opt_pretty)

Delete a project template

A specific, existing project template can be deleted by making a DELETE request on the URL for that project template.

Returns an empty data record.

### Example

* Bearer Authentication (personalAccessToken):
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.ProjectTemplatesApi(api_client)
    project_template_gid = '1331' # str | Globally unique identifier for the project template.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a project template
        api_response = await api_instance.delete_project_template(project_template_gid, opt_pretty=opt_pretty)
        print("The response of ProjectTemplatesApi->delete_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->delete_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 

### Return type

[**DeleteAllocation200Response**](DeleteAllocation200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted the specified project template. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_template**
> GetProjectTemplate200Response get_project_template(project_template_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a project template

<b>Required scope: </b><code>project_templates:read</code>

Returns the complete project template record for a single project template.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_project_template200_response import GetProjectTemplate200Response
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
    api_instance = asana_asyncio.ProjectTemplatesApi(api_client)
    project_template_gid = '1331' # str | Globally unique identifier for the project template.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"color\",\"description\",\"html_description\",\"name\",\"owner\",\"public\",\"requested_dates\",\"requested_dates.description\",\"requested_dates.name\",\"requested_roles\",\"requested_roles.name\",\"team\",\"team.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a project template
        api_response = await api_instance.get_project_template(project_template_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectTemplatesApi->get_project_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->get_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetProjectTemplate200Response**](GetProjectTemplate200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested project template. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_templates**
> GetProjectTemplates200Response get_project_templates(opt_pretty=opt_pretty, workspace=workspace, team=team, limit=limit, offset=offset, opt_fields=opt_fields)

Get multiple project templates

<b>Required scope: </b><code>project_templates:read</code>

Returns the compact project template records for all project templates in the given team or workspace.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_project_templates200_response import GetProjectTemplates200Response
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
    api_instance = asana_asyncio.ProjectTemplatesApi(api_client)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    workspace = '12345' # str | The workspace to filter results on. (optional)
    team = '14916' # str | The team to filter projects on. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"color\",\"description\",\"html_description\",\"name\",\"offset\",\"owner\",\"path\",\"public\",\"requested_dates\",\"requested_dates.description\",\"requested_dates.name\",\"requested_roles\",\"requested_roles.name\",\"team\",\"team.name\",\"uri\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get multiple project templates
        api_response = await api_instance.get_project_templates(opt_pretty=opt_pretty, workspace=workspace, team=team, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of ProjectTemplatesApi->get_project_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->get_project_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **workspace** | **str**| The workspace to filter results on. | [optional] 
 **team** | **str**| The team to filter projects on. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetProjectTemplates200Response**](GetProjectTemplates200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested team&#39;s or workspace&#39;s project templates. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_templates_for_team**
> GetProjectTemplates200Response get_project_templates_for_team(team_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get a team's project templates

<b>Required scope: </b><code>project_templates:read</code>

Returns the compact project template records for all project templates in the team.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_project_templates200_response import GetProjectTemplates200Response
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
    api_instance = asana_asyncio.ProjectTemplatesApi(api_client)
    team_gid = '159874' # str | Globally unique identifier for the team.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"color\",\"description\",\"html_description\",\"name\",\"offset\",\"owner\",\"path\",\"public\",\"requested_dates\",\"requested_dates.description\",\"requested_dates.name\",\"requested_roles\",\"requested_roles.name\",\"team\",\"team.name\",\"uri\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a team's project templates
        api_response = await api_instance.get_project_templates_for_team(team_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of ProjectTemplatesApi->get_project_templates_for_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->get_project_templates_for_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetProjectTemplates200Response**](GetProjectTemplates200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested team&#39;s project templates. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instantiate_project**
> GetJob200Response instantiate_project(project_template_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, instantiate_project_request=instantiate_project_request)

Instantiate a project from a project template

<b>Required scope: </b><code>projects:write</code>

Creates and returns a job that will asynchronously handle the project instantiation.

To form this request, it is recommended to first make a request to [get a project template](/reference/getprojecttemplate). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.

_Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](/reference/workspaces) parameter._

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_job200_response import GetJob200Response
from asana_asyncio.models.instantiate_project_request import InstantiateProjectRequest
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
    api_instance = asana_asyncio.ProjectTemplatesApi(api_client)
    project_template_gid = '1331' # str | Globally unique identifier for the project template.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"new_graph_export\",\"new_graph_export.completed_at\",\"new_graph_export.created_at\",\"new_graph_export.download_url\",\"new_project\",\"new_project.name\",\"new_project_template\",\"new_project_template.name\",\"new_resource_export\",\"new_task\",\"new_task.created_by\",\"new_task.name\",\"new_task.resource_subtype\",\"new_task_template\",\"new_task_template.name\",\"resource_subtype\",\"status\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)
    instantiate_project_request = asana_asyncio.InstantiateProjectRequest() # InstantiateProjectRequest | Describes the inputs used for instantiating a project, such as the resulting project's name, which team it should be created in, and values for date variables. (optional)

    try:
        # Instantiate a project from a project template
        api_response = await api_instance.instantiate_project(project_template_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, instantiate_project_request=instantiate_project_request)
        print("The response of ProjectTemplatesApi->instantiate_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->instantiate_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 
 **instantiate_project_request** | [**InstantiateProjectRequest**](InstantiateProjectRequest.md)| Describes the inputs used for instantiating a project, such as the resulting project&#39;s name, which team it should be created in, and values for date variables. | [optional] 

### Return type

[**GetJob200Response**](GetJob200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the job to handle project instantiation. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

