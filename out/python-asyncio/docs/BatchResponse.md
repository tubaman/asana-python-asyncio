# BatchResponse

A response object returned from a batch request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | The HTTP status code that the invoked endpoint returned. | [optional] 
**headers** | **object** | A map of HTTP headers specific to this result. This is primarily used for returning a &#x60;Location&#x60; header to accompany a &#x60;201 Created&#x60; result.  The parent HTTP response will contain all common headers. | [optional] 
**body** | **object** | The JSON body that the invoked endpoint returned. | [optional] 

## Example

```python
from asana_asyncio.models.batch_response import BatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResponse from a JSON string
batch_response_instance = BatchResponse.from_json(json)
# print the JSON string representation of the object
print(BatchResponse.to_json())

# convert the object into a dict
batch_response_dict = batch_response_instance.to_dict()
# create an instance of BatchResponse from a dict
batch_response_from_dict = BatchResponse.from_dict(batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


