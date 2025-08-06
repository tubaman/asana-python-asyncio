# GoalRelationshipCompactSupportingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 

## Example

```python
from asana_asyncio.models.goal_relationship_compact_supporting_resource import GoalRelationshipCompactSupportingResource

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRelationshipCompactSupportingResource from a JSON string
goal_relationship_compact_supporting_resource_instance = GoalRelationshipCompactSupportingResource.from_json(json)
# print the JSON string representation of the object
print(GoalRelationshipCompactSupportingResource.to_json())

# convert the object into a dict
goal_relationship_compact_supporting_resource_dict = goal_relationship_compact_supporting_resource_instance.to_dict()
# create an instance of GoalRelationshipCompactSupportingResource from a dict
goal_relationship_compact_supporting_resource_from_dict = GoalRelationshipCompactSupportingResource.from_dict(goal_relationship_compact_supporting_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


