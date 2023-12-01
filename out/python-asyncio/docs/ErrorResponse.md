# ErrorResponse

Sadly, sometimes requests to the API are not successful. Failures can occur for a wide range of reasons. In all cases, the API should return an HTTP Status Code that indicates the nature of the failure, with a response body in JSON format containing additional information.   In the event of a server error the response body will contain an error phrase. These phrases are automatically generated using the [node-asana-phrase library](https://github.com/Asana/node-asana-phrase) and can be used by Asana support to quickly look up the incident that caused the server error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print ErrorResponse.to_json()

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_form_dict = error_response.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


