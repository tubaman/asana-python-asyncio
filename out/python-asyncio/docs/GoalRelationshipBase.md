# GoalRelationshipBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**supporting_resource** | [**GoalRelationshipCompactAllOfSupportingResource**](GoalRelationshipCompactAllOfSupportingResource.md) |  | [optional] 
**contribution_weight** | **float** | The weight that the supporting resource&#39;s progress contributes to the supported goal&#39;s progress. This can only be 0 or 1. | [optional] 
**supported_goal** | [**GoalRelationshipBaseAllOfSupportedGoal**](GoalRelationshipBaseAllOfSupportedGoal.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.goal_relationship_base import GoalRelationshipBase

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRelationshipBase from a JSON string
goal_relationship_base_instance = GoalRelationshipBase.from_json(json)
# print the JSON string representation of the object
print GoalRelationshipBase.to_json()

# convert the object into a dict
goal_relationship_base_dict = goal_relationship_base_instance.to_dict()
# create an instance of GoalRelationshipBase from a dict
goal_relationship_base_form_dict = goal_relationship_base.from_dict(goal_relationship_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

