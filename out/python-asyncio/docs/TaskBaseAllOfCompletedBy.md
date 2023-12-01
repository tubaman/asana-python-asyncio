# TaskBaseAllOfCompletedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.task_base_all_of_completed_by import TaskBaseAllOfCompletedBy

# TODO update the JSON string below
json = "{}"
# create an instance of TaskBaseAllOfCompletedBy from a JSON string
task_base_all_of_completed_by_instance = TaskBaseAllOfCompletedBy.from_json(json)
# print the JSON string representation of the object
print TaskBaseAllOfCompletedBy.to_json()

# convert the object into a dict
task_base_all_of_completed_by_dict = task_base_all_of_completed_by_instance.to_dict()
# create an instance of TaskBaseAllOfCompletedBy from a dict
task_base_all_of_completed_by_form_dict = task_base_all_of_completed_by.from_dict(task_base_all_of_completed_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


