# TaskSetParentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **str** | The new parent of the task, or &#x60;null&#x60; for no parent. | 
**insert_after** | **str** | A subtask of the parent to insert the task after, or &#x60;null&#x60; to insert at the beginning of the list. | [optional] 
**insert_before** | **str** | A subtask of the parent to insert the task before, or &#x60;null&#x60; to insert at the end of the list. | [optional] 

## Example

```python
from asana_asyncio.models.task_set_parent_request import TaskSetParentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSetParentRequest from a JSON string
task_set_parent_request_instance = TaskSetParentRequest.from_json(json)
# print the JSON string representation of the object
print TaskSetParentRequest.to_json()

# convert the object into a dict
task_set_parent_request_dict = task_set_parent_request_instance.to_dict()
# create an instance of TaskSetParentRequest from a dict
task_set_parent_request_form_dict = task_set_parent_request.from_dict(task_set_parent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


