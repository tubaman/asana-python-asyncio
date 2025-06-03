# BatchRequestAction

An action object for use in a batch request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relative_path** | **str** | The path of the desired endpoint relative to the API’s base URL. Query parameters are not accepted here; put them in &#x60;data&#x60; instead. | 
**method** | **str** | The HTTP method you wish to emulate for the action. | 
**data** | **object** | For &#x60;GET&#x60; requests, this should be a map of query parameters you would have normally passed in the URL. Options and pagination are not accepted here; put them in &#x60;options&#x60; instead. For &#x60;POST&#x60;, &#x60;PATCH&#x60;, and &#x60;PUT&#x60; methods, this should be the content you would have normally put in the data field of the body. | [optional] 
**options** | [**BatchRequestActionOptions**](BatchRequestActionOptions.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.batch_request_action import BatchRequestAction

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRequestAction from a JSON string
batch_request_action_instance = BatchRequestAction.from_json(json)
# print the JSON string representation of the object
print(BatchRequestAction.to_json())

# convert the object into a dict
batch_request_action_dict = batch_request_action_instance.to_dict()
# create an instance of BatchRequestAction from a dict
batch_request_action_from_dict = BatchRequestAction.from_dict(batch_request_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


