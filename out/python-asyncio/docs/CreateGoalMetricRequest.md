# CreateGoalMetricRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoalMetricBase**](GoalMetricBase.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_goal_metric_request import CreateGoalMetricRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGoalMetricRequest from a JSON string
create_goal_metric_request_instance = CreateGoalMetricRequest.from_json(json)
# print the JSON string representation of the object
print CreateGoalMetricRequest.to_json()

# convert the object into a dict
create_goal_metric_request_dict = create_goal_metric_request_instance.to_dict()
# create an instance of CreateGoalMetricRequest from a dict
create_goal_metric_request_form_dict = create_goal_metric_request.from_dict(create_goal_metric_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


