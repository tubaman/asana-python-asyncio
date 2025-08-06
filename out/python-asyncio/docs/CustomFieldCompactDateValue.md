# CustomFieldCompactDateValue

*Conditional*. Only relevant for custom fields of type `date`. This object reflects the chosen date (and optionally, time) value of a `date` custom field. If no date is selected, the value of `date_value` will be `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | A string representing the date in YYYY-MM-DD format. | [optional] 
**date_time** | **str** | A string representing the date in ISO 8601 format. If no time value is selected, the value of &#x60;date-time&#x60; will be &#x60;null&#x60;. | [optional] 

## Example

```python
from asana_asyncio.models.custom_field_compact_date_value import CustomFieldCompactDateValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldCompactDateValue from a JSON string
custom_field_compact_date_value_instance = CustomFieldCompactDateValue.from_json(json)
# print the JSON string representation of the object
print(CustomFieldCompactDateValue.to_json())

# convert the object into a dict
custom_field_compact_date_value_dict = custom_field_compact_date_value_instance.to_dict()
# create an instance of CustomFieldCompactDateValue from a dict
custom_field_compact_date_value_from_dict = CustomFieldCompactDateValue.from_dict(custom_field_compact_date_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


