# BatchRequest

A request object for use in a batch request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[BatchRequestAction]**](BatchRequestAction.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.batch_request import BatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRequest from a JSON string
batch_request_instance = BatchRequest.from_json(json)
# print the JSON string representation of the object
print BatchRequest.to_json()

# convert the object into a dict
batch_request_dict = batch_request_instance.to_dict()
# create an instance of BatchRequest from a dict
batch_request_form_dict = batch_request.from_dict(batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


