# TaskDuplicateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new task. | [optional] 
**include** | **str** | A comma-separated list of fields that will be duplicated to the new task. ##### Fields - assignee - attachments - dates - dependencies - followers - notes - parent - projects - subtasks - tags | [optional] 

## Example

```python
from asana_asyncio.models.task_duplicate_request import TaskDuplicateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDuplicateRequest from a JSON string
task_duplicate_request_instance = TaskDuplicateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskDuplicateRequest.to_json())

# convert the object into a dict
task_duplicate_request_dict = task_duplicate_request_instance.to_dict()
# create an instance of TaskDuplicateRequest from a dict
task_duplicate_request_from_dict = TaskDuplicateRequest.from_dict(task_duplicate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


