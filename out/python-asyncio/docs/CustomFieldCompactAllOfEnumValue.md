# CustomFieldCompactAllOfEnumValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the enum option. | [optional] 
**enabled** | **bool** | Whether or not the enum option is a selectable value for the custom field. | [optional] 
**color** | **str** | The color of the enum option. Defaults to ‘none’. | [optional] 

## Example

```python
from asana_asyncio.models.custom_field_compact_all_of_enum_value import CustomFieldCompactAllOfEnumValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldCompactAllOfEnumValue from a JSON string
custom_field_compact_all_of_enum_value_instance = CustomFieldCompactAllOfEnumValue.from_json(json)
# print the JSON string representation of the object
print CustomFieldCompactAllOfEnumValue.to_json()

# convert the object into a dict
custom_field_compact_all_of_enum_value_dict = custom_field_compact_all_of_enum_value_instance.to_dict()
# create an instance of CustomFieldCompactAllOfEnumValue from a dict
custom_field_compact_all_of_enum_value_form_dict = custom_field_compact_all_of_enum_value.from_dict(custom_field_compact_all_of_enum_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


