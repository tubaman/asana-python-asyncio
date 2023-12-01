# GoalMetricBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**precision** | **int** | *Conditional*. Only relevant for goal metrics of type ‘Number’. This field dictates the number of places after the decimal to round to, i.e. 0 is integer values, 1 rounds to the nearest tenth, and so on. Must be between 0 and 6, inclusive. For percentage format, this may be unintuitive, as a value of 0.25 has a precision of 0, while a value of 0.251 has a precision of 1. This is due to 0.25 being displayed as 25%. | [optional] 
**unit** | **str** | A supported unit of measure for the goal metric, or none. | [optional] 
**currency_code** | **str** | ISO 4217 currency code to format this custom field. This will be null if the &#x60;unit&#x60; is not &#x60;currency&#x60;. | [optional] 
**initial_number_value** | **float** | This number is the start value of a goal metric of type number. | [optional] 
**target_number_value** | **float** | This number is the end value of a goal metric of type number. This number cannot equal &#x60;initial_number_value&#x60;. | [optional] 
**current_number_value** | **float** | This number is the current value of a goal metric of type number. | [optional] 
**current_display_value** | **str** | This string is the current value of a goal metric of type string. | [optional] [readonly] 
**progress_source** | **str** | This field defines how the progress value of a goal metric is being calculated. A goal&#39;s progress can be provided manually by the user, calculated automatically from contributing subgoals, projects, or tasks, or managed by an integration with an external data source, such as Salesforce. | [optional] 

## Example

```python
from asana_asyncio.models.goal_metric_base import GoalMetricBase

# TODO update the JSON string below
json = "{}"
# create an instance of GoalMetricBase from a JSON string
goal_metric_base_instance = GoalMetricBase.from_json(json)
# print the JSON string representation of the object
print GoalMetricBase.to_json()

# convert the object into a dict
goal_metric_base_dict = goal_metric_base_instance.to_dict()
# create an instance of GoalMetricBase from a dict
goal_metric_base_form_dict = goal_metric_base.from_dict(goal_metric_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

