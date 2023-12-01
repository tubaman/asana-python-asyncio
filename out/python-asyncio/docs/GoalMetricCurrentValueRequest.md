# GoalMetricCurrentValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**current_number_value** | **float** | *Conditional*. This number is the current value of a goal metric of type number. | [optional] 

## Example

```python
from asana_asyncio.models.goal_metric_current_value_request import GoalMetricCurrentValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalMetricCurrentValueRequest from a JSON string
goal_metric_current_value_request_instance = GoalMetricCurrentValueRequest.from_json(json)
# print the JSON string representation of the object
print GoalMetricCurrentValueRequest.to_json()

# convert the object into a dict
goal_metric_current_value_request_dict = goal_metric_current_value_request_instance.to_dict()
# create an instance of GoalMetricCurrentValueRequest from a dict
goal_metric_current_value_request_form_dict = goal_metric_current_value_request.from_dict(goal_metric_current_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


