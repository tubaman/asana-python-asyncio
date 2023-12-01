# GoalRelationshipCompactAllOfSupportingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 

## Example

```python
from asana_asyncio.models.goal_relationship_compact_all_of_supporting_resource import GoalRelationshipCompactAllOfSupportingResource

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRelationshipCompactAllOfSupportingResource from a JSON string
goal_relationship_compact_all_of_supporting_resource_instance = GoalRelationshipCompactAllOfSupportingResource.from_json(json)
# print the JSON string representation of the object
print GoalRelationshipCompactAllOfSupportingResource.to_json()

# convert the object into a dict
goal_relationship_compact_all_of_supporting_resource_dict = goal_relationship_compact_all_of_supporting_resource_instance.to_dict()
# create an instance of GoalRelationshipCompactAllOfSupportingResource from a dict
goal_relationship_compact_all_of_supporting_resource_form_dict = goal_relationship_compact_all_of_supporting_resource.from_dict(goal_relationship_compact_all_of_supporting_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


