# CustomFieldSettingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**project** | [**CustomFieldSettingResponseAllOfProject**](CustomFieldSettingResponseAllOfProject.md) |  | [optional] 
**is_important** | **bool** | &#x60;is_important&#x60; is used in the Asana web application to determine if this custom field is displayed in the list/grid view of a project or portfolio. | [optional] [readonly] 
**parent** | [**CustomFieldSettingResponseAllOfParent**](CustomFieldSettingResponseAllOfParent.md) |  | [optional] 
**custom_field** | [**CustomFieldSettingResponseAllOfCustomField**](CustomFieldSettingResponseAllOfCustomField.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.custom_field_setting_response import CustomFieldSettingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldSettingResponse from a JSON string
custom_field_setting_response_instance = CustomFieldSettingResponse.from_json(json)
# print the JSON string representation of the object
print CustomFieldSettingResponse.to_json()

# convert the object into a dict
custom_field_setting_response_dict = custom_field_setting_response_instance.to_dict()
# create an instance of CustomFieldSettingResponse from a dict
custom_field_setting_response_form_dict = custom_field_setting_response.from_dict(custom_field_setting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


