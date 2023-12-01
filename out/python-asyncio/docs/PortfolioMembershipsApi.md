# asana_asyncio.PortfolioMembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portfolio_membership**](PortfolioMembershipsApi.md#get_portfolio_membership) | **GET** /portfolio_memberships/{portfolio_membership_gid} | Get a portfolio membership
[**get_portfolio_memberships**](PortfolioMembershipsApi.md#get_portfolio_memberships) | **GET** /portfolio_memberships | Get multiple portfolio memberships
[**get_portfolio_memberships_for_portfolio**](PortfolioMembershipsApi.md#get_portfolio_memberships_for_portfolio) | **GET** /portfolios/{portfolio_gid}/portfolio_memberships | Get memberships from a portfolio


# **get_portfolio_membership**
> GetPortfolioMembership200Response get_portfolio_membership(portfolio_membership_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)

Get a portfolio membership

Returns the complete portfolio record for a single portfolio membership.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_portfolio_membership200_response import GetPortfolioMembership200Response
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
    api_instance = asana_asyncio.PortfolioMembershipsApi(api_client)
    portfolio_membership_gid = '1331' # str | 
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    opt_fields = ['[\"portfolio\",\"portfolio.name\",\"user\",\"user.name\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get a portfolio membership
        api_response = await api_instance.get_portfolio_membership(portfolio_membership_gid, opt_pretty=opt_pretty, opt_fields=opt_fields)
        print("The response of PortfolioMembershipsApi->get_portfolio_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMembershipsApi->get_portfolio_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_membership_gid** | **str**|  | 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetPortfolioMembership200Response**](GetPortfolioMembership200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested portfolio membership. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_memberships**
> GetPortfolioMemberships200Response get_portfolio_memberships(portfolio=portfolio, workspace=workspace, user=user, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get multiple portfolio memberships

Returns a list of portfolio memberships in compact representation. You must specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_portfolio_memberships200_response import GetPortfolioMemberships200Response
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
    api_instance = asana_asyncio.PortfolioMembershipsApi(api_client)
    portfolio = '12345' # str | The portfolio to filter results on. (optional)
    workspace = '12345' # str | The workspace to filter results on. (optional)
    user = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (optional)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ['[\"offset\",\"path\",\"portfolio\",\"portfolio.name\",\"uri\",\"user\",\"user.name\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get multiple portfolio memberships
        api_response = await api_instance.get_portfolio_memberships(portfolio=portfolio, workspace=workspace, user=user, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of PortfolioMembershipsApi->get_portfolio_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMembershipsApi->get_portfolio_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio** | **str**| The portfolio to filter results on. | [optional] 
 **workspace** | **str**| The workspace to filter results on. | [optional] 
 **user** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetPortfolioMemberships200Response**](GetPortfolioMemberships200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved portfolio memberships. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_memberships_for_portfolio**
> GetPortfolioMemberships200Response get_portfolio_memberships_for_portfolio(portfolio_gid, user=user, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)

Get memberships from a portfolio

Returns the compact portfolio membership records for the portfolio.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.get_portfolio_memberships200_response import GetPortfolioMemberships200Response
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
    api_instance = asana_asyncio.PortfolioMembershipsApi(api_client)
    portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
    user = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (optional)
    opt_pretty = true # bool | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. (optional)
    limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
    opt_fields = ['[\"offset\",\"path\",\"portfolio\",\"portfolio.name\",\"uri\",\"user\",\"user.name\"]'] # List[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

    try:
        # Get memberships from a portfolio
        api_response = await api_instance.get_portfolio_memberships_for_portfolio(portfolio_gid, user=user, opt_pretty=opt_pretty, limit=limit, offset=offset, opt_fields=opt_fields)
        print("The response of PortfolioMembershipsApi->get_portfolio_memberships_for_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioMembershipsApi->get_portfolio_memberships_for_portfolio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **user** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **opt_pretty** | **bool**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39; | [optional] 
 **opt_fields** | [**List[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GetPortfolioMemberships200Response**](GetPortfolioMemberships200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the requested portfolio&#39;s memberships. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

