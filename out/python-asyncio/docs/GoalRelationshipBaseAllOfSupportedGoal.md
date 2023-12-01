# GoalRelationshipBaseAllOfSupportedGoal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the goal. | [optional] 
**owner** | [**GoalCompactAllOfOwner**](GoalCompactAllOfOwner.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.goal_relationship_base_all_of_supported_goal import GoalRelationshipBaseAllOfSupportedGoal

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRelationshipBaseAllOfSupportedGoal from a JSON string
goal_relationship_base_all_of_supported_goal_instance = GoalRelationshipBaseAllOfSupportedGoal.from_json(json)
# print the JSON string representation of the object
print GoalRelationshipBaseAllOfSupportedGoal.to_json()

# convert the object into a dict
goal_relationship_base_all_of_supported_goal_dict = goal_relationship_base_all_of_supported_goal_instance.to_dict()
# create an instance of GoalRelationshipBaseAllOfSupportedGoal from a dict
goal_relationship_base_all_of_supported_goal_form_dict = goal_relationship_base_all_of_supported_goal.from_dict(goal_relationship_base_all_of_supported_goal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


