# RemoveCustomFieldSettingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field** | **str** | The custom field to remove from this portfolio. | 

## Example

```python
from asana_asyncio.models.remove_custom_field_setting_request import RemoveCustomFieldSettingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCustomFieldSettingRequest from a JSON string
remove_custom_field_setting_request_instance = RemoveCustomFieldSettingRequest.from_json(json)
# print the JSON string representation of the object
print RemoveCustomFieldSettingRequest.to_json()

# convert the object into a dict
remove_custom_field_setting_request_dict = remove_custom_field_setting_request_instance.to_dict()
# create an instance of RemoveCustomFieldSettingRequest from a dict
remove_custom_field_setting_request_form_dict = remove_custom_field_setting_request.from_dict(remove_custom_field_setting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


