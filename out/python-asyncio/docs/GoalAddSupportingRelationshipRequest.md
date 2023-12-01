# GoalAddSupportingRelationshipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supporting_resource** | **str** | The gid of the supporting resource to add to the parent goal. Must be the gid of a goal, project, task, or portfolio. | 
**insert_before** | **str** | An id of a subgoal of this parent goal. The new subgoal will be added before the one specified here. &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. Currently only supported when adding a subgoal. | [optional] 
**insert_after** | **str** | An id of a subgoal of this parent goal. The new subgoal will be added after the one specified here. &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. Currently only supported when adding a subgoal. | [optional] 
**contribution_weight** | **float** | The weight that the supporting resource&#39;s progress will contribute to the supported goal&#39;s progress. This can only be 0 or 1. | [optional] 

## Example

```python
from asana_asyncio.models.goal_add_supporting_relationship_request import GoalAddSupportingRelationshipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalAddSupportingRelationshipRequest from a JSON string
goal_add_supporting_relationship_request_instance = GoalAddSupportingRelationshipRequest.from_json(json)
# print the JSON string representation of the object
print GoalAddSupportingRelationshipRequest.to_json()

# convert the object into a dict
goal_add_supporting_relationship_request_dict = goal_add_supporting_relationship_request_instance.to_dict()
# create an instance of GoalAddSupportingRelationshipRequest from a dict
goal_add_supporting_relationship_request_form_dict = goal_add_supporting_relationship_request.from_dict(goal_add_supporting_relationship_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


