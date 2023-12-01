# CustomFieldSettingResponseAllOfParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 

## Example

```python
from asana_asyncio.models.custom_field_setting_response_all_of_parent import CustomFieldSettingResponseAllOfParent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSettingResponseAllOfParent from a JSON string
custom_field_setting_response_all_of_parent_instance = CustomFieldSettingResponseAllOfParent.from_json(json)
# print the JSON string representation of the object
print CustomFieldSettingResponseAllOfParent.to_json()

# convert the object into a dict
custom_field_setting_response_all_of_parent_dict = custom_field_setting_response_all_of_parent_instance.to_dict()
# create an instance of CustomFieldSettingResponseAllOfParent from a dict
custom_field_setting_response_all_of_parent_form_dict = custom_field_setting_response_all_of_parent.from_dict(custom_field_setting_response_all_of_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


