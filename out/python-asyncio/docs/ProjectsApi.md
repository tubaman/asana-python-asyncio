# asana_asyncio.ProjectsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_field_setting_for_project**](ProjectsApi.md#add_custom_field_setting_for_project) | **POST** /projects/{project_gid}/addCustomFieldSetting | Add a custom field to a project
[**add_followers_for_project**](ProjectsApi.md#add_followers_for_project) | **POST** /projects/{project_gid}/addFollowers | Add followers to a project
[**add_members_for_project**](ProjectsApi.md#add_members_for_project) | **POST** /projects/{project_gid}/addMembers | Add users to a project
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create a project
[**create_project_for_team**](ProjectsApi.md#create_project_for_team) | **POST** /teams/{team_gid}/projects | Create a project in a team
[**create_project_for_workspace**](ProjectsApi.md#create_project_for_workspace) | **POST** /workspaces/{workspace_gid}/projects | Create a project in a workspace
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects/{project_gid} | Delete a project
[**duplicate_project**](ProjectsApi.md#duplicate_project) | **POST** /projects/{project_gid}/duplicate | Duplicate a project
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{project_gid} | Get a project
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | Get multiple projects
[**get_projects_for_task**](ProjectsApi.md#get_projects_for_task) | **GET** /tasks/{task_gid}/projects | Get projects a task is in
[**get_projects_for_team**](ProjectsApi.md#get_projects_for_team) | **GET** /teams/{team_gid}/projects | Get a team&#39;s projects
[**get_projects_for_workspace**](ProjectsApi.md#get_projects_for_workspace) | **GET** /workspaces/{workspace_gid}/projects | Get all projects in a workspace
[**get_task_counts_for_project**](ProjectsApi.md#get_task_counts_for_project) | **GET** /projects/{project_gid}/task_counts | Get task count of a project
[**project_save_as_template**](ProjectsApi.md#project_save_as_template) | **POST** /projects/{project_gid}/saveAsTemplate | Create a project template from a project
[**remove_custom_field_setting_for_project**](ProjectsApi.md#remove_custom_field_setting_for_project) | **POST** /projects/{project_gid}/removeCustomFieldSetting | Remove a custom field from a project
[**remove_followers_for_project**](ProjectsApi.md#remove_followers_for_project) | **POST** /projects/{project_gid}/removeFollowers | Remove followers from a project
[**remove_members_for_project**](ProjectsApi.md#remove_members_for_project) | **POST** /projects/{project_gid}/removeMembers | Remove users from a project
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{project_gid} | Update a project


# **add_custom_field_setting_for_project**
> AddCustomFieldSettingForPortfolio200Response add_custom_field_setting_for_project(project_gid, add_custom_field_setting_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Add a custom field to a project

<b>Required scope: </b><code>projects:write</code>

Custom fields are associated with projects by way of custom field settings.  This method creates a setting for the project.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_custom_field_setting_for_portfolio200_response import AddCustomFieldSettingForPortfolio200Response
from asana_asyncio.models.add_custom_field_setting_for_portfolio_request import AddCustomFieldSettingForPortfolioRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    add_custom_field_setting_for_portfolio_request = asana_asyncio.AddCustomFieldSettingForPortfolioRequest() # AddCustomFieldSettingForPortfolioRequest | Information about the custom field setting.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"custom_field\",\"custom_field.asana_created_field\",\"custom_field.created_by\",\"custom_field.created_by.name\",\"custom_field.currency_code\",\"custom_field.custom_label\",\"custom_field.custom_label_position\",\"custom_field.date_value\",\"custom_field.date_value.date\",\"custom_field.date_value.date_time\",\"custom_field.default_access_level\",\"custom_field.description\",\"custom_field.display_value\",\"custom_field.enabled\",\"custom_field.enum_options\",\"custom_field.enum_options.color\",\"custom_field.enum_options.enabled\",\"custom_field.enum_options.name\",\"custom_field.enum_value\",\"custom_field.enum_value.color\",\"custom_field.enum_value.enabled\",\"custom_field.enum_value.name\",\"custom_field.format\",\"custom_field.has_notifications_enabled\",\"custom_field.id_prefix\",\"custom_field.is_formula_field\",\"custom_field.is_global_to_workspace\",\"custom_field.is_value_read_only\",\"custom_field.multi_enum_values\",\"custom_field.multi_enum_values.color\",\"custom_field.multi_enum_values.enabled\",\"custom_field.multi_enum_values.name\",\"custom_field.name\",\"custom_field.number_value\",\"custom_field.people_value\",\"custom_field.people_value.name\",\"custom_field.precision\",\"custom_field.privacy_setting\",\"custom_field.representation_type\",\"custom_field.resource_subtype\",\"custom_field.text_value\",\"custom_field.type\",\"is_important\",\"parent\",\"parent.name\",\"project\",\"project.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Add a custom field to a project
        api_response = await api_instance.add_custom_field_setting_for_project(project_gid, add_custom_field_setting_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->add_custom_field_setting_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_custom_field_setting_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **add_custom_field_setting_for_portfolio_request** | [**AddCustomFieldSettingForPortfolioRequest**](AddCustomFieldSettingForPortfolioRequest.md)| Information about the custom field setting. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**AddCustomFieldSettingForPortfolio200Response**](AddCustomFieldSettingForPortfolio200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added the custom field to the project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_followers_for_project**
> CreateProject201Response add_followers_for_project(project_gid, add_followers_for_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Add followers to a project

Adds the specified list of users as followers to the project. Followers are a subset of members who have opted in to receive "tasks added" notifications for a project. Therefore, if the users are not already members of the project, they will also become members as a result of this operation.
Returns the updated project record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_followers_for_project_request import AddFollowersForProjectRequest
from asana_asyncio.models.create_project201_response import CreateProject201Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    add_followers_for_project_request = asana_asyncio.AddFollowersForProjectRequest() # AddFollowersForProjectRequest | Information about the followers being added.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Add followers to a project
        api_response = await api_instance.add_followers_for_project(project_gid, add_followers_for_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->add_followers_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_followers_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **add_followers_for_project_request** | [**AddFollowersForProjectRequest**](AddFollowersForProjectRequest.md)| Information about the followers being added. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added followers to the project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_members_for_project**
> CreateProject201Response add_members_for_project(project_gid, add_members_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Add users to a project

Adds the specified list of users as members of the project. Note that a user being added as a member may also be added as a *follower* as a result of this operation. This is because the user's default notification settings (i.e., in the "Notifications" tab of "My Profile Settings") will override this endpoint's default behavior of setting "Tasks added" notifications to `false`.
Returns the updated project record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_members_for_portfolio_request import AddMembersForPortfolioRequest
from asana_asyncio.models.create_project201_response import CreateProject201Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    add_members_for_portfolio_request = asana_asyncio.AddMembersForPortfolioRequest() # AddMembersForPortfolioRequest | Information about the members being added.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Add users to a project
        api_response = await api_instance.add_members_for_project(project_gid, add_members_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->add_members_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_members_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **add_members_for_portfolio_request** | [**AddMembersForPortfolioRequest**](AddMembersForPortfolioRequest.md)| Information about the members being added. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added members to the project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> CreateProject201Response create_project(create_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a project

<b>Required scope: </b><code>projects:write</code>

Create a new project in a workspace or team.

Every project is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the `workspace` parameter regardless of whether or not it is an
organization.

If the workspace for your project is an organization, you must also
supply a `team` to share the project with.

Returns the full record of the newly created project.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_project201_response import CreateProject201Response
from asana_asyncio.models.create_project_request import CreateProjectRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    create_project_request = asana_asyncio.CreateProjectRequest() # CreateProjectRequest | The project to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a project
        api_response = await api_instance.create_project(create_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)| The project to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully retrieved projects. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_for_team**
> CreateProject201Response create_project_for_team(team_gid, create_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a project in a team

<b>Required scope: </b><code>projects:write</code>

Creates a project shared with the given team.

Returns the full record of the newly created project.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_project201_response import CreateProject201Response
from asana_asyncio.models.create_project_request import CreateProjectRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    team_gid = '159874' # str | Globally unique identifier for the team.
    create_project_request = asana_asyncio.CreateProjectRequest() # CreateProjectRequest | The new project to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a project in a team
        api_response = await api_instance.create_project_for_team(team_gid, create_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->create_project_for_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_for_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)| The new project to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the specified project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_for_workspace**
> CreateProject201Response create_project_for_workspace(workspace_gid, create_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a project in a workspace

<b>Required scope: </b><code>projects:write</code>

Creates a project in the workspace.

If the workspace for your project is an organization, you must also
supply a team to share the project with.

Returns the full record of the newly created project.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_project201_response import CreateProject201Response
from asana_asyncio.models.create_project_request import CreateProjectRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
    create_project_request = asana_asyncio.CreateProjectRequest() # CreateProjectRequest | The new project to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a project in a workspace
        api_response = await api_instance.create_project_for_workspace(workspace_gid, create_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->create_project_for_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_for_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)| The new project to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new project in the specified workspace. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> DeleteAllocation200Response delete_project(project_gid, opt_pretty=opt_pretty)

Delete a project

<b>Required scope: </b><code>projects:delete</code>

A specific, existing project can be deleted by making a DELETE request on
the URL for that project.

Returns an empty data record.

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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a project
        api_response = await api_instance.delete_project(project_gid, opt_pretty=opt_pretty)
        print("The response of ProjectsApi->delete_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
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
**200** | Successfully deleted the specified project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_project**
> GetJob200Response duplicate_project(project_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, duplicate_project_request=duplicate_project_request)

Duplicate a project

<b>Required scope: </b><code>projects:write</code>

Creates and returns a job that will asynchronously handle the duplication.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.duplicate_project_request import DuplicateProjectRequest
from asana_asyncio.models.get_job200_response import GetJob200Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"new_graph_export\",\"new_project\",\"new_project.name\",\"new_project_template\",\"new_project_template.name\",\"new_task\",\"new_task.created_by\",\"new_task.name\",\"new_task.resource_subtype\",\"new_task_template\",\"new_task_template.name\",\"resource_subtype\",\"status\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)
    duplicate_project_request = asana_asyncio.DuplicateProjectRequest() # DuplicateProjectRequest | Describes the duplicate's name and the elements that will be duplicated. (optional)

    try:
        # Duplicate a project
        api_response = await api_instance.duplicate_project(project_gid, opt_pretty=opt_pretty, opt_fields=opt_fields, duplicate_project_request=duplicate_project_request)
        print("The response of ProjectsApi->duplicate_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->duplicate_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 
 **duplicate_project_request** | [**DuplicateProjectRequest**](DuplicateProjectRequest.md)| Describes the duplicate&#39;s name and the elements that will be duplicated. | [optional] 

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
**201** | Successfully created the job to handle duplication. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> CreateProject201Response get_project(project_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a project

<b>Required scope: </b><code>projects:read</code>

<table>
  <tr>
    <th>Field</th>
    <th>Required Scope</th>
  </tr>
  <tr>
    <td><code>custom_field_settings</code></td>
    <td><code>custom_fields:read</code></td>
  </tr>
  <tr>
    <td><code>custom_fields</code></td>
    <td><code>custom_fields:read</code></td>
  </tr>
</table>

Returns the complete project record for a single project.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_project201_response import CreateProject201Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a project
        api_response = await api_instance.get_project(project_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> GetItemsForPortfolio200Response get_projects(opt_pretty=opt_pretty, limit=limit, offset=offset, workspace=workspace, team=team, archived=archived, opt_fields=opt_fields)

Get multiple projects

<b>Required scope: </b><code>projects:read</code>

Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned.
*Note: This endpoint may timeout for large domains. Try filtering by team!*

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_items_for_portfolio200_response import GetItemsForPortfolio200Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    workspace = '1331' # str | The workspace or organization to filter projects on. (optional)
    team = '14916' # str | The team to filter projects on. (optional)
    archived = false # bool | Only return projects whose `archived` field takes on the value of this parameter. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"offset\",\"owner\",\"path\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get multiple projects
        api_response = await api_instance.get_projects(opt_pretty=opt_pretty, limit=limit, offset=offset, workspace=workspace, team=team, archived=archived, opt_fields=opt_fields)
        print("The response of ProjectsApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **workspace** | **str**| The workspace or organization to filter projects on. | [optional] 
 **team** | **str**| The team to filter projects on. | [optional] 
 **archived** | **bool**| Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetItemsForPortfolio200Response**](GetItemsForPortfolio200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved projects. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_for_task**
> GetItemsForPortfolio200Response get_projects_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get projects a task is in

<b>Required scope: </b><code>projects:read</code>

Returns a compact representation of all of the projects the task is in.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_items_for_portfolio200_response import GetItemsForPortfolio200Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"offset\",\"owner\",\"path\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get projects a task is in
        api_response = await api_instance.get_projects_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of ProjectsApi->get_projects_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetItemsForPortfolio200Response**](GetItemsForPortfolio200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the projects for the given task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_for_team**
> GetItemsForPortfolio200Response get_projects_for_team(team_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, archived=archived, opt_fields=opt_fields)

Get a team's projects

<b>Required scope: </b><code>projects:read</code>

Returns the compact project records for all projects in the team.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_items_for_portfolio200_response import GetItemsForPortfolio200Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    team_gid = '159874' # str | Globally unique identifier for the team.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    archived = false # bool | Only return projects whose `archived` field takes on the value of this parameter. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"offset\",\"owner\",\"path\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a team's projects
        api_response = await api_instance.get_projects_for_team(team_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, archived=archived, opt_fields=opt_fields)
        print("The response of ProjectsApi->get_projects_for_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_for_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **archived** | **bool**| Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetItemsForPortfolio200Response**](GetItemsForPortfolio200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested team&#39;s projects. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_for_workspace**
> GetItemsForPortfolio200Response get_projects_for_workspace(workspace_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, archived=archived, opt_fields=opt_fields)

Get all projects in a workspace

<b>Required scope: </b><code>projects:read</code>

Returns the compact project records for all projects in the workspace.
*Note: This endpoint may timeout for large domains. Prefer the `/teams/{team_gid}/projects` endpoint.*

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_items_for_portfolio200_response import GetItemsForPortfolio200Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    archived = false # bool | Only return projects whose `archived` field takes on the value of this parameter. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"offset\",\"owner\",\"path\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get all projects in a workspace
        api_response = await api_instance.get_projects_for_workspace(workspace_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, archived=archived, opt_fields=opt_fields)
        print("The response of ProjectsApi->get_projects_for_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_for_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **archived** | **bool**| Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetItemsForPortfolio200Response**](GetItemsForPortfolio200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested workspace&#39;s projects. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_counts_for_project**
> GetTaskCountsForProject200Response get_task_counts_for_project(project_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get task count of a project

<b>Required scope: </b><code>projects:read</code>

<table>
  <tr>
    <th>Field</th>
    <th>Required Scope</th>
  </tr>
  <tr>
    <td><code>custom_field_settings</code></td>
    <td><code>custom_fields:read</code></td>
  </tr>
  <tr>
    <td><code>custom_fields</code></td>
    <td><code>custom_fields:read</code></td>
  </tr>
</table>

Get an object that holds task count fields. **All fields are excluded by default**. You must [opt in](/docs/inputoutput-options) using `opt_fields` to get any information from this endpoint.

This endpoint has an additional [rate limit](/docs/rate-limits) and each field counts especially high against our [cost limits](/docs/rate-limits#cost-limits).

Milestones are just tasks, so they are included in the `num_tasks`, `num_incomplete_tasks`, and `num_completed_tasks` counts.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_task_counts_for_project200_response import GetTaskCountsForProject200Response
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"num_completed_milestones\",\"num_completed_tasks\",\"num_incomplete_milestones\",\"num_incomplete_tasks\",\"num_milestones\",\"num_tasks\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get task count of a project
        api_response = await api_instance.get_task_counts_for_project(project_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->get_task_counts_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_task_counts_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetTaskCountsForProject200Response**](GetTaskCountsForProject200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested project&#39;s task counts. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_save_as_template**
> GetJob200Response project_save_as_template(project_gid, project_save_as_template_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a project template from a project

Creates and returns a job that will asynchronously handle the project template creation.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_job200_response import GetJob200Response
from asana_asyncio.models.project_save_as_template_request import ProjectSaveAsTemplateRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    project_save_as_template_request = asana_asyncio.ProjectSaveAsTemplateRequest() # ProjectSaveAsTemplateRequest | Describes the inputs used for creating a project template, such as the resulting project template's name, which team it should be created in.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"new_graph_export\",\"new_project\",\"new_project.name\",\"new_project_template\",\"new_project_template.name\",\"new_task\",\"new_task.created_by\",\"new_task.name\",\"new_task.resource_subtype\",\"new_task_template\",\"new_task_template.name\",\"resource_subtype\",\"status\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a project template from a project
        api_response = await api_instance.project_save_as_template(project_gid, project_save_as_template_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->project_save_as_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_save_as_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **project_save_as_template_request** | [**ProjectSaveAsTemplateRequest**](ProjectSaveAsTemplateRequest.md)| Describes the inputs used for creating a project template, such as the resulting project template&#39;s name, which team it should be created in. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetJob200Response**](GetJob200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the job to handle project template creation. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_custom_field_setting_for_project**
> DeleteAllocation200Response remove_custom_field_setting_for_project(project_gid, remove_custom_field_setting_for_portfolio_request, opt_pretty=opt_pretty)

Remove a custom field from a project

<b>Required scope: </b><code>projects:write</code>

Removes a custom field setting from a project.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.delete_allocation200_response import DeleteAllocation200Response
from asana_asyncio.models.remove_custom_field_setting_for_portfolio_request import RemoveCustomFieldSettingForPortfolioRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    remove_custom_field_setting_for_portfolio_request = asana_asyncio.RemoveCustomFieldSettingForPortfolioRequest() # RemoveCustomFieldSettingForPortfolioRequest | Information about the custom field setting being removed.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Remove a custom field from a project
        api_response = await api_instance.remove_custom_field_setting_for_project(project_gid, remove_custom_field_setting_for_portfolio_request, opt_pretty=opt_pretty)
        print("The response of ProjectsApi->remove_custom_field_setting_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_custom_field_setting_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **remove_custom_field_setting_for_portfolio_request** | [**RemoveCustomFieldSettingForPortfolioRequest**](RemoveCustomFieldSettingForPortfolioRequest.md)| Information about the custom field setting being removed. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 

### Return type

[**DeleteAllocation200Response**](DeleteAllocation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the custom field from the project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_followers_for_project**
> CreateProject201Response remove_followers_for_project(project_gid, remove_followers_for_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Remove followers from a project

Removes the specified list of users from following the project, this will not affect project membership status.
Returns the updated project record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_project201_response import CreateProject201Response
from asana_asyncio.models.remove_followers_for_project_request import RemoveFollowersForProjectRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    remove_followers_for_project_request = asana_asyncio.RemoveFollowersForProjectRequest() # RemoveFollowersForProjectRequest | Information about the followers being removed.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Remove followers from a project
        api_response = await api_instance.remove_followers_for_project(project_gid, remove_followers_for_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->remove_followers_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_followers_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **remove_followers_for_project_request** | [**RemoveFollowersForProjectRequest**](RemoveFollowersForProjectRequest.md)| Information about the followers being removed. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed followers from the project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_members_for_project**
> CreateProject201Response remove_members_for_project(project_gid, remove_members_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Remove users from a project

Removes the specified list of users from members of the project.
Returns the updated project record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_project201_response import CreateProject201Response
from asana_asyncio.models.remove_members_for_portfolio_request import RemoveMembersForPortfolioRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    remove_members_for_portfolio_request = asana_asyncio.RemoveMembersForPortfolioRequest() # RemoveMembersForPortfolioRequest | Information about the members being removed.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Remove users from a project
        api_response = await api_instance.remove_members_for_project(project_gid, remove_members_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->remove_members_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_members_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **remove_members_for_portfolio_request** | [**RemoveMembersForPortfolioRequest**](RemoveMembersForPortfolioRequest.md)| Information about the members being removed. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the members from the project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> CreateProject201Response update_project(project_gid, update_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Update a project

<b>Required scope: </b><code>projects:write</code>

A specific, existing project can be updated by making a PUT request on
the URL for that project. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated project record.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_project201_response import CreateProject201Response
from asana_asyncio.models.update_project_request import UpdateProjectRequest
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
    api_instance = asana_asyncio.ProjectsApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    update_project_request = asana_asyncio.UpdateProjectRequest() # UpdateProjectRequest | The updated fields for the project.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"owner\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Update a project
        api_response = await api_instance.update_project(project_gid, update_project_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of ProjectsApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md)| The updated fields for the project. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the project. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

