# asana_asyncio.StoriesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_story_for_task**](StoriesApi.md#create_story_for_task) | **POST** /tasks/{task_gid}/stories | Create a story on a task
[**delete_story**](StoriesApi.md#delete_story) | **DELETE** /stories/{story_gid} | Delete a story
[**get_stories_for_task**](StoriesApi.md#get_stories_for_task) | **GET** /tasks/{task_gid}/stories | Get stories from a task
[**get_story**](StoriesApi.md#get_story) | **GET** /stories/{story_gid} | Get a story
[**update_story**](StoriesApi.md#update_story) | **PUT** /stories/{story_gid} | Update a story


# **create_story_for_task**
> GetStory200Response create_story_for_task(task_gid, update_story_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a story on a task

Adds a story to a task. This endpoint currently only allows for comment stories to be created. The comment will be authored by the currently authenticated user, and timestamped when the server receives the request.  Returns the full record for the new story added to the task.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_story200_response import GetStory200Response
from asana_asyncio.models.update_story_request import UpdateStoryRequest
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
    api_instance = asana_asyncio.StoriesApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    update_story_request = asana_asyncio.UpdateStoryRequest() # UpdateStoryRequest | The story to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"assignee\",\"assignee.name\",\"created_at\",\"created_by\",\"created_by.name\",\"custom_field\",\"custom_field.date_value\",\"custom_field.date_value.date\",\"custom_field.date_value.date_time\",\"custom_field.display_value\",\"custom_field.enabled\",\"custom_field.enum_options\",\"custom_field.enum_options.color\",\"custom_field.enum_options.enabled\",\"custom_field.enum_options.name\",\"custom_field.enum_value\",\"custom_field.enum_value.color\",\"custom_field.enum_value.enabled\",\"custom_field.enum_value.name\",\"custom_field.id_prefix\",\"custom_field.is_formula_field\",\"custom_field.multi_enum_values\",\"custom_field.multi_enum_values.color\",\"custom_field.multi_enum_values.enabled\",\"custom_field.multi_enum_values.name\",\"custom_field.name\",\"custom_field.number_value\",\"custom_field.representation_type\",\"custom_field.resource_subtype\",\"custom_field.text_value\",\"custom_field.type\",\"dependency\",\"dependency.created_by\",\"dependency.name\",\"dependency.resource_subtype\",\"duplicate_of\",\"duplicate_of.created_by\",\"duplicate_of.name\",\"duplicate_of.resource_subtype\",\"duplicated_from\",\"duplicated_from.created_by\",\"duplicated_from.name\",\"duplicated_from.resource_subtype\",\"follower\",\"follower.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_text\",\"is_editable\",\"is_edited\",\"is_pinned\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"new_approval_status\",\"new_date_value\",\"new_dates\",\"new_dates.due_at\",\"new_dates.due_on\",\"new_dates.start_on\",\"new_enum_value\",\"new_enum_value.color\",\"new_enum_value.enabled\",\"new_enum_value.name\",\"new_multi_enum_values\",\"new_multi_enum_values.color\",\"new_multi_enum_values.enabled\",\"new_multi_enum_values.name\",\"new_name\",\"new_number_value\",\"new_people_value\",\"new_people_value.name\",\"new_resource_subtype\",\"new_section\",\"new_section.name\",\"new_text_value\",\"num_hearts\",\"num_likes\",\"old_approval_status\",\"old_date_value\",\"old_dates\",\"old_dates.due_at\",\"old_dates.due_on\",\"old_dates.start_on\",\"old_enum_value\",\"old_enum_value.color\",\"old_enum_value.enabled\",\"old_enum_value.name\",\"old_multi_enum_values\",\"old_multi_enum_values.color\",\"old_multi_enum_values.enabled\",\"old_multi_enum_values.name\",\"old_name\",\"old_number_value\",\"old_people_value\",\"old_people_value.name\",\"old_resource_subtype\",\"old_section\",\"old_section.name\",\"old_text_value\",\"previews\",\"previews.fallback\",\"previews.footer\",\"previews.header\",\"previews.header_link\",\"previews.html_text\",\"previews.text\",\"previews.title\",\"previews.title_link\",\"project\",\"project.name\",\"resource_subtype\",\"source\",\"sticker_name\",\"story\",\"story.created_at\",\"story.created_by\",\"story.created_by.name\",\"story.resource_subtype\",\"story.text\",\"tag\",\"tag.name\",\"target\",\"target.created_by\",\"target.name\",\"target.resource_subtype\",\"task\",\"task.created_by\",\"task.name\",\"task.resource_subtype\",\"text\",\"type\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a story on a task
        api_response = await api_instance.create_story_for_task(task_gid, update_story_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of StoriesApi->create_story_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoriesApi->create_story_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **update_story_request** | [**UpdateStoryRequest**](UpdateStoryRequest.md)| The story to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetStory200Response**](GetStory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new story. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story**
> DeleteAttachment200Response delete_story(story_gid, opt_pretty=opt_pretty)

Delete a story

Deletes a story. A user can only delete stories they have created.  Returns an empty data record.

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
    api_instance = asana_asyncio.StoriesApi(api_client)
    story_gid = '35678' # str | Globally unique identifier for the story.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a story
        api_response = await api_instance.delete_story(story_gid, opt_pretty=opt_pretty)
        print("The response of StoriesApi->delete_story:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoriesApi->delete_story: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_gid** | **str**| Globally unique identifier for the story. | 
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
**200** | Successfully deleted the specified story. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stories_for_task**
> GetStoriesForTask200Response get_stories_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get stories from a task

Returns the compact records for all stories on the task.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_stories_for_task200_response import GetStoriesForTask200Response
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
    api_instance = asana_asyncio.StoriesApi(api_client)
    task_gid = '321654' # str | The task to operate on.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ['[\"assignee\",\"assignee.name\",\"created_at\",\"created_by\",\"created_by.name\",\"custom_field\",\"custom_field.date_value\",\"custom_field.date_value.date\",\"custom_field.date_value.date_time\",\"custom_field.display_value\",\"custom_field.enabled\",\"custom_field.enum_options\",\"custom_field.enum_options.color\",\"custom_field.enum_options.enabled\",\"custom_field.enum_options.name\",\"custom_field.enum_value\",\"custom_field.enum_value.color\",\"custom_field.enum_value.enabled\",\"custom_field.enum_value.name\",\"custom_field.id_prefix\",\"custom_field.is_formula_field\",\"custom_field.multi_enum_values\",\"custom_field.multi_enum_values.color\",\"custom_field.multi_enum_values.enabled\",\"custom_field.multi_enum_values.name\",\"custom_field.name\",\"custom_field.number_value\",\"custom_field.representation_type\",\"custom_field.resource_subtype\",\"custom_field.text_value\",\"custom_field.type\",\"dependency\",\"dependency.created_by\",\"dependency.name\",\"dependency.resource_subtype\",\"duplicate_of\",\"duplicate_of.created_by\",\"duplicate_of.name\",\"duplicate_of.resource_subtype\",\"duplicated_from\",\"duplicated_from.created_by\",\"duplicated_from.name\",\"duplicated_from.resource_subtype\",\"follower\",\"follower.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_text\",\"is_editable\",\"is_edited\",\"is_pinned\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"new_approval_status\",\"new_date_value\",\"new_dates\",\"new_dates.due_at\",\"new_dates.due_on\",\"new_dates.start_on\",\"new_enum_value\",\"new_enum_value.color\",\"new_enum_value.enabled\",\"new_enum_value.name\",\"new_multi_enum_values\",\"new_multi_enum_values.color\",\"new_multi_enum_values.enabled\",\"new_multi_enum_values.name\",\"new_name\",\"new_number_value\",\"new_people_value\",\"new_people_value.name\",\"new_resource_subtype\",\"new_section\",\"new_section.name\",\"new_text_value\",\"num_hearts\",\"num_likes\",\"offset\",\"old_approval_status\",\"old_date_value\",\"old_dates\",\"old_dates.due_at\",\"old_dates.due_on\",\"old_dates.start_on\",\"old_enum_value\",\"old_enum_value.color\",\"old_enum_value.enabled\",\"old_enum_value.name\",\"old_multi_enum_values\",\"old_multi_enum_values.color\",\"old_multi_enum_values.enabled\",\"old_multi_enum_values.name\",\"old_name\",\"old_number_value\",\"old_people_value\",\"old_people_value.name\",\"old_resource_subtype\",\"old_section\",\"old_section.name\",\"old_text_value\",\"path\",\"previews\",\"previews.fallback\",\"previews.footer\",\"previews.header\",\"previews.header_link\",\"previews.html_text\",\"previews.text\",\"previews.title\",\"previews.title_link\",\"project\",\"project.name\",\"resource_subtype\",\"source\",\"sticker_name\",\"story\",\"story.created_at\",\"story.created_by\",\"story.created_by.name\",\"story.resource_subtype\",\"story.text\",\"tag\",\"tag.name\",\"target\",\"target.created_by\",\"target.name\",\"target.resource_subtype\",\"task\",\"task.created_by\",\"task.name\",\"task.resource_subtype\",\"text\",\"type\",\"uri\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get stories from a task
        api_response = await api_instance.get_stories_for_task(task_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of StoriesApi->get_stories_for_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoriesApi->get_stories_for_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetStoriesForTask200Response**](GetStoriesForTask200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified task&#39;s stories. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story**
> GetStory200Response get_story(story_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a story

Returns the full record for a single story.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_story200_response import GetStory200Response
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
    api_instance = asana_asyncio.StoriesApi(api_client)
    story_gid = '35678' # str | Globally unique identifier for the story.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"assignee\",\"assignee.name\",\"created_at\",\"created_by\",\"created_by.name\",\"custom_field\",\"custom_field.date_value\",\"custom_field.date_value.date\",\"custom_field.date_value.date_time\",\"custom_field.display_value\",\"custom_field.enabled\",\"custom_field.enum_options\",\"custom_field.enum_options.color\",\"custom_field.enum_options.enabled\",\"custom_field.enum_options.name\",\"custom_field.enum_value\",\"custom_field.enum_value.color\",\"custom_field.enum_value.enabled\",\"custom_field.enum_value.name\",\"custom_field.id_prefix\",\"custom_field.is_formula_field\",\"custom_field.multi_enum_values\",\"custom_field.multi_enum_values.color\",\"custom_field.multi_enum_values.enabled\",\"custom_field.multi_enum_values.name\",\"custom_field.name\",\"custom_field.number_value\",\"custom_field.representation_type\",\"custom_field.resource_subtype\",\"custom_field.text_value\",\"custom_field.type\",\"dependency\",\"dependency.created_by\",\"dependency.name\",\"dependency.resource_subtype\",\"duplicate_of\",\"duplicate_of.created_by\",\"duplicate_of.name\",\"duplicate_of.resource_subtype\",\"duplicated_from\",\"duplicated_from.created_by\",\"duplicated_from.name\",\"duplicated_from.resource_subtype\",\"follower\",\"follower.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_text\",\"is_editable\",\"is_edited\",\"is_pinned\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"new_approval_status\",\"new_date_value\",\"new_dates\",\"new_dates.due_at\",\"new_dates.due_on\",\"new_dates.start_on\",\"new_enum_value\",\"new_enum_value.color\",\"new_enum_value.enabled\",\"new_enum_value.name\",\"new_multi_enum_values\",\"new_multi_enum_values.color\",\"new_multi_enum_values.enabled\",\"new_multi_enum_values.name\",\"new_name\",\"new_number_value\",\"new_people_value\",\"new_people_value.name\",\"new_resource_subtype\",\"new_section\",\"new_section.name\",\"new_text_value\",\"num_hearts\",\"num_likes\",\"old_approval_status\",\"old_date_value\",\"old_dates\",\"old_dates.due_at\",\"old_dates.due_on\",\"old_dates.start_on\",\"old_enum_value\",\"old_enum_value.color\",\"old_enum_value.enabled\",\"old_enum_value.name\",\"old_multi_enum_values\",\"old_multi_enum_values.color\",\"old_multi_enum_values.enabled\",\"old_multi_enum_values.name\",\"old_name\",\"old_number_value\",\"old_people_value\",\"old_people_value.name\",\"old_resource_subtype\",\"old_section\",\"old_section.name\",\"old_text_value\",\"previews\",\"previews.fallback\",\"previews.footer\",\"previews.header\",\"previews.header_link\",\"previews.html_text\",\"previews.text\",\"previews.title\",\"previews.title_link\",\"project\",\"project.name\",\"resource_subtype\",\"source\",\"sticker_name\",\"story\",\"story.created_at\",\"story.created_by\",\"story.created_by.name\",\"story.resource_subtype\",\"story.text\",\"tag\",\"tag.name\",\"target\",\"target.created_by\",\"target.name\",\"target.resource_subtype\",\"task\",\"task.created_by\",\"task.name\",\"task.resource_subtype\",\"text\",\"type\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a story
        api_response = await api_instance.get_story(story_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of StoriesApi->get_story:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoriesApi->get_story: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_gid** | **str**| Globally unique identifier for the story. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetStory200Response**](GetStory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified story. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_story**
> GetStory200Response update_story(story_gid, update_story_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Update a story

Updates the story and returns the full record for the updated story. Only comment stories can have their text updated, and only comment stories and attachment stories can be pinned. Only one of `text` and `html_text` can be specified.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_story200_response import GetStory200Response
from asana_asyncio.models.update_story_request import UpdateStoryRequest
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
    api_instance = asana_asyncio.StoriesApi(api_client)
    story_gid = '35678' # str | Globally unique identifier for the story.
    update_story_request = asana_asyncio.UpdateStoryRequest() # UpdateStoryRequest | The comment story to update.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"assignee\",\"assignee.name\",\"created_at\",\"created_by\",\"created_by.name\",\"custom_field\",\"custom_field.date_value\",\"custom_field.date_value.date\",\"custom_field.date_value.date_time\",\"custom_field.display_value\",\"custom_field.enabled\",\"custom_field.enum_options\",\"custom_field.enum_options.color\",\"custom_field.enum_options.enabled\",\"custom_field.enum_options.name\",\"custom_field.enum_value\",\"custom_field.enum_value.color\",\"custom_field.enum_value.enabled\",\"custom_field.enum_value.name\",\"custom_field.id_prefix\",\"custom_field.is_formula_field\",\"custom_field.multi_enum_values\",\"custom_field.multi_enum_values.color\",\"custom_field.multi_enum_values.enabled\",\"custom_field.multi_enum_values.name\",\"custom_field.name\",\"custom_field.number_value\",\"custom_field.representation_type\",\"custom_field.resource_subtype\",\"custom_field.text_value\",\"custom_field.type\",\"dependency\",\"dependency.created_by\",\"dependency.name\",\"dependency.resource_subtype\",\"duplicate_of\",\"duplicate_of.created_by\",\"duplicate_of.name\",\"duplicate_of.resource_subtype\",\"duplicated_from\",\"duplicated_from.created_by\",\"duplicated_from.name\",\"duplicated_from.resource_subtype\",\"follower\",\"follower.name\",\"hearted\",\"hearts\",\"hearts.user\",\"hearts.user.name\",\"html_text\",\"is_editable\",\"is_edited\",\"is_pinned\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"new_approval_status\",\"new_date_value\",\"new_dates\",\"new_dates.due_at\",\"new_dates.due_on\",\"new_dates.start_on\",\"new_enum_value\",\"new_enum_value.color\",\"new_enum_value.enabled\",\"new_enum_value.name\",\"new_multi_enum_values\",\"new_multi_enum_values.color\",\"new_multi_enum_values.enabled\",\"new_multi_enum_values.name\",\"new_name\",\"new_number_value\",\"new_people_value\",\"new_people_value.name\",\"new_resource_subtype\",\"new_section\",\"new_section.name\",\"new_text_value\",\"num_hearts\",\"num_likes\",\"old_approval_status\",\"old_date_value\",\"old_dates\",\"old_dates.due_at\",\"old_dates.due_on\",\"old_dates.start_on\",\"old_enum_value\",\"old_enum_value.color\",\"old_enum_value.enabled\",\"old_enum_value.name\",\"old_multi_enum_values\",\"old_multi_enum_values.color\",\"old_multi_enum_values.enabled\",\"old_multi_enum_values.name\",\"old_name\",\"old_number_value\",\"old_people_value\",\"old_people_value.name\",\"old_resource_subtype\",\"old_section\",\"old_section.name\",\"old_text_value\",\"previews\",\"previews.fallback\",\"previews.footer\",\"previews.header\",\"previews.header_link\",\"previews.html_text\",\"previews.text\",\"previews.title\",\"previews.title_link\",\"project\",\"project.name\",\"resource_subtype\",\"source\",\"sticker_name\",\"story\",\"story.created_at\",\"story.created_by\",\"story.created_by.name\",\"story.resource_subtype\",\"story.text\",\"tag\",\"tag.name\",\"target\",\"target.created_by\",\"target.name\",\"target.resource_subtype\",\"task\",\"task.created_by\",\"task.name\",\"task.resource_subtype\",\"text\",\"type\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Update a story
        api_response = await api_instance.update_story(story_gid, update_story_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of StoriesApi->update_story:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoriesApi->update_story: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_gid** | **str**| Globally unique identifier for the story. | 
 **update_story_request** | [**UpdateStoryRequest**](UpdateStoryRequest.md)| The comment story to update. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetStory200Response**](GetStory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified story. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

