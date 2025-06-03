# TaskAddProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | The project to add the task to. | 
**insert_after** | **str** | A task in the project to insert the task after, or &#x60;null&#x60; to insert at the beginning of the list. | [optional] 
**insert_before** | **str** | A task in the project to insert the task before, or &#x60;null&#x60; to insert at the end of the list. | [optional] 
**section** | **str** | A section in the project to insert the task into. The task will be inserted at the bottom of the section. | [optional] 

## Example

```python
from asana_asyncio.models.task_add_project_request import TaskAddProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskAddProjectRequest from a JSON string
task_add_project_request_instance = TaskAddProjectRequest.from_json(json)
# print the JSON string representation of the object
print(TaskAddProjectRequest.to_json())

# convert the object into a dict
task_add_project_request_dict = task_add_project_request_instance.to_dict()
# create an instance of TaskAddProjectRequest from a dict
task_add_project_request_from_dict = TaskAddProjectRequest.from_dict(task_add_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


