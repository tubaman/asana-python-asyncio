# asana_asyncio.PortfoliosApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_field_setting_for_portfolio**](PortfoliosApi.md#add_custom_field_setting_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addCustomFieldSetting | Add a custom field to a portfolio
[**add_item_for_portfolio**](PortfoliosApi.md#add_item_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addItem | Add a portfolio item
[**add_members_for_portfolio**](PortfoliosApi.md#add_members_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addMembers | Add users to a portfolio
[**create_portfolio**](PortfoliosApi.md#create_portfolio) | **POST** /portfolios | Create a portfolio
[**delete_portfolio**](PortfoliosApi.md#delete_portfolio) | **DELETE** /portfolios/{portfolio_gid} | Delete a portfolio
[**get_items_for_portfolio**](PortfoliosApi.md#get_items_for_portfolio) | **GET** /portfolios/{portfolio_gid}/items | Get portfolio items
[**get_portfolio**](PortfoliosApi.md#get_portfolio) | **GET** /portfolios/{portfolio_gid} | Get a portfolio
[**get_portfolios**](PortfoliosApi.md#get_portfolios) | **GET** /portfolios | Get multiple portfolios
[**remove_custom_field_setting_for_portfolio**](PortfoliosApi.md#remove_custom_field_setting_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeCustomFieldSetting | Remove a custom field from a portfolio
[**remove_item_for_portfolio**](PortfoliosApi.md#remove_item_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeItem | Remove a portfolio item
[**remove_members_for_portfolio**](PortfoliosApi.md#remove_members_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeMembers | Remove users from a portfolio
[**update_portfolio**](PortfoliosApi.md#update_portfolio) | **PUT** /portfolios/{portfolio_gid} | Update a portfolio


# **add_custom_field_setting_for_portfolio**
> AddCustomFieldSettingForPortfolio200Response add_custom_field_setting_for_portfolio(portfolio_gid, add_custom_field_setting_for_portfolio_request, opt_pretty=opt_pretty)

Add a custom field to a portfolio

Custom fields are associated with portfolios by way of custom field settings.  This method creates a setting for the portfolio.

### Example

* Bearer Authentication (personalAccessToken):
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    add_custom_field_setting_for_portfolio_request = asana_asyncio.AddCustomFieldSettingForPortfolioRequest() # AddCustomFieldSettingForPortfolioRequest | Information about the custom field setting.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Add a custom field to a portfolio
        api_response = await api_instance.add_custom_field_setting_for_portfolio(portfolio_gid, add_custom_field_setting_for_portfolio_request, opt_pretty=opt_pretty)
        print("The response of PortfoliosApi->add_custom_field_setting_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->add_custom_field_setting_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **add_custom_field_setting_for_portfolio_request** | [**AddCustomFieldSettingForPortfolioRequest**](AddCustomFieldSettingForPortfolioRequest.md)| Information about the custom field setting. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 

### Return type

[**AddCustomFieldSettingForPortfolio200Response**](AddCustomFieldSettingForPortfolio200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added the custom field to the portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_for_portfolio**
> DeleteAllocation200Response add_item_for_portfolio(portfolio_gid, add_item_for_portfolio_request, opt_pretty=opt_pretty)

Add a portfolio item

Add an item to a portfolio.
Returns an empty data block.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_item_for_portfolio_request import AddItemForPortfolioRequest
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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    add_item_for_portfolio_request = asana_asyncio.AddItemForPortfolioRequest() # AddItemForPortfolioRequest | Information about the item being inserted.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Add a portfolio item
        api_response = await api_instance.add_item_for_portfolio(portfolio_gid, add_item_for_portfolio_request, opt_pretty=opt_pretty)
        print("The response of PortfoliosApi->add_item_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->add_item_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **add_item_for_portfolio_request** | [**AddItemForPortfolioRequest**](AddItemForPortfolioRequest.md)| Information about the item being inserted. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 

### Return type

[**DeleteAllocation200Response**](DeleteAllocation200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added the item to the portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_members_for_portfolio**
> CreatePortfolio201Response add_members_for_portfolio(portfolio_gid, add_members_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Add users to a portfolio

Adds the specified list of users as members of the portfolio.
Returns the updated portfolio record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.add_members_for_portfolio_request import AddMembersForPortfolioRequest
from asana_asyncio.models.create_portfolio201_response import CreatePortfolio201Response
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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    add_members_for_portfolio_request = asana_asyncio.AddMembersForPortfolioRequest() # AddMembersForPortfolioRequest | Information about the members being added.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"created_at\",\"created_by\",\"created_by.name\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"due_on\",\"members\",\"members.name\",\"name\",\"owner\",\"owner.name\",\"permalink_url\",\"privacy_setting\",\"project_templates\",\"project_templates.name\",\"public\",\"start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Add users to a portfolio
        api_response = await api_instance.add_members_for_portfolio(portfolio_gid, add_members_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of PortfoliosApi->add_members_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->add_members_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **add_members_for_portfolio_request** | [**AddMembersForPortfolioRequest**](AddMembersForPortfolioRequest.md)| Information about the members being added. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreatePortfolio201Response**](CreatePortfolio201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added members to the portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_portfolio**
> CreatePortfolio201Response create_portfolio(create_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Create a portfolio

Creates a new portfolio in the given workspace with the supplied name.

Note that portfolios created in the Asana UI may have some state
(like the “Priority” custom field) which is automatically added
to the portfolio when it is created. Portfolios created via our
API will *not* be created with the same initial state to allow
integrations to create their own starting state on a portfolio.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_portfolio201_response import CreatePortfolio201Response
from asana_asyncio.models.create_portfolio_request import CreatePortfolioRequest
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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    create_portfolio_request = asana_asyncio.CreatePortfolioRequest() # CreatePortfolioRequest | The portfolio to create.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"created_at\",\"created_by\",\"created_by.name\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"due_on\",\"members\",\"members.name\",\"name\",\"owner\",\"owner.name\",\"permalink_url\",\"privacy_setting\",\"project_templates\",\"project_templates.name\",\"public\",\"start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Create a portfolio
        api_response = await api_instance.create_portfolio(create_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of PortfoliosApi->create_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->create_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_portfolio_request** | [**CreatePortfolioRequest**](CreatePortfolioRequest.md)| The portfolio to create. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreatePortfolio201Response**](CreatePortfolio201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio**
> DeleteAllocation200Response delete_portfolio(portfolio_gid, opt_pretty=opt_pretty)

Delete a portfolio

An existing portfolio can be deleted by making a DELETE request on
the URL for that portfolio.

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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Delete a portfolio
        api_response = await api_instance.delete_portfolio(portfolio_gid, opt_pretty=opt_pretty)
        print("The response of PortfoliosApi->delete_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->delete_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
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
**200** | Successfully deleted the specified portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_for_portfolio**
> GetItemsForPortfolio200Response get_items_for_portfolio(portfolio_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get portfolio items

<b>Required scope: </b><code>portfolios:read</code>

Get a list of the items in compact form in a portfolio.

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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    opt_fields = ['[\"archived\",\"color\",\"completed\",\"completed_at\",\"completed_by\",\"completed_by.name\",\"created_at\",\"created_from_template\",\"created_from_template.name\",\"current_status\",\"current_status.author\",\"current_status.author.name\",\"current_status.color\",\"current_status.created_at\",\"current_status.created_by\",\"current_status.created_by.name\",\"current_status.html_text\",\"current_status.modified_at\",\"current_status.text\",\"current_status.title\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"default_view\",\"due_date\",\"due_on\",\"followers\",\"followers.name\",\"html_notes\",\"icon\",\"members\",\"members.name\",\"minimum_access_level_for_customization\",\"minimum_access_level_for_sharing\",\"modified_at\",\"name\",\"notes\",\"offset\",\"owner\",\"path\",\"permalink_url\",\"privacy_setting\",\"project_brief\",\"public\",\"start_on\",\"team\",\"team.name\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get portfolio items
        api_response = await api_instance.get_items_for_portfolio(portfolio_gid, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of PortfoliosApi->get_items_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_items_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
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
**200** | Successfully retrieved the requested portfolio&#39;s items. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio**
> CreatePortfolio201Response get_portfolio(portfolio_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a portfolio

<b>Required scope: </b><code>portfolios:read</code>

Returns the complete portfolio record for a single portfolio.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_portfolio201_response import CreatePortfolio201Response
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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"created_at\",\"created_by\",\"created_by.name\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"due_on\",\"members\",\"members.name\",\"name\",\"owner\",\"owner.name\",\"permalink_url\",\"privacy_setting\",\"project_templates\",\"project_templates.name\",\"public\",\"start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a portfolio
        api_response = await api_instance.get_portfolio(portfolio_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of PortfoliosApi->get_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreatePortfolio201Response**](CreatePortfolio201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolios**
> GetPortfolios200Response get_portfolios(workspace, opt_pretty=opt_pretty, limit=limit, offset=offset, owner=owner, opt_fields=opt_fields)

Get multiple portfolios

<b>Required scope: </b><code>portfolios:read</code>

Returns a list of the portfolios in compact representation that are owned by the current API user.

### Example

* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.get_portfolios200_response import GetPortfolios200Response
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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    workspace = '1331' # str | The workspace or organization to filter portfolios on.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* (optional)
    owner = '14916' # str | The user who owns the portfolio. Currently, API users can only get a list of portfolios that they themselves own, unless the request is made from a Service Account. In the case of a Service Account, if this parameter is specified, then all portfolios owned by this parameter are returned. Otherwise, all portfolios across the workspace are returned. (optional)
    opt_fields = ['[\"archived\",\"color\",\"created_at\",\"created_by\",\"created_by.name\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"due_on\",\"members\",\"members.name\",\"name\",\"offset\",\"owner\",\"owner.name\",\"path\",\"permalink_url\",\"privacy_setting\",\"project_templates\",\"project_templates.name\",\"public\",\"start_on\",\"uri\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get multiple portfolios
        api_response = await api_instance.get_portfolios(workspace, opt_pretty=opt_pretty, limit=limit, offset=offset, owner=owner, opt_fields=opt_fields)
        print("The response of PortfoliosApi->get_portfolios:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolios: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace or organization to filter portfolios on. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **owner** | **str**| The user who owns the portfolio. Currently, API users can only get a list of portfolios that they themselves own, unless the request is made from a Service Account. In the case of a Service Account, if this parameter is specified, then all portfolios owned by this parameter are returned. Otherwise, all portfolios across the workspace are returned. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetPortfolios200Response**](GetPortfolios200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved portfolios. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_custom_field_setting_for_portfolio**
> DeleteAllocation200Response remove_custom_field_setting_for_portfolio(portfolio_gid, remove_custom_field_setting_for_portfolio_request, opt_pretty=opt_pretty)

Remove a custom field from a portfolio

Removes a custom field setting from a portfolio.

### Example

* Bearer Authentication (personalAccessToken):
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

# Configure Bearer authorization: personalAccessToken
configuration = asana_asyncio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with asana_asyncio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    remove_custom_field_setting_for_portfolio_request = asana_asyncio.RemoveCustomFieldSettingForPortfolioRequest() # RemoveCustomFieldSettingForPortfolioRequest | Information about the custom field setting being removed.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Remove a custom field from a portfolio
        api_response = await api_instance.remove_custom_field_setting_for_portfolio(portfolio_gid, remove_custom_field_setting_for_portfolio_request, opt_pretty=opt_pretty)
        print("The response of PortfoliosApi->remove_custom_field_setting_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->remove_custom_field_setting_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **remove_custom_field_setting_for_portfolio_request** | [**RemoveCustomFieldSettingForPortfolioRequest**](RemoveCustomFieldSettingForPortfolioRequest.md)| Information about the custom field setting being removed. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 

### Return type

[**DeleteAllocation200Response**](DeleteAllocation200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the custom field from the portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_item_for_portfolio**
> DeleteAllocation200Response remove_item_for_portfolio(portfolio_gid, remove_item_for_portfolio_request, opt_pretty=opt_pretty)

Remove a portfolio item

Remove an item from a portfolio.
Returns an empty data block.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.delete_allocation200_response import DeleteAllocation200Response
from asana_asyncio.models.remove_item_for_portfolio_request import RemoveItemForPortfolioRequest
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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    remove_item_for_portfolio_request = asana_asyncio.RemoveItemForPortfolioRequest() # RemoveItemForPortfolioRequest | Information about the item being removed.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)

    try:
        # Remove a portfolio item
        api_response = await api_instance.remove_item_for_portfolio(portfolio_gid, remove_item_for_portfolio_request, opt_pretty=opt_pretty)
        print("The response of PortfoliosApi->remove_item_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->remove_item_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **remove_item_for_portfolio_request** | [**RemoveItemForPortfolioRequest**](RemoveItemForPortfolioRequest.md)| Information about the item being removed. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 

### Return type

[**DeleteAllocation200Response**](DeleteAllocation200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the item from the portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_members_for_portfolio**
> CreatePortfolio201Response remove_members_for_portfolio(portfolio_gid, remove_members_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Remove users from a portfolio

Removes the specified list of users from members of the portfolio.
Returns the updated portfolio record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_portfolio201_response import CreatePortfolio201Response
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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    remove_members_for_portfolio_request = asana_asyncio.RemoveMembersForPortfolioRequest() # RemoveMembersForPortfolioRequest | Information about the members being removed.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"created_at\",\"created_by\",\"created_by.name\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"due_on\",\"members\",\"members.name\",\"name\",\"owner\",\"owner.name\",\"permalink_url\",\"privacy_setting\",\"project_templates\",\"project_templates.name\",\"public\",\"start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Remove users from a portfolio
        api_response = await api_instance.remove_members_for_portfolio(portfolio_gid, remove_members_for_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of PortfoliosApi->remove_members_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->remove_members_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **remove_members_for_portfolio_request** | [**RemoveMembersForPortfolioRequest**](RemoveMembersForPortfolioRequest.md)| Information about the members being removed. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreatePortfolio201Response**](CreatePortfolio201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the members from the portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portfolio**
> CreatePortfolio201Response update_portfolio(portfolio_gid, create_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)

Update a portfolio

An existing portfolio can be updated by making a PUT request on the URL for
that portfolio. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated portfolio record.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_portfolio201_response import CreatePortfolio201Response
from asana_asyncio.models.create_portfolio_request import CreatePortfolioRequest
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
    api_instance = asana_asyncio.PortfoliosApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    create_portfolio_request = asana_asyncio.CreatePortfolioRequest() # CreatePortfolioRequest | The updated fields for the portfolio.
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"archived\",\"color\",\"created_at\",\"created_by\",\"created_by.name\",\"current_status_update\",\"current_status_update.resource_subtype\",\"current_status_update.title\",\"custom_field_settings\",\"custom_field_settings.custom_field\",\"custom_field_settings.custom_field.asana_created_field\",\"custom_field_settings.custom_field.created_by\",\"custom_field_settings.custom_field.created_by.name\",\"custom_field_settings.custom_field.currency_code\",\"custom_field_settings.custom_field.custom_label\",\"custom_field_settings.custom_field.custom_label_position\",\"custom_field_settings.custom_field.date_value\",\"custom_field_settings.custom_field.date_value.date\",\"custom_field_settings.custom_field.date_value.date_time\",\"custom_field_settings.custom_field.default_access_level\",\"custom_field_settings.custom_field.description\",\"custom_field_settings.custom_field.display_value\",\"custom_field_settings.custom_field.enabled\",\"custom_field_settings.custom_field.enum_options\",\"custom_field_settings.custom_field.enum_options.color\",\"custom_field_settings.custom_field.enum_options.enabled\",\"custom_field_settings.custom_field.enum_options.name\",\"custom_field_settings.custom_field.enum_value\",\"custom_field_settings.custom_field.enum_value.color\",\"custom_field_settings.custom_field.enum_value.enabled\",\"custom_field_settings.custom_field.enum_value.name\",\"custom_field_settings.custom_field.format\",\"custom_field_settings.custom_field.has_notifications_enabled\",\"custom_field_settings.custom_field.id_prefix\",\"custom_field_settings.custom_field.is_formula_field\",\"custom_field_settings.custom_field.is_global_to_workspace\",\"custom_field_settings.custom_field.is_value_read_only\",\"custom_field_settings.custom_field.multi_enum_values\",\"custom_field_settings.custom_field.multi_enum_values.color\",\"custom_field_settings.custom_field.multi_enum_values.enabled\",\"custom_field_settings.custom_field.multi_enum_values.name\",\"custom_field_settings.custom_field.name\",\"custom_field_settings.custom_field.number_value\",\"custom_field_settings.custom_field.people_value\",\"custom_field_settings.custom_field.people_value.name\",\"custom_field_settings.custom_field.precision\",\"custom_field_settings.custom_field.privacy_setting\",\"custom_field_settings.custom_field.representation_type\",\"custom_field_settings.custom_field.resource_subtype\",\"custom_field_settings.custom_field.text_value\",\"custom_field_settings.custom_field.type\",\"custom_field_settings.is_important\",\"custom_field_settings.parent\",\"custom_field_settings.parent.name\",\"custom_field_settings.project\",\"custom_field_settings.project.name\",\"custom_fields\",\"custom_fields.date_value\",\"custom_fields.date_value.date\",\"custom_fields.date_value.date_time\",\"custom_fields.display_value\",\"custom_fields.enabled\",\"custom_fields.enum_options\",\"custom_fields.enum_options.color\",\"custom_fields.enum_options.enabled\",\"custom_fields.enum_options.name\",\"custom_fields.enum_value\",\"custom_fields.enum_value.color\",\"custom_fields.enum_value.enabled\",\"custom_fields.enum_value.name\",\"custom_fields.id_prefix\",\"custom_fields.is_formula_field\",\"custom_fields.multi_enum_values\",\"custom_fields.multi_enum_values.color\",\"custom_fields.multi_enum_values.enabled\",\"custom_fields.multi_enum_values.name\",\"custom_fields.name\",\"custom_fields.number_value\",\"custom_fields.representation_type\",\"custom_fields.text_value\",\"custom_fields.type\",\"default_access_level\",\"due_on\",\"members\",\"members.name\",\"name\",\"owner\",\"owner.name\",\"permalink_url\",\"privacy_setting\",\"project_templates\",\"project_templates.name\",\"public\",\"start_on\",\"workspace\",\"workspace.name\"]'] # List[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Update a portfolio
        api_response = await api_instance.update_portfolio(portfolio_gid, create_portfolio_request, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of PortfoliosApi->update_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->update_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **create_portfolio_request** | [**CreatePortfolioRequest**](CreatePortfolioRequest.md)| The updated fields for the portfolio. | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CreatePortfolio201Response**](CreatePortfolio201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the portfolio. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

