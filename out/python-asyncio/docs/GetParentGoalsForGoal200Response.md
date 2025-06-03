# GetParentGoalsForGoal200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GoalCompact]**](GoalCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_parent_goals_for_goal200_response import GetParentGoalsForGoal200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetParentGoalsForGoal200Response from a JSON string
get_parent_goals_for_goal200_response_instance = GetParentGoalsForGoal200Response.from_json(json)
# print the JSON string representation of the object
print(GetParentGoalsForGoal200Response.to_json())

# convert the object into a dict
get_parent_goals_for_goal200_response_dict = get_parent_goals_for_goal200_response_instance.to_dict()
# create an instance of GetParentGoalsForGoal200Response from a dict
get_parent_goals_for_goal200_response_from_dict = GetParentGoalsForGoal200Response.from_dict(get_parent_goals_for_goal200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


