# GoalResponseAllOfWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the workspace. | [optional] 

## Example

```python
from asana_asyncio.models.goal_response_all_of_workspace import GoalResponseAllOfWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of GoalResponseAllOfWorkspace from a JSON string
goal_response_all_of_workspace_instance = GoalResponseAllOfWorkspace.from_json(json)
# print the JSON string representation of the object
print GoalResponseAllOfWorkspace.to_json()

# convert the object into a dict
goal_response_all_of_workspace_dict = goal_response_all_of_workspace_instance.to_dict()
# create an instance of GoalResponseAllOfWorkspace from a dict
goal_response_all_of_workspace_form_dict = goal_response_all_of_workspace.from_dict(goal_response_all_of_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


