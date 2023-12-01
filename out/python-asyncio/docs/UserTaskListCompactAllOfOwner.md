# UserTaskListCompactAllOfOwner

The owner of the user task list, i.e. the person whose My Tasks is represented by this resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.user_task_list_compact_all_of_owner import UserTaskListCompactAllOfOwner

# TODO update the JSON string below
json = "{}"
# create an instance of UserTaskListCompactAllOfOwner from a JSON string
user_task_list_compact_all_of_owner_instance = UserTaskListCompactAllOfOwner.from_json(json)
# print the JSON string representation of the object
print UserTaskListCompactAllOfOwner.to_json()

# convert the object into a dict
user_task_list_compact_all_of_owner_dict = user_task_list_compact_all_of_owner_instance.to_dict()
# create an instance of UserTaskListCompactAllOfOwner from a dict
user_task_list_compact_all_of_owner_form_dict = user_task_list_compact_all_of_owner.from_dict(user_task_list_compact_all_of_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


