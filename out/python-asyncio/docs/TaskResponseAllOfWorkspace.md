# TaskResponseAllOfWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the workspace. | [optional] 

## Example

```python
from asana_asyncio.models.task_response_all_of_workspace import TaskResponseAllOfWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponseAllOfWorkspace from a JSON string
task_response_all_of_workspace_instance = TaskResponseAllOfWorkspace.from_json(json)
# print the JSON string representation of the object
print(TaskResponseAllOfWorkspace.to_json())

# convert the object into a dict
task_response_all_of_workspace_dict = task_response_all_of_workspace_instance.to_dict()
# create an instance of TaskResponseAllOfWorkspace from a dict
task_response_all_of_workspace_from_dict = TaskResponseAllOfWorkspace.from_dict(task_response_all_of_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


