# TaskResponseAllOfAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.task_response_all_of_assignee import TaskResponseAllOfAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponseAllOfAssignee from a JSON string
task_response_all_of_assignee_instance = TaskResponseAllOfAssignee.from_json(json)
# print the JSON string representation of the object
print TaskResponseAllOfAssignee.to_json()

# convert the object into a dict
task_response_all_of_assignee_dict = task_response_all_of_assignee_instance.to_dict()
# create an instance of TaskResponseAllOfAssignee from a dict
task_response_all_of_assignee_form_dict = task_response_all_of_assignee.from_dict(task_response_all_of_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


