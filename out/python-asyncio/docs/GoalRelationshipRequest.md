# GoalRelationshipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**supporting_resource** | [**GoalRelationshipCompactSupportingResource**](GoalRelationshipCompactSupportingResource.md) |  | [optional] 
**contribution_weight** | **float** | The weight that the supporting resource&#39;s progress contributes to the supported goal&#39;s progress. This can be 0, 1, or any value in between. | [optional] 
**supported_goal** | [**GoalRelationshipBaseAllOfSupportedGoal**](GoalRelationshipBaseAllOfSupportedGoal.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.goal_relationship_request import GoalRelationshipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRelationshipRequest from a JSON string
goal_relationship_request_instance = GoalRelationshipRequest.from_json(json)
# print the JSON string representation of the object
print(GoalRelationshipRequest.to_json())

# convert the object into a dict
goal_relationship_request_dict = goal_relationship_request_instance.to_dict()
# create an instance of GoalRelationshipRequest from a dict
goal_relationship_request_from_dict = GoalRelationshipRequest.from_dict(goal_relationship_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


