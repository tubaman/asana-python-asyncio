# UpdateGoalMetricRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoalMetricCurrentValueRequest**](GoalMetricCurrentValueRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_goal_metric_request import UpdateGoalMetricRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalMetricRequest from a JSON string
update_goal_metric_request_instance = UpdateGoalMetricRequest.from_json(json)
# print the JSON string representation of the object
print UpdateGoalMetricRequest.to_json()

# convert the object into a dict
update_goal_metric_request_dict = update_goal_metric_request_instance.to_dict()
# create an instance of UpdateGoalMetricRequest from a dict
update_goal_metric_request_form_dict = update_goal_metric_request.from_dict(update_goal_metric_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


