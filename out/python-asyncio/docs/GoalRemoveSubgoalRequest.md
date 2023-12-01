# GoalRemoveSubgoalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subgoal** | **str** | The goal gid to remove as subgoal from the parent goal | 

## Example

```python
from asana_asyncio.models.goal_remove_subgoal_request import GoalRemoveSubgoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRemoveSubgoalRequest from a JSON string
goal_remove_subgoal_request_instance = GoalRemoveSubgoalRequest.from_json(json)
# print the JSON string representation of the object
print GoalRemoveSubgoalRequest.to_json()

# convert the object into a dict
goal_remove_subgoal_request_dict = goal_remove_subgoal_request_instance.to_dict()
# create an instance of GoalRemoveSubgoalRequest from a dict
goal_remove_subgoal_request_form_dict = goal_remove_subgoal_request.from_dict(goal_remove_subgoal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


