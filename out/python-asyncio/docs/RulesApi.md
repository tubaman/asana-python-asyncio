# asana_asyncio.RulesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_rule**](RulesApi.md#trigger_rule) | **POST** /rule_triggers/{rule_trigger_gid}/run | Trigger a rule


# **trigger_rule**
> TriggerRule200Response trigger_rule(rule_trigger_gid, trigger_rule_request)

Trigger a rule

Trigger a rule which uses an [\"incoming web request\"](/docs/incoming-web-requests) trigger.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import time
import os
import asana_asyncio
from asana_asyncio.models.trigger_rule200_response import TriggerRule200Response
from asana_asyncio.models.trigger_rule_request import TriggerRuleRequest
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
    api_instance = asana_asyncio.RulesApi(api_client)
    rule_trigger_gid = '12345' # str | The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint.
    trigger_rule_request = asana_asyncio.TriggerRuleRequest() # TriggerRuleRequest | A dictionary of variables accessible from within the rule.

    try:
        # Trigger a rule
        api_response = await api_instance.trigger_rule(rule_trigger_gid, trigger_rule_request)
        print("The response of RulesApi->trigger_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->trigger_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_trigger_gid** | **str**| The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint. | 
 **trigger_rule_request** | [**TriggerRuleRequest**](TriggerRuleRequest.md)| A dictionary of variables accessible from within the rule. | 

### Return type

[**TriggerRule200Response**](TriggerRule200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully triggered a rule. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

