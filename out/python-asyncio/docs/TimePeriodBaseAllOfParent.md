# TimePeriodBaseAllOfParent


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
from asana_asyncio.models.time_period_base_all_of_parent import TimePeriodBaseAllOfParent

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodBaseAllOfParent from a JSON string
time_period_base_all_of_parent_instance = TimePeriodBaseAllOfParent.from_json(json)
# print the JSON string representation of the object
print TimePeriodBaseAllOfParent.to_json()

# convert the object into a dict
time_period_base_all_of_parent_dict = time_period_base_all_of_parent_instance.to_dict()
# create an instance of TimePeriodBaseAllOfParent from a dict
time_period_base_all_of_parent_form_dict = time_period_base_all_of_parent.from_dict(time_period_base_all_of_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


