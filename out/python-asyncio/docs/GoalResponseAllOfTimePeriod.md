# GoalResponseAllOfTimePeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**end_on** | **str** | The localized end date of the time period in &#x60;YYYY-MM-DD&#x60; format. | [optional] 
**start_on** | **str** | The localized start date of the time period in &#x60;YYYY-MM-DD&#x60; format. | [optional] 
**period** | **str** | The cadence and index of the time period. The value is one of: &#x60;FY&#x60;, &#x60;H1&#x60;, &#x60;H2&#x60;, &#x60;Q1&#x60;, &#x60;Q2&#x60;, &#x60;Q3&#x60;, or &#x60;Q4&#x60;. | [optional] 
**display_name** | **str** | A string representing the cadence code and the fiscal year. | [optional] 

## Example

```python
from asana_asyncio.models.goal_response_all_of_time_period import GoalResponseAllOfTimePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of GoalResponseAllOfTimePeriod from a JSON string
goal_response_all_of_time_period_instance = GoalResponseAllOfTimePeriod.from_json(json)
# print the JSON string representation of the object
print GoalResponseAllOfTimePeriod.to_json()

# convert the object into a dict
goal_response_all_of_time_period_dict = goal_response_all_of_time_period_instance.to_dict()
# create an instance of GoalResponseAllOfTimePeriod from a dict
goal_response_all_of_time_period_form_dict = goal_response_all_of_time_period.from_dict(goal_response_all_of_time_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


