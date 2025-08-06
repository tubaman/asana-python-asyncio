# asana_asyncio.ExportsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_graph_export**](ExportsApi.md#create_graph_export) | **POST** /exports/graph | Initiate a graph export


# **create_graph_export**
> CreateGraphExport201Response create_graph_export(create_graph_export_request)

Initiate a graph export

Initiates a graph export job for a given parent object
(team, portfolio, or project). The export will be processed asynchronously.
Once initiated, use the [jobs](/reference/getjob) endpoint to monitor progress.

**Export Caching:** When exporting more than 1,000 tasks, the results are cached for 4 hours. Any new export requests made within this 4-hour window will return the same cached results rather than generating a fresh export.

### Example

* Bearer Authentication (personalAccessToken):
* OAuth Authentication (oauth2):

```python
import asana_asyncio
from asana_asyncio.models.create_graph_export201_response import CreateGraphExport201Response
from asana_asyncio.models.create_graph_export_request import CreateGraphExportRequest
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
    api_instance = asana_asyncio.ExportsApi(api_client)
    create_graph_export_request = asana_asyncio.CreateGraphExportRequest() # CreateGraphExportRequest | A JSON payload specifying the parent object to export.

    try:
        # Initiate a graph export
        api_response = await api_instance.create_graph_export(create_graph_export_request)
        print("The response of ExportsApi->create_graph_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportsApi->create_graph_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_graph_export_request** | [**CreateGraphExportRequest**](CreateGraphExportRequest.md)| A JSON payload specifying the parent object to export. | 

### Return type

[**CreateGraphExport201Response**](CreateGraphExport201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created Graph export request. |  -  |
**400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
**401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
**403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
**404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
**500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

