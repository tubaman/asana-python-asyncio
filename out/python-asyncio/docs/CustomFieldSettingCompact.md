# CustomFieldSettingCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.custom_field_setting_compact import CustomFieldSettingCompact

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSettingCompact from a JSON string
custom_field_setting_compact_instance = CustomFieldSettingCompact.from_json(json)
# print the JSON string representation of the object
print CustomFieldSettingCompact.to_json()

# convert the object into a dict
custom_field_setting_compact_dict = custom_field_setting_compact_instance.to_dict()
# create an instance of CustomFieldSettingCompact from a dict
custom_field_setting_compact_form_dict = custom_field_setting_compact.from_dict(custom_field_setting_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


