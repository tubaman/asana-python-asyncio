# GoalCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the goal. | [optional] 
**owner** | [**GoalCompactAllOfOwner**](GoalCompactAllOfOwner.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.goal_compact import GoalCompact

# TODO update the JSON string below
json = "{}"
# create an instance of GoalCompact from a JSON string
goal_compact_instance = GoalCompact.from_json(json)
# print the JSON string representation of the object
print GoalCompact.to_json()

# convert the object into a dict
goal_compact_dict = goal_compact_instance.to_dict()
# create an instance of GoalCompact from a dict
goal_compact_form_dict = goal_compact.from_dict(goal_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


