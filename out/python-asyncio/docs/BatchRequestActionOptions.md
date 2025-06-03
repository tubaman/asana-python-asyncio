# BatchRequestActionOptions

Pagination (`limit` and `offset`) and output options (`fields` or `expand`) for the action. “Pretty” JSON output is not an available option on individual actions; if you want pretty output, specify that option on the parent request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Pagination limit for the request. | [optional] 
**offset** | **int** | Pagination offset for the request. | [optional] 
**fields** | **List[str]** | The fields to retrieve in the request. | [optional] 

## Example

```python
from asana_asyncio.models.batch_request_action_options import BatchRequestActionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRequestActionOptions from a JSON string
batch_request_action_options_instance = BatchRequestActionOptions.from_json(json)
# print the JSON string representation of the object
print(BatchRequestActionOptions.to_json())

# convert the object into a dict
batch_request_action_options_dict = batch_request_action_options_instance.to_dict()
# create an instance of BatchRequestActionOptions from a dict
batch_request_action_options_from_dict = BatchRequestActionOptions.from_dict(batch_request_action_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


