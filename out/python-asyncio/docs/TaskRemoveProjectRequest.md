# TaskRemoveProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | The project to remove the task from. | 

## Example

```python
from asana_asyncio.models.task_remove_project_request import TaskRemoveProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskRemoveProjectRequest from a JSON string
task_remove_project_request_instance = TaskRemoveProjectRequest.from_json(json)
# print the JSON string representation of the object
print(TaskRemoveProjectRequest.to_json())

# convert the object into a dict
task_remove_project_request_dict = task_remove_project_request_instance.to_dict()
# create an instance of TaskRemoveProjectRequest from a dict
task_remove_project_request_from_dict = TaskRemoveProjectRequest.from_dict(task_remove_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


