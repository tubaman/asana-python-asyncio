# TaskCountResponse

A response object returned from the task count endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_tasks** | **int** | The number of tasks in a project. | [optional] 
**num_incomplete_tasks** | **int** | The number of incomplete tasks in a project. | [optional] 
**num_completed_tasks** | **int** | The number of completed tasks in a project. | [optional] 
**num_milestones** | **int** | The number of milestones in a project. | [optional] 
**num_incomplete_milestones** | **int** | The number of incomplete milestones in a project. | [optional] 
**num_completed_milestones** | **int** | The number of completed milestones in a project. | [optional] 

## Example

```python
from asana_asyncio.models.task_count_response import TaskCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCountResponse from a JSON string
task_count_response_instance = TaskCountResponse.from_json(json)
# print the JSON string representation of the object
print(TaskCountResponse.to_json())

# convert the object into a dict
task_count_response_dict = task_count_response_instance.to_dict()
# create an instance of TaskCountResponse from a dict
task_count_response_from_dict = TaskCountResponse.from_dict(task_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


