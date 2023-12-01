# SetParentForTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskSetParentRequest**](TaskSetParentRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.set_parent_for_task_request import SetParentForTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetParentForTaskRequest from a JSON string
set_parent_for_task_request_instance = SetParentForTaskRequest.from_json(json)
# print the JSON string representation of the object
print SetParentForTaskRequest.to_json()

# convert the object into a dict
set_parent_for_task_request_dict = set_parent_for_task_request_instance.to_dict()
# create an instance of SetParentForTaskRequest from a dict
set_parent_for_task_request_form_dict = set_parent_for_task_request.from_dict(set_parent_for_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


