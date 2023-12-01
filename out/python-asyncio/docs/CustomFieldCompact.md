# CustomFieldCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the custom field. | [optional] 
**resource_subtype** | **str** | The type of the custom field. Must be one of the given values.  | [optional] [readonly] 
**type** | **str** | *Deprecated: new integrations should prefer the resource_subtype field.* The type of the custom field. Must be one of the given values.  | [optional] [readonly] 
**enum_options** | [**List[EnumOption]**](EnumOption.md) | *Conditional*. Only relevant for custom fields of type &#x60;enum&#x60;. This array specifies the possible values which an &#x60;enum&#x60; custom field can adopt. To modify the enum options, refer to [working with enum options](/reference/createenumoptionforcustomfield). | [optional] 
**enabled** | **bool** | *Conditional*. Determines if the custom field is enabled or not. | [optional] [readonly] 
**is_formula_field** | **bool** | *Conditional*. This flag describes whether a custom field is a formula custom field. | [optional] 
**date_value** | [**CustomFieldCompactAllOfDateValue**](CustomFieldCompactAllOfDateValue.md) |  | [optional] 
**enum_value** | [**CustomFieldCompactAllOfEnumValue**](CustomFieldCompactAllOfEnumValue.md) |  | [optional] 
**multi_enum_values** | [**List[EnumOption]**](EnumOption.md) | *Conditional*. Only relevant for custom fields of type &#x60;multi_enum&#x60;. This object is the chosen values of a &#x60;multi_enum&#x60; custom field. | [optional] 
**number_value** | **float** | *Conditional*. This number is the value of a &#x60;number&#x60; custom field. | [optional] 
**text_value** | **str** | *Conditional*. This string is the value of a &#x60;text&#x60; custom field. | [optional] 
**display_value** | **str** | A string representation for the value of the custom field. Integrations that don&#39;t require the underlying type should use this field to read values. Using this field will future-proof an app against new custom field types. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.custom_field_compact import CustomFieldCompact

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldCompact from a JSON string
custom_field_compact_instance = CustomFieldCompact.from_json(json)
# print the JSON string representation of the object
print CustomFieldCompact.to_json()

# convert the object into a dict
custom_field_compact_dict = custom_field_compact_instance.to_dict()
# create an instance of CustomFieldCompact from a dict
custom_field_compact_form_dict = custom_field_compact.from_dict(custom_field_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


