# GoalAddSubgoalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subgoal** | **str** | The goal gid to add as subgoal to a parent goal | 
**insert_before** | **str** | An id of a subgoal of this parent goal. The new subgoal will be added before the one specified here. &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. | [optional] 
**insert_after** | **str** | An id of a subgoal of this parent goal. The new subgoal will be added after the one specified here. &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. | [optional] 

## Example

```python
from asana_asyncio.models.goal_add_subgoal_request import GoalAddSubgoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalAddSubgoalRequest from a JSON string
goal_add_subgoal_request_instance = GoalAddSubgoalRequest.from_json(json)
# print the JSON string representation of the object
print(GoalAddSubgoalRequest.to_json())

# convert the object into a dict
goal_add_subgoal_request_dict = goal_add_subgoal_request_instance.to_dict()
# create an instance of GoalAddSubgoalRequest from a dict
goal_add_subgoal_request_from_dict = GoalAddSubgoalRequest.from_dict(goal_add_subgoal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


