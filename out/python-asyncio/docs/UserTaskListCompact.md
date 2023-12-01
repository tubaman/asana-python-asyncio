# UserTaskListCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the user task list. | [optional] 
**owner** | [**UserTaskListCompactAllOfOwner**](UserTaskListCompactAllOfOwner.md) |  | [optional] 
**workspace** | [**UserTaskListCompactAllOfWorkspace**](UserTaskListCompactAllOfWorkspace.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.user_task_list_compact import UserTaskListCompact

# TODO update the JSON string below
json = "{}"
# create an instance of UserTaskListCompact from a JSON string
user_task_list_compact_instance = UserTaskListCompact.from_json(json)
# print the JSON string representation of the object
print UserTaskListCompact.to_json()

# convert the object into a dict
user_task_list_compact_dict = user_task_list_compact_instance.to_dict()
# create an instance of UserTaskListCompact from a dict
user_task_list_compact_form_dict = user_task_list_compact.from_dict(user_task_list_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


