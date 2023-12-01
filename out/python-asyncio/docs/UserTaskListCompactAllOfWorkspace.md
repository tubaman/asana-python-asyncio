# UserTaskListCompactAllOfWorkspace

The workspace in which the user task list is located.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the workspace. | [optional] 

## Example

```python
from asana_asyncio.models.user_task_list_compact_all_of_workspace import UserTaskListCompactAllOfWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of UserTaskListCompactAllOfWorkspace from a JSON string
user_task_list_compact_all_of_workspace_instance = UserTaskListCompactAllOfWorkspace.from_json(json)
# print the JSON string representation of the object
print UserTaskListCompactAllOfWorkspace.to_json()

# convert the object into a dict
user_task_list_compact_all_of_workspace_dict = user_task_list_compact_all_of_workspace_instance.to_dict()
# create an instance of UserTaskListCompactAllOfWorkspace from a dict
user_task_list_compact_all_of_workspace_form_dict = user_task_list_compact_all_of_workspace.from_dict(user_task_list_compact_all_of_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


