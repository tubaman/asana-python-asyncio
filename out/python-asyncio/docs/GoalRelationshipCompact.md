# GoalRelationshipCompact

A *goal relationship* is an object representing the relationship between a goal and another goal, a project, a task, or a portfolio.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**supporting_resource** | [**GoalRelationshipCompactSupportingResource**](GoalRelationshipCompactSupportingResource.md) |  | [optional] 
**contribution_weight** | **float** | The weight that the supporting resource&#39;s progress contributes to the supported goal&#39;s progress. This can be 0, 1, or any value in between. | [optional] 

## Example

```python
from asana_asyncio.models.goal_relationship_compact import GoalRelationshipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRelationshipCompact from a JSON string
goal_relationship_compact_instance = GoalRelationshipCompact.from_json(json)
# print the JSON string representation of the object
print(GoalRelationshipCompact.to_json())

# convert the object into a dict
goal_relationship_compact_dict = goal_relationship_compact_instance.to_dict()
# create an instance of GoalRelationshipCompact from a dict
goal_relationship_compact_from_dict = GoalRelationshipCompact.from_dict(goal_relationship_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


