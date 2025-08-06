# asana_asyncio.TasksApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dependencies_for_task**](TasksApi.md#add_dependencies_for_task) | **POST** /tasks/{task_gid}/addDependencies | Set dependencies for a task
[**add_dependents_for_task**](TasksApi.md#add_dependents_for_task) | **POST** /tasks/{task_gid}/addDependents | Set dependents for a task
[**add_followers_for_task**](TasksApi.md#add_followers_for_task) | **POST** /tasks/{task_gid}/addFollowers | Add followers to a task
[**add_project_for_task**](TasksApi.md#add_project_for_task) | **POST** /tasks/{task_gid}/addProject | Add a project to a task
[**add_tag_for_task**](TasksApi.md#add_tag_for_task) | **POST** /tasks/{task_gid}/addTag | Add a tag to a task
[**create_subtask_for_task**](TasksApi.md#create_subtask_for_task) | **POST** /tasks/{task_gid}/subtasks | Create a subtask
[**create_task**](TasksApi.md#create_task) | **POST** /tasks | Create a task
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /tasks/{task_gid} | Delete a task
[**duplicate_task**](TasksApi.md#duplicate_task) | **POST** /tasks/{task_gid}/duplicate | Duplicate a task
[**get_dependencies_for_task**](TasksApi.md#get_dependencies_for_task) | **GET** /tasks/{task_gid}/dependencies | Get dependencies from a task
[**get_dependents_for_task**](TasksApi.md#get_dependents_for_task) | **GET** /tasks/{task_gid}/dependents | Get dependents from a task
[**get_subtasks_for_task**](TasksApi.md#get_subtasks_for_task) | **GET** /tasks/{task_gid}/subtasks | Get subtasks from a task
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{task_gid} | Get a task
[**get_task_for_custom_id**](TasksApi.md#get_task_for_custom_id) | **GET** /workspaces/{workspace_gid}/tasks/custom_id/{custom_id} | Get a task for a given custom ID
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks | Get multiple tasks
[**get_tasks_for_project**](TasksApi.md#get_tasks_for_project) | **GET** /projects/{project_gid}/tasks | Get tasks from a project
[**get_tasks_for_section**](TasksApi.md#get_tasks_for_section) | **GET** /sections/{section_gid}/tasks | Get tasks from a section
[**get_tasks_for_tag**](TasksApi.md#get_tasks_for_tag) | **GET** /tags/{tag_gid}/tasks | Get tasks from a tag
[**get_tasks_for_user_task_list**](TasksApi.md#get_tasks_for_user_task_list) | **GET** /user_task_lists/{user_task_list_gid}/tasks | Get tasks from a user task list
[**remove_dependencies_for_task**](TasksApi.md#remove_dependencies_for_task) | **POST** /tasks/{task_gid}/removeDependencies | Unlink dependencies from a task
[**remove_dependents_for_task**](TasksApi.md#remove_dependents_for_task) | **POST** /tasks/{task_gid}/removeDependents | Unlink dependents from a task
[**remove_follower_for_task**](TasksApi.md#remove_follower_for_task) | **POST** /tasks/{task_gid}/removeFollowers | Remove followers from a task
[**remove_project_for_task**](TasksApi.md#remove_project_for_task) | **POST** /tasks/{task_gid}/removeProject | Remove a project from a task
[**remove_tag_for_task**](TasksApi.md#remove_tag_for_task) | **POST** /tasks/{task_gid}/removeTag | Remove a tag from a task
[**search_tasks_for_workspace**](TasksApi.md#search_tasks_for_workspace) | **GET** /workspaces/{workspace_gid}/tasks/search | Search tasks in a workspace
[**set_parent_for_task**](TasksApi.md#set_parent_for_task) | **POST** /tasks/{task_gid}/setParent | Set the parent of a task
[**update_task**](TasksApi.md#update_task) | **PUT** /tasks/{task_gid} | Update a task


# **add_dependencies_for_task**
> DeleteAllocation200Response add_dependencies_for_task(task_gid, add_dependencies_for_task_request, opt_pretty=opt_pretty)

Set dependencies for a task

<b>Required scope: </b><code>tasks:write</code>

Marks a set of tasks as dependencies of this task, if they are not already dependencies. *A task can have at most 30 dependents and dependencies combined*.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_dependencies_for_task_request import AddDependenciesForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    add_dependencies_for_task_request = asana_asyncio.AddDependenciesForTaskRequest() # AddDependenciesForTaskRequest | The list of tasks to set as dependencies.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Set dependencies for a task
        api_response = await api_instance.add_dependencies_for_task(task_gid, add_dependencies_for_task_request, opt_pretty=opt_pretty)
        print("The response of TasksApi->add_dependencies_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->add_dependencies_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **add_dependencies_for_task_request** | [**AddDependenciesForTaskRequest**](AddDependenciesForTaskRequest.md)| The list of tasks to set as dependencies. | 
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
**200** | Successfully set the specified dependencies on the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dependents_for_task**
> DeleteAllocation200Response add_dependents_for_task(task_gid, add_dependents_for_task_request, opt_pretty=opt_pretty)

Set dependents for a task

<b>Required scope: </b><code>tasks:write</code>

Marks a set of tasks as dependents of this task, if they are not already dependents. *A task can have at most 30 dependents and dependencies combined*.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_dependents_for_task_request import AddDependentsForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    add_dependents_for_task_request = asana_asyncio.AddDependentsForTaskRequest() # AddDependentsForTaskRequest | The list of tasks to add as dependents.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Set dependents for a task
        api_response = await api_instance.add_dependents_for_task(task_gid, add_dependents_for_task_request, opt_pretty=opt_pretty)
        print("The response of TasksApi->add_dependents_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->add_dependents_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **add_dependents_for_task_request** | [**AddDependentsForTaskRequest**](AddDependentsForTaskRequest.md)| The list of tasks to add as dependents. | 
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
**200** | Successfully set the specified dependents on the given task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_followers_for_task**
> CreateTask201Response add_followers_for_task(task_gid, add_followers_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Add followers to a task

<b>Required scope: </b><code>tasks:write</code>

Adds followers to a task. Returns an empty data block.
Each task can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated task record, described above.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_followers_request import AddFollowersRequest
from asana_asyncio.models.create_task201_response import CreateTask201Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    add_followers_request = asana_asyncio.AddFollowersRequest() # AddFollowersRequest | The followers to add to the task.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Add followers to a task
        api_response = await api_instance.add_followers_for_task(task_gid, add_followers_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of TasksApi->add_followers_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->add_followers_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **add_followers_request** | [**AddFollowersRequest**](AddFollowersRequest.md)| The followers to add to the task. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added the specified followers to the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_for_task**
> DeleteAllocation200Response add_project_for_task(task_gid, add_project_for_task_request, opt_pretty=opt_pretty)

Add a project to a task

<b>Required scope: </b><code>tasks:write</code>

Adds the task to the specified project, in the optional location
specified. If no location arguments are given, the task will be added to
the end of the project.

`addProject` can also be used to reorder a task within a project or
section that already contains it.

At most one of `insert_before`, `insert_after`, or `section` should be
specified. Inserting into a section in an non-order-dependent way can be
done by specifying section, otherwise, to insert within a section in a
particular place, specify `insert_before` or `insert_after` and a task
within the section to anchor the position of this task.

A task can have at most 20 projects multi-homed to it.

Returns an empty data block.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_project_for_task_request import AddProjectForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    add_project_for_task_request = asana_asyncio.AddProjectForTaskRequest() # AddProjectForTaskRequest | The project to add the task to.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Add a project to a task
        api_response = await api_instance.add_project_for_task(task_gid, add_project_for_task_request, opt_pretty=opt_pretty)
        print("The response of TasksApi->add_project_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->add_project_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **add_project_for_task_request** | [**AddProjectForTaskRequest**](AddProjectForTaskRequest.md)| The project to add the task to. | 
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
**200** | Successfully added the specified project to the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tag_for_task**
> DeleteAllocation200Response add_tag_for_task(task_gid, add_tag_for_task_request, opt_pretty=opt_pretty)

Add a tag to a task

<b>Required scope: </b><code>tasks:write</code>

Adds a tag to a task. Returns an empty data block.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_tag_for_task_request import AddTagForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    add_tag_for_task_request = asana_asyncio.AddTagForTaskRequest() # AddTagForTaskRequest | The tag to add to the task.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Add a tag to a task
        api_response = await api_instance.add_tag_for_task(task_gid, add_tag_for_task_request, opt_pretty=opt_pretty)
        print("The response of TasksApi->add_tag_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->add_tag_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **add_tag_for_task_request** | [**AddTagForTaskRequest**](AddTagForTaskRequest.md)| The tag to add to the task. | 
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
**200** | Successfully added the specified tag to the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subtask_for_task**
> CreateTask201Response create_subtask_for_task(task_gid, create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a subtask

<b>Required scope: </b><code>tasks:write</code>

Creates a new subtask and adds it to the parent task. Returns the full record for the newly created subtask.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_task201_response import CreateTask201Response
from asana_asyncio.models.create_task_request import CreateTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    create_task_request = asana_asyncio.CreateTaskRequest() # CreateTaskRequest | The new subtask to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a subtask
        api_response = await api_instance.create_subtask_for_task(task_gid, create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of TasksApi->create_subtask_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_subtask_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| The new subtask to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the specified subtask. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> CreateTask201Response create_task(create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a task

<b>Required scope: </b><code>tasks:write</code>

Creating a new task is as easy as POSTing to the `/tasks` endpoint with a
data block containing the fields you’d like to set on the task. Any
unspecified fields will take on default values.

Every task is required to be created in a specific workspace, and this
workspace cannot be changed once set. The workspace need not be set
explicitly if you specify `projects` or a `parent` task instead.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_task201_response import CreateTask201Response
from asana_asyncio.models.create_task_request import CreateTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    create_task_request = asana_asyncio.CreateTaskRequest() # CreateTaskRequest | The task to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a task
        api_response = await api_instance.create_task(create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of TasksApi->create_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| The task to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> DeleteAllocation200Response delete_task(task_gid, opt_pretty=opt_pretty)

Delete a task

<b>Required scope: </b><code>tasks:delete</code>

A specific, existing task can be deleted by making a DELETE request on
the URL for that task. Deleted tasks go into the “trash” of the user
making the delete request. Tasks can be recovered from the trash within a
period of 30 days; afterward they are completely removed from the system.

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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a task
        api_response = await api_instance.delete_task(task_gid, opt_pretty=opt_pretty)
        print("The response of TasksApi->delete_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->delete_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
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
**200** | Successfully deleted the specified task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_task**
> GetJob200Response duplicate_task(task_gid, duplicate_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Duplicate a task

<b>Required scope: </b><code>tasks:write</code>

Creates and returns a job that will asynchronously handle the duplication.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.duplicate_task_request import DuplicateTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    duplicate_task_request = asana_asyncio.DuplicateTaskRequest() # DuplicateTaskRequest | Describes the duplicate's name and the fields that will be duplicated.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"new_graph_export\",\"new_graph_export.completed_at\",\"new_graph_export.created_at\",\"new_graph_export.download_url\",\"new_project\",\"new_project.name\",\"new_project_template\",\"new_project_template.name\",\"new_resource_export\",\"new_task\",\"new_task.created_by\",\"new_task.name\",\"new_task.resource_subtype\",\"new_task_template\",\"new_task_template.name\",\"resource_subtype\",\"status\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Duplicate a task
        api_response = await api_instance.duplicate_task(task_gid, duplicate_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of TasksApi->duplicate_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->duplicate_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **duplicate_task_request** | [**DuplicateTaskRequest**](DuplicateTaskRequest.md)| Describes the duplicate&#39;s name and the fields that will be duplicated. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

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

# **get_dependencies_for_task**
> GetTasks200Response get_dependencies_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get dependencies from a task

<b>Required scope: </b><code>tasks:read</code>

Returns the compact representations of all of the dependencies of a task.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_tasks200_response import GetTasks200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"offset\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"path\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get dependencies from a task
        api_response = await api_instance.get_dependencies_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of TasksApi->get_dependencies_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_dependencies_for_task: %s\n" % e)
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

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified task&#39;s dependencies. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependents_for_task**
> GetTasks200Response get_dependents_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get dependents from a task

<b>Required scope: </b><code>tasks:read</code>

Returns the compact representations of all of the dependents of a task.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_tasks200_response import GetTasks200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"offset\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"path\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get dependents from a task
        api_response = await api_instance.get_dependents_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of TasksApi->get_dependents_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_dependents_for_task: %s\n" % e)
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

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified dependents of the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtasks_for_task**
> GetTasks200Response get_subtasks_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get subtasks from a task

<b>Required scope: </b><code>tasks:read</code>

Returns a compact representation of all of the subtasks of a task.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_tasks200_response import GetTasks200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"offset\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"path\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get subtasks from a task
        api_response = await api_instance.get_subtasks_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of TasksApi->get_subtasks_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_subtasks_for_task: %s\n" % e)
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

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified task&#39;s subtasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> CreateTask201Response get_task(task_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a task

<b>Required scope: </b><code>tasks:read</code>

<table>
  <tr>
    <th>Field</th>
    <th>Required Scope</th>
  </tr>
  <tr>
    <td><code>memberships</code></td>
    <td><code>projects:read</code>, <code>project_sections:read</code></td>
  </tr>
  <tr>
    <td><code>actual_time_minutes</code></td>
    <td><code>time_tracking_entries:read</code></td>
  </tr>
  <tr>
    <td><code>custom_fields</code></td>
    <td><code>custom_fields:read</code></td>
  </tr>
</table>

Returns the complete task record for a single task.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_task201_response import CreateTask201Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a task
        api_response = await api_instance.get_task(task_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of TasksApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_for_custom_id**
> CreateTask201Response get_task_for_custom_id(workspace_gid, custom_id)

Get a task for a given custom ID

<b>Required scope: </b><code>tasks:read</code>

<table>
  <tr>
    <th>Field</th>
    <th>Required Scope</th>
  </tr>
  <tr>
    <td><code>memberships</code></td>
    <td><code>projects:read</code>, <code>project_sections:read</code></td>
  </tr>
  <tr>
    <td><code>actual_time_minutes</code></td>
    <td><code>time_tracking_entries:read</code></td>
  </tr>
  <tr>
    <td><code>custom_fields</code></td>
    <td><code>custom_fields:read</code></td>
  </tr>
</table>

Returns a task given a custom ID shortcode.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_task201_response import CreateTask201Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
    custom_id = 'EX-1' # str | Generated custom ID for a task.

    try:
        # Get a task for a given custom ID
        api_response = await api_instance.get_task_for_custom_id(workspace_gid, custom_id)
        print("The response of TasksApi->get_task_for_custom_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_for_custom_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **custom_id** | **str**| Generated custom ID for a task. | 

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved task for given custom ID. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> GetTasks200Response get_tasks(opt_pretty=opt_pretty, limit=limit, offset=offset, assignee=assignee, project=project, section=section, workspace=workspace, completed_since=completed_since, modified_since=modified_since, opt_fields=opt_fields)

Get multiple tasks

<b>Required scope: </b><code>tasks:read</code>

Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.

For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/reference/searchtasksforworkspace).

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_tasks200_response import GetTasks200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    assignee = '14641' # str | The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified. *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.* (optional)
    project = '321654' # str | The project to filter tasks on. (optional)
    section = '321654' # str | The section to filter tasks on. (optional)
    workspace = '321654' # str | The workspace to filter tasks on. *Note: If you specify `workspace`, you must also specify the `assignee` to filter on.* (optional)
    completed_since = '2012-02-22T02:06:58.158Z' # datetime | Only return tasks that are either incomplete or that have been completed since this time. (optional)
    modified_since = '2012-02-22T02:06:58.158Z' # datetime | Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.* (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"offset\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"path\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get multiple tasks
        api_response = await api_instance.get_tasks(opt_pretty=opt_pretty, limit=limit, offset=offset, assignee=assignee, project=project, section=section, workspace=workspace, completed_since=completed_since, modified_since=modified_since, opt_fields=opt_fields)
        print("The response of TasksApi->get_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **assignee** | **str**| The assignee to filter tasks on. If searching for unassigned tasks, assignee.any &#x3D; null can be specified. *Note: If you specify &#x60;assignee&#x60;, you must also specify the &#x60;workspace&#x60; to filter on.* | [optional] 
 **project** | **str**| The project to filter tasks on. | [optional] 
 **section** | **str**| The section to filter tasks on. | [optional] 
 **workspace** | **str**| The workspace to filter tasks on. *Note: If you specify &#x60;workspace&#x60;, you must also specify the &#x60;assignee&#x60; to filter on.* | [optional] 
 **completed_since** | **datetime**| Only return tasks that are either incomplete or that have been completed since this time. | [optional] 
 **modified_since** | **datetime**| Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.* | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved requested tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_project**
> GetTasks200Response get_tasks_for_project(project_gid, completed_since=completed_since, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get tasks from a project

<b>Required scope: </b><code>tasks:read</code>

Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_tasks200_response import GetTasks200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    project_gid = '1331' # str | Globally unique identifier for the project.
    completed_since = '2012-02-22T02:06:58.158Z' # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  (optional)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"offset\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"path\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get tasks from a project
        api_response = await api_instance.get_tasks_for_project(project_gid, completed_since=completed_since, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of TasksApi->get_tasks_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  | [optional] 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested project&#39;s tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_section**
> GetTasks200Response get_tasks_for_section(section_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, completed_since=completed_since, opt_fields=opt_fields)

Get tasks from a section

<b>Required scope: </b><code>tasks:read</code>

*Board view only*: Returns the compact section records for all tasks within the given section.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_tasks200_response import GetTasks200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    section_gid = '321654' # str | The globally unique identifier for the section.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    completed_since = '2012-02-22T02:06:58.158Z' # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"offset\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"path\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get tasks from a section
        api_response = await api_instance.get_tasks_for_section(section_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, completed_since=completed_since, opt_fields=opt_fields)
        print("The response of TasksApi->get_tasks_for_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks_for_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_gid** | **str**| The globally unique identifier for the section. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the section&#39;s tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_tag**
> GetTasks200Response get_tasks_for_tag(tag_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get tasks from a tag

<b>Required scope: </b><code>tasks:read</code>

Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_tasks200_response import GetTasks200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    tag_gid = '11235' # str | Globally unique identifier for the tag.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"offset\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"path\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get tasks from a tag
        api_response = await api_instance.get_tasks_for_tag(tag_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of TasksApi->get_tasks_for_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks_for_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_gid** | **str**| Globally unique identifier for the tag. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the tasks associated with the specified tag. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_user_task_list**
> GetTasks200Response get_tasks_for_user_task_list(user_task_list_gid, completed_since=completed_since, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get tasks from a user task list

<b>Required scope: </b><code>tasks:read</code>

Returns the compact list of tasks in a user’s My Tasks list.
*Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.*
*Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting `completed_since=now` will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_tasks200_response import GetTasks200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    user_task_list_gid = '12345' # str | Globally unique identifier for the user task list.
    completed_since = '2012-02-22T02:06:58.158Z' # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  (optional)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"offset\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"path\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get tasks from a user task list
        api_response = await api_instance.get_tasks_for_user_task_list(user_task_list_gid, completed_since=completed_since, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of TasksApi->get_tasks_for_user_task_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks_for_user_task_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_task_list_gid** | **str**| Globally unique identifier for the user task list. | 
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  | [optional] 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetTasks200Response**](GetTasks200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the user task list&#39;s tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dependencies_for_task**
> DeleteAllocation200Response remove_dependencies_for_task(task_gid, add_dependencies_for_task_request, opt_pretty=opt_pretty)

Unlink dependencies from a task

<b>Required scope: </b><code>tasks:write</code>

Unlinks a set of dependencies from this task.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_dependencies_for_task_request import AddDependenciesForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    add_dependencies_for_task_request = asana_asyncio.AddDependenciesForTaskRequest() # AddDependenciesForTaskRequest | The list of tasks to unlink as dependencies.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Unlink dependencies from a task
        api_response = await api_instance.remove_dependencies_for_task(task_gid, add_dependencies_for_task_request, opt_pretty=opt_pretty)
        print("The response of TasksApi->remove_dependencies_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->remove_dependencies_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **add_dependencies_for_task_request** | [**AddDependenciesForTaskRequest**](AddDependenciesForTaskRequest.md)| The list of tasks to unlink as dependencies. | 
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
**200** | Successfully unlinked the dependencies from the specified task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dependents_for_task**
> DeleteAllocation200Response remove_dependents_for_task(task_gid, add_dependents_for_task_request, opt_pretty=opt_pretty)

Unlink dependents from a task

<b>Required scope: </b><code>tasks:write</code>

Unlinks a set of dependents from this task.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_dependents_for_task_request import AddDependentsForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    add_dependents_for_task_request = asana_asyncio.AddDependentsForTaskRequest() # AddDependentsForTaskRequest | The list of tasks to remove as dependents.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Unlink dependents from a task
        api_response = await api_instance.remove_dependents_for_task(task_gid, add_dependents_for_task_request, opt_pretty=opt_pretty)
        print("The response of TasksApi->remove_dependents_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->remove_dependents_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **add_dependents_for_task_request** | [**AddDependentsForTaskRequest**](AddDependentsForTaskRequest.md)| The list of tasks to remove as dependents. | 
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
**200** | Successfully unlinked the specified tasks as dependents. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_follower_for_task**
> CreateTask201Response remove_follower_for_task(task_gid, remove_follower_for_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Remove followers from a task

<b>Required scope: </b><code>tasks:write</code>

Removes each of the specified followers from the task if they are following. Returns the complete, updated record for the affected task.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_task201_response import CreateTask201Response
from asana_asyncio.models.remove_follower_for_task_request import RemoveFollowerForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    remove_follower_for_task_request = asana_asyncio.RemoveFollowerForTaskRequest() # RemoveFollowerForTaskRequest | The followers to remove from the task.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Remove followers from a task
        api_response = await api_instance.remove_follower_for_task(task_gid, remove_follower_for_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of TasksApi->remove_follower_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->remove_follower_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **remove_follower_for_task_request** | [**RemoveFollowerForTaskRequest**](RemoveFollowerForTaskRequest.md)| The followers to remove from the task. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the specified followers from the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_for_task**
> DeleteAllocation200Response remove_project_for_task(task_gid, remove_project_for_task_request, opt_pretty=opt_pretty)

Remove a project from a task

<b>Required scope: </b><code>tasks:write</code>

Removes the task from the specified project. The task will still exist in
the system, but it will not be in the project anymore.

Returns an empty data block.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.delete_allocation200_response import DeleteAllocation200Response
from asana_asyncio.models.remove_project_for_task_request import RemoveProjectForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    remove_project_for_task_request = asana_asyncio.RemoveProjectForTaskRequest() # RemoveProjectForTaskRequest | The project to remove the task from.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Remove a project from a task
        api_response = await api_instance.remove_project_for_task(task_gid, remove_project_for_task_request, opt_pretty=opt_pretty)
        print("The response of TasksApi->remove_project_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->remove_project_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **remove_project_for_task_request** | [**RemoveProjectForTaskRequest**](RemoveProjectForTaskRequest.md)| The project to remove the task from. | 
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
**200** | Successfully removed the specified project from the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tag_for_task**
> DeleteAllocation200Response remove_tag_for_task(task_gid, remove_tag_for_task_request, opt_pretty=opt_pretty)

Remove a tag from a task

<b>Required scope: </b><code>tasks:write</code>

Removes a tag from a task. Returns an empty data block.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.delete_allocation200_response import DeleteAllocation200Response
from asana_asyncio.models.remove_tag_for_task_request import RemoveTagForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    remove_tag_for_task_request = asana_asyncio.RemoveTagForTaskRequest() # RemoveTagForTaskRequest | The tag to remove from the task.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Remove a tag from a task
        api_response = await api_instance.remove_tag_for_task(task_gid, remove_tag_for_task_request, opt_pretty=opt_pretty)
        print("The response of TasksApi->remove_tag_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->remove_tag_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **remove_tag_for_task_request** | [**RemoveTagForTaskRequest**](RemoveTagForTaskRequest.md)| The tag to remove from the task. | 
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
**200** | Successfully removed the specified tag from the task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tasks_for_workspace**
> SearchTasksForWorkspace200Response search_tasks_for_workspace(workspace_gid, opt_pretty=opt_pretty, text=text, resource_subtype=resource_subtype, assignee_any=assignee_any, assignee_not=assignee_not, portfolios_any=portfolios_any, projects_any=projects_any, projects_not=projects_not, projects_all=projects_all, sections_any=sections_any, sections_not=sections_not, sections_all=sections_all, tags_any=tags_any, tags_not=tags_not, tags_all=tags_all, teams_any=teams_any, followers_any=followers_any, followers_not=followers_not, created_by_any=created_by_any, created_by_not=created_by_not, assigned_by_any=assigned_by_any, assigned_by_not=assigned_by_not, liked_by_not=liked_by_not, commented_on_by_not=commented_on_by_not, due_on_before=due_on_before, due_on_after=due_on_after, due_on=due_on, due_at_before=due_at_before, due_at_after=due_at_after, start_on_before=start_on_before, start_on_after=start_on_after, start_on=start_on, created_on_before=created_on_before, created_on_after=created_on_after, created_on=created_on, created_at_before=created_at_before, created_at_after=created_at_after, completed_on_before=completed_on_before, completed_on_after=completed_on_after, completed_on=completed_on, completed_at_before=completed_at_before, completed_at_after=completed_at_after, modified_on_before=modified_on_before, modified_on_after=modified_on_after, modified_on=modified_on, modified_at_before=modified_at_before, modified_at_after=modified_at_after, is_blocking=is_blocking, is_blocked=is_blocked, has_attachment=has_attachment, completed=completed, is_subtask=is_subtask, sort_by=sort_by, sort_ascending=sort_ascending, opt_fields=opt_fields)

Search tasks in a workspace

<b>Required scope: </b><code>tasks:read</code>

To mirror the functionality of the Asana web app's advanced search feature, the Asana API has a task search endpoint that allows you to build complex filters to find and retrieve the exact data you need.
#### Premium access
Like the Asana web product's advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:

- The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace

Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error.
#### Pagination
Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](https://developers.asana.com/docs/#pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter.
#### Eventual consistency
Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a task that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product.
#### Rate limits
You may receive a `429 Too Many Requests` response if you hit any of our [rate limits](https://developers.asana.com/docs/#rate-limits).
#### Custom field parameters
| Parameter name | Custom field type | Accepted type |
|---|---|---|
| custom_fields.{gid}.is_set | All | Boolean |
| custom_fields.{gid}.value | Text | String |
| custom_fields.{gid}.value | Number | Number |
| custom_fields.{gid}.value | Enum | Enum option ID |
| custom_fields.{gid}.starts_with | Text only | String |
| custom_fields.{gid}.ends_with | Text only | String |
| custom_fields.{gid}.contains | Text only | String |
| custom_fields.{gid}.less_than | Number only | Number |
| custom_fields.{gid}.greater_than | Number only | Number |


For example, if the gid of the custom field is 12345, these query parameter to find tasks where it is set would be `custom_fields.12345.is_set=true`. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: `custom_fields.12345.value=67890`.

**Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field

*Note: If you specify `projects.any` and `sections.any`, you will receive tasks for the project **and** tasks for the section. If you're looking for only tasks in a section, omit the `projects.any` from the request.*

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.search_tasks_for_workspace200_response import SearchTasksForWorkspace200Response
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
    api_instance = asana_asyncio.TasksApi(api_client)
    workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    text = 'Bug' # str | Performs full-text search on both task name and description (optional)
    resource_subtype = milestone # str | Filters results by the task's resource_subtype (optional) (default to milestone)
    assignee_any = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    assignee_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    portfolios_any = '12345,23456,34567' # str | Comma-separated list of portfolio IDs (optional)
    projects_any = '12345,23456,34567' # str | Comma-separated list of project IDs (optional)
    projects_not = '12345,23456,34567' # str | Comma-separated list of project IDs (optional)
    projects_all = '12345,23456,34567' # str | Comma-separated list of project IDs (optional)
    sections_any = '12345,23456,34567' # str | Comma-separated list of section or column IDs (optional)
    sections_not = '12345,23456,34567' # str | Comma-separated list of section or column IDs (optional)
    sections_all = '12345,23456,34567' # str | Comma-separated list of section or column IDs (optional)
    tags_any = '12345,23456,34567' # str | Comma-separated list of tag IDs (optional)
    tags_not = '12345,23456,34567' # str | Comma-separated list of tag IDs (optional)
    tags_all = '12345,23456,34567' # str | Comma-separated list of tag IDs (optional)
    teams_any = '12345,23456,34567' # str | Comma-separated list of team IDs (optional)
    followers_any = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    followers_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    created_by_any = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    created_by_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    assigned_by_any = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    assigned_by_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    liked_by_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    commented_on_by_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
    due_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
    due_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
    due_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
    due_at_before = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
    due_at_after = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
    start_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
    start_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
    start_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
    created_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
    created_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
    created_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
    created_at_before = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
    created_at_after = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
    completed_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
    completed_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
    completed_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
    completed_at_before = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
    completed_at_after = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
    modified_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
    modified_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
    modified_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
    modified_at_before = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
    modified_at_after = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
    is_blocking = false # bool | Filter to incomplete tasks with dependents (optional)
    is_blocked = false # bool | Filter to tasks with incomplete dependencies (optional)
    has_attachment = false # bool | Filter to tasks with attachments (optional)
    completed = false # bool | Filter to completed tasks (optional)
    is_subtask = false # bool | Filter to subtasks (optional)
    sort_by = modified_at # str | One of `due_date`, `created_at`, `completed_at`, `likes`, or `modified_at`, defaults to `modified_at` (optional) (default to modified_at)
    sort_ascending = False # bool | Default `false` (optional) (default to False)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Search tasks in a workspace
        api_response = await api_instance.search_tasks_for_workspace(workspace_gid, opt_pretty=opt_pretty, text=text, resource_subtype=resource_subtype, assignee_any=assignee_any, assignee_not=assignee_not, portfolios_any=portfolios_any, projects_any=projects_any, projects_not=projects_not, projects_all=projects_all, sections_any=sections_any, sections_not=sections_not, sections_all=sections_all, tags_any=tags_any, tags_not=tags_not, tags_all=tags_all, teams_any=teams_any, followers_any=followers_any, followers_not=followers_not, created_by_any=created_by_any, created_by_not=created_by_not, assigned_by_any=assigned_by_any, assigned_by_not=assigned_by_not, liked_by_not=liked_by_not, commented_on_by_not=commented_on_by_not, due_on_before=due_on_before, due_on_after=due_on_after, due_on=due_on, due_at_before=due_at_before, due_at_after=due_at_after, start_on_before=start_on_before, start_on_after=start_on_after, start_on=start_on, created_on_before=created_on_before, created_on_after=created_on_after, created_on=created_on, created_at_before=created_at_before, created_at_after=created_at_after, completed_on_before=completed_on_before, completed_on_after=completed_on_after, completed_on=completed_on, completed_at_before=completed_at_before, completed_at_after=completed_at_after, modified_on_before=modified_on_before, modified_on_after=modified_on_after, modified_on=modified_on, modified_at_before=modified_at_before, modified_at_after=modified_at_after, is_blocking=is_blocking, is_blocked=is_blocked, has_attachment=has_attachment, completed=completed, is_subtask=is_subtask, sort_by=sort_by, sort_ascending=sort_ascending, opt_fields=opt_fields)
        print("The response of TasksApi->search_tasks_for_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->search_tasks_for_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **text** | **str**| Performs full-text search on both task name and description | [optional] 
 **resource_subtype** | **str**| Filters results by the task&#39;s resource_subtype | [optional] [default to milestone]
 **assignee_any** | **str**| Comma-separated list of user identifiers | [optional] 
 **assignee_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **portfolios_any** | **str**| Comma-separated list of portfolio IDs | [optional] 
 **projects_any** | **str**| Comma-separated list of project IDs | [optional] 
 **projects_not** | **str**| Comma-separated list of project IDs | [optional] 
 **projects_all** | **str**| Comma-separated list of project IDs | [optional] 
 **sections_any** | **str**| Comma-separated list of section or column IDs | [optional] 
 **sections_not** | **str**| Comma-separated list of section or column IDs | [optional] 
 **sections_all** | **str**| Comma-separated list of section or column IDs | [optional] 
 **tags_any** | **str**| Comma-separated list of tag IDs | [optional] 
 **tags_not** | **str**| Comma-separated list of tag IDs | [optional] 
 **tags_all** | **str**| Comma-separated list of tag IDs | [optional] 
 **teams_any** | **str**| Comma-separated list of team IDs | [optional] 
 **followers_any** | **str**| Comma-separated list of user identifiers | [optional] 
 **followers_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **created_by_any** | **str**| Comma-separated list of user identifiers | [optional] 
 **created_by_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **assigned_by_any** | **str**| Comma-separated list of user identifiers | [optional] 
 **assigned_by_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **liked_by_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **commented_on_by_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **due_on_before** | **date**| ISO 8601 date string | [optional] 
 **due_on_after** | **date**| ISO 8601 date string | [optional] 
 **due_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **due_at_before** | **datetime**| ISO 8601 datetime string | [optional] 
 **due_at_after** | **datetime**| ISO 8601 datetime string | [optional] 
 **start_on_before** | **date**| ISO 8601 date string | [optional] 
 **start_on_after** | **date**| ISO 8601 date string | [optional] 
 **start_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **created_on_before** | **date**| ISO 8601 date string | [optional] 
 **created_on_after** | **date**| ISO 8601 date string | [optional] 
 **created_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **created_at_before** | **datetime**| ISO 8601 datetime string | [optional] 
 **created_at_after** | **datetime**| ISO 8601 datetime string | [optional] 
 **completed_on_before** | **date**| ISO 8601 date string | [optional] 
 **completed_on_after** | **date**| ISO 8601 date string | [optional] 
 **completed_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **completed_at_before** | **datetime**| ISO 8601 datetime string | [optional] 
 **completed_at_after** | **datetime**| ISO 8601 datetime string | [optional] 
 **modified_on_before** | **date**| ISO 8601 date string | [optional] 
 **modified_on_after** | **date**| ISO 8601 date string | [optional] 
 **modified_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **modified_at_before** | **datetime**| ISO 8601 datetime string | [optional] 
 **modified_at_after** | **datetime**| ISO 8601 datetime string | [optional] 
 **is_blocking** | **bool**| Filter to incomplete tasks with dependents | [optional] 
 **is_blocked** | **bool**| Filter to tasks with incomplete dependencies | [optional] 
 **has_attachment** | **bool**| Filter to tasks with attachments | [optional] 
 **completed** | **bool**| Filter to completed tasks | [optional] 
 **is_subtask** | **bool**| Filter to subtasks | [optional] 
 **sort_by** | **str**| One of &#x60;due_date&#x60;, &#x60;created_at&#x60;, &#x60;completed_at&#x60;, &#x60;likes&#x60;, or &#x60;modified_at&#x60;, defaults to &#x60;modified_at&#x60; | [optional] [default to modified_at]
 **sort_ascending** | **bool**| Default &#x60;false&#x60; | [optional] [default to False]
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**SearchTasksForWorkspace200Response**](SearchTasksForWorkspace200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the section&#39;s tasks. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parent_for_task**
> CreateTask201Response set_parent_for_task(task_gid, set_parent_for_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Set the parent of a task

<b>Required scope: </b><code>tasks:write</code>

parent, or no parent task at all. Returns an empty data block. When using `insert_before` and `insert_after`, at most one of those two options can be specified, and they must already be subtasks of the parent.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_task201_response import CreateTask201Response
from asana_asyncio.models.set_parent_for_task_request import SetParentForTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    set_parent_for_task_request = asana_asyncio.SetParentForTaskRequest() # SetParentForTaskRequest | The new parent of the subtask.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Set the parent of a task
        api_response = await api_instance.set_parent_for_task(task_gid, set_parent_for_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of TasksApi->set_parent_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->set_parent_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **set_parent_for_task_request** | [**SetParentForTaskRequest**](SetParentForTaskRequest.md)| The new parent of the subtask. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully changed the parent of the specified subtask. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> CreateTask201Response update_task(task_gid, create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Update a task

<b>Required scope: </b><code>tasks:write</code>

A specific, existing task can be updated by making a PUT request on the
URL for that task. Only the fields provided in the `data` block will be
updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated task record.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_task201_response import CreateTask201Response
from asana_asyncio.models.create_task_request import CreateTaskRequest
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
    api_instance = asana_asyncio.TasksApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    create_task_request = asana_asyncio.CreateTaskRequest() # CreateTaskRequest | The task to update.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"actual_time_minutes\",\"approval_status\",\"assignee\",\"assignee.name\",\"assignee_section\",\"assignee_section.name\",\"assignee_status\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_by\",\"custom_fields\",\"custom_fields.asana_created_field\",\"custom_fields.created_by\",\"custom_fields.created_by.name\",\"custom_fields.currency_code\",\"custom_fields.custom_label\",\"custom_fields.custom_label_position\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.default_access_level\",\"custom_fields.description\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.format\",\"custom_fields.has_notifications_enabled\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.is_global_to_workspace\",\"custom_fields.is_value_read_only\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.people_value\",\"custom_fields.people_value.name\",\"custom_fields.precision\",\"custom_fields.privacy_setting\",\"custom_fields.representation_type\",\"custom_fields.resource_subtype\",\"custom_fields.text_value\",\"custom_fields.type\",\"custom_type\",\"custom_type.name\",\"custom_type_status_option\",\"custom_type_status_option.name\",\"dependencies\",\"dependents\",\"due_at\",\"due_on\",\"external\",\"external.data\",\"followers\",\"followers.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_notes\",\"is_rendered_as_separator\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"memberships\",\"memberships.project\",\"memberships.project.name\",\"memberships.section\",\"memberships.section.name\",\"modified_at\",\"name\",\"notes\",\"num_hearts\",\"num_likes\",\"num_subtasks\",\"parent\",\"parent.created_by\",\"parent.name\",\"parent.resource_subtype\",\"permalink_url\",\"projects\",\"projects.name\",\"resource_subtype\",\"start_at\",\"start_on\",\"tags\",\"tags.name\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Update a task
        api_response = await api_instance.update_task(task_gid, create_task_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of TasksApi->update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| The task to update. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreateTask201Response**](CreateTask201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the specified task. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

