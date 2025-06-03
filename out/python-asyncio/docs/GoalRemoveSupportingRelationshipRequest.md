# GoalRemoveSupportingRelationshipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supporting_resource** | **str** | The gid of the supporting resource to remove from the parent goal. Must be the gid of a goal, project, task, or portfolio. | 

## Example

```python
from asana_asyncio.models.goal_remove_supporting_relationship_request import GoalRemoveSupportingRelationshipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRemoveSupportingRelationshipRequest from a JSON string
goal_remove_supporting_relationship_request_instance = GoalRemoveSupportingRelationshipRequest.from_json(json)
# print the JSON string representation of the object
print(GoalRemoveSupportingRelationshipRequest.to_json())

# convert the object into a dict
goal_remove_supporting_relationship_request_dict = goal_remove_supporting_relationship_request_instance.to_dict()
# create an instance of GoalRemoveSupportingRelationshipRequest from a dict
goal_remove_supporting_relationship_request_from_dict = GoalRemoveSupportingRelationshipRequest.from_dict(goal_remove_supporting_relationship_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


