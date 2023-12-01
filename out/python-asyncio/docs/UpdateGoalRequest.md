# UpdateGoalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoalUpdateRequest**](GoalUpdateRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_goal_request import UpdateGoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalRequest from a JSON string
update_goal_request_instance = UpdateGoalRequest.from_json(json)
# print the JSON string representation of the object
print UpdateGoalRequest.to_json()

# convert the object into a dict
update_goal_request_dict = update_goal_request_instance.to_dict()
# create an instance of UpdateGoalRequest from a dict
update_goal_request_form_dict = update_goal_request.from_dict(update_goal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


