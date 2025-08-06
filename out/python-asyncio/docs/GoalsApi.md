# asana_asyncio.GoalsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_followers**](GoalsApi.md#add_followers) | **POST** /goals/{goal_gid}/addFollowers | Add a collaborator to a goal
[**create_goal**](GoalsApi.md#create_goal) | **POST** /goals | Create a goal
[**create_goal_metric**](GoalsApi.md#create_goal_metric) | **POST** /goals/{goal_gid}/setMetric | Create a goal metric
[**delete_goal**](GoalsApi.md#delete_goal) | **DELETE** /goals/{goal_gid} | Delete a goal
[**get_goal**](GoalsApi.md#get_goal) | **GET** /goals/{goal_gid} | Get a goal
[**get_goals**](GoalsApi.md#get_goals) | **GET** /goals | Get goals
[**get_parent_goals_for_goal**](GoalsApi.md#get_parent_goals_for_goal) | **GET** /goals/{goal_gid}/parentGoals | Get parent goals from a goal
[**remove_followers**](GoalsApi.md#remove_followers) | **POST** /goals/{goal_gid}/removeFollowers | Remove a collaborator from a goal
[**update_goal**](GoalsApi.md#update_goal) | **PUT** /goals/{goal_gid} | Update a goal
[**update_goal_metric**](GoalsApi.md#update_goal_metric) | **POST** /goals/{goal_gid}/setMetricCurrentValue | Update a goal metric


# **add_followers**
> GetGoal200Response add_followers(goal_gid, add_followers_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Add a collaborator to a goal

Adds followers to a goal. Returns the goal the followers were added to.
Each goal can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_followers_request import AddFollowersRequest
from asana_asyncio.models.get_goal200_response import GetGoal200Response
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    goal_gid = '12345' # str | Globally unique identifier for the goal.
    add_followers_request = asana_asyncio.AddFollowersRequest() # AddFollowersRequest | The followers to be added as collaborators
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"owner\",\"owner.name\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Add a collaborator to a goal
        api_response = await api_instance.add_followers(goal_gid, add_followers_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of GoalsApi->add_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->add_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **add_followers_request** | [**AddFollowersRequest**](AddFollowersRequest.md)| The followers to be added as collaborators | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added users as collaborators. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_goal**
> GetGoal200Response create_goal(create_goal_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a goal

Creates a new goal in a workspace or team.

Returns the full record of the newly created goal.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_goal_request import CreateGoalRequest
from asana_asyncio.models.get_goal200_response import GetGoal200Response
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    create_goal_request = asana_asyncio.CreateGoalRequest() # CreateGoalRequest | The goal to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"owner\",\"owner.name\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a goal
        api_response = await api_instance.create_goal(create_goal_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of GoalsApi->create_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->create_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_goal_request** | [**CreateGoalRequest**](CreateGoalRequest.md)| The goal to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new goal. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_goal_metric**
> GetGoal200Response create_goal_metric(goal_gid, create_goal_metric_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a goal metric

Creates and adds a goal metric to a specified goal. Note that this replaces an existing goal metric if one already exists.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_goal_metric_request import CreateGoalMetricRequest
from asana_asyncio.models.get_goal200_response import GetGoal200Response
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    goal_gid = '12345' # str | Globally unique identifier for the goal.
    create_goal_metric_request = asana_asyncio.CreateGoalMetricRequest() # CreateGoalMetricRequest | The goal metric to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"owner\",\"owner.name\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a goal metric
        api_response = await api_instance.create_goal_metric(goal_gid, create_goal_metric_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of GoalsApi->create_goal_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->create_goal_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **create_goal_metric_request** | [**CreateGoalMetricRequest**](CreateGoalMetricRequest.md)| The goal metric to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new goal metric. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_goal**
> DeleteAllocation200Response delete_goal(goal_gid, opt_pretty=opt_pretty)

Delete a goal

A specific, existing goal can be deleted by making a DELETE request on the URL for that goal.

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
    api_instance = asana_asyncio.GoalsApi(api_client)
    goal_gid = '12345' # str | Globally unique identifier for the goal.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a goal
        api_response = await api_instance.delete_goal(goal_gid, opt_pretty=opt_pretty)
        print("The response of GoalsApi->delete_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->delete_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
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
**200** | Successfully deleted the specified goal. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal**
> GetGoal200Response get_goal(goal_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a goal

<b>Required scope: </b><code>goals:read</code>

<table>
  <tr>
    <th>Field</th>
    <th>Required Scope</th>
  </tr>
  <tr>
    <td><code>time_period</code></td>
    <td><code>time_periods:read</code></td>
  </tr>
</table>

Returns the complete goal record for a single goal.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_goal200_response import GetGoal200Response
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    goal_gid = '12345' # str | Globally unique identifier for the goal.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"owner\",\"owner.name\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a goal
        api_response = await api_instance.get_goal(goal_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of GoalsApi->get_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the record for a single goal. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals**
> GetGoals200Response get_goals(opt_pretty=opt_pretty, portfolio=portfolio, project=project, task=task, is_workspace_level=is_workspace_level, team=team, workspace=workspace, time_periods=time_periods, limit=limit, offset=offset, opt_fields=opt_fields)

Get goals

<b>Required scope: </b><code>goals:read</code>

Returns compact goal records.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_goals200_response import GetGoals200Response
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    portfolio = '159874' # str | Globally unique identifier for supporting portfolio. (optional)
    project = '512241' # str | Globally unique identifier for supporting project. (optional)
    task = '78424' # str | Globally unique identifier for supporting task. (optional)
    is_workspace_level = false # bool | Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter. (optional)
    team = '31326' # str | Globally unique identifier for the team. (optional)
    workspace = '31326' # str | Globally unique identifier for the workspace. (optional)
    time_periods = ['221693,506165'] # List[str] | Globally unique identifiers for the time periods. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"offset\",\"owner\",\"owner.name\",\"path\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get goals
        api_response = await api_instance.get_goals(opt_pretty=opt_pretty, portfolio=portfolio, project=project, task=task, is_workspace_level=is_workspace_level, team=team, workspace=workspace, time_periods=time_periods, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of GoalsApi->get_goals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **portfolio** | **str**| Globally unique identifier for supporting portfolio. | [optional] 
 **project** | **str**| Globally unique identifier for supporting project. | [optional] 
 **task** | **str**| Globally unique identifier for supporting task. | [optional] 
 **is_workspace_level** | **bool**| Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter. | [optional] 
 **team** | **str**| Globally unique identifier for the team. | [optional] 
 **workspace** | **str**| Globally unique identifier for the workspace. | [optional] 
 **time_periods** | [**List[str]**](str.md)| Globally unique identifiers for the time periods. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetGoals200Response**](GetGoals200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested goals. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_goals_for_goal**
> GetParentGoalsForGoal200Response get_parent_goals_for_goal(goal_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get parent goals from a goal

<b>Required scope: </b><code>goals:read</code>

Returns a compact representation of all of the parent goals of a goal.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_parent_goals_for_goal200_response import GetParentGoalsForGoal200Response
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    goal_gid = '12345' # str | Globally unique identifier for the goal.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"owner\",\"owner.name\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get parent goals from a goal
        api_response = await api_instance.get_parent_goals_for_goal(goal_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of GoalsApi->get_parent_goals_for_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_parent_goals_for_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetParentGoalsForGoal200Response**](GetParentGoalsForGoal200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the specified goal&#39;s parent goals. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_followers**
> GetGoal200Response remove_followers(goal_gid, add_followers_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Remove a collaborator from a goal

Removes followers from a goal. Returns the goal the followers were removed from.
Each goal can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_followers_request import AddFollowersRequest
from asana_asyncio.models.get_goal200_response import GetGoal200Response
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    goal_gid = '12345' # str | Globally unique identifier for the goal.
    add_followers_request = asana_asyncio.AddFollowersRequest() # AddFollowersRequest | The followers to be removed as collaborators
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"owner\",\"owner.name\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Remove a collaborator from a goal
        api_response = await api_instance.remove_followers(goal_gid, add_followers_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of GoalsApi->remove_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->remove_followers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **add_followers_request** | [**AddFollowersRequest**](AddFollowersRequest.md)| The followers to be removed as collaborators | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed users as collaborators. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal**
> GetGoal200Response update_goal(goal_gid, update_goal_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Update a goal

An existing goal can be updated by making a PUT request on the URL for
that goal. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated goal record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_goal200_response import GetGoal200Response
from asana_asyncio.models.update_goal_request import UpdateGoalRequest
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    goal_gid = '12345' # str | Globally unique identifier for the goal.
    update_goal_request = asana_asyncio.UpdateGoalRequest() # UpdateGoalRequest | The updated fields for the goal.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"owner\",\"owner.name\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Update a goal
        api_response = await api_instance.update_goal(goal_gid, update_goal_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of GoalsApi->update_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->update_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **update_goal_request** | [**UpdateGoalRequest**](UpdateGoalRequest.md)| The updated fields for the goal. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the goal. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_metric**
> GetGoal200Response update_goal_metric(goal_gid, update_goal_metric_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Update a goal metric

Updates a goal's existing metric's `current_number_value` if one exists,
otherwise responds with a 400 status code.

Returns the complete updated goal metric record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_goal200_response import GetGoal200Response
from asana_asyncio.models.update_goal_metric_request import UpdateGoalMetricRequest
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
    api_instance = asana_asyncio.GoalsApi(api_client)
    goal_gid = '12345' # str | Globally unique identifier for the goal.
    update_goal_metric_request = asana_asyncio.UpdateGoalMetricRequest() # UpdateGoalMetricRequest | The updated fields for the goal metric.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"is_workspace_level\",\"liked\",\"likes\",\"likes.user\",\"likes.user.name\",\"metric\",\"metric.can_manage\",\"metric.currency_code\",\"metric.current_display_value\",\"metric.current_number_value\",\"metric.initial_number_value\",\"metric.is_custom_weight\",\"metric.precision\",\"metric.progress_source\",\"metric.resource_subtype\",\"metric.target_number_value\",\"metric.unit\",\"name\",\"notes\",\"num_likes\",\"owner\",\"owner.name\",\"start_on\",\"status\",\"team\",\"team.name\",\"time_period\",\"time_period.display_name\",\"time_period.end_on\",\"time_period.period\",\"time_period.start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Update a goal metric
        api_response = await api_instance.update_goal_metric(goal_gid, update_goal_metric_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of GoalsApi->update_goal_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->update_goal_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **update_goal_metric_request** | [**UpdateGoalMetricRequest**](UpdateGoalMetricRequest.md)| The updated fields for the goal metric. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetGoal200Response**](GetGoal200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the goal metric. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

