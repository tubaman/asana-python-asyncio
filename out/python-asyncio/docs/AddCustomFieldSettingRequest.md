# AddCustomFieldSettingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field** | [**AddCustomFieldSettingRequestCustomField**](AddCustomFieldSettingRequestCustomField.md) |  | 
**is_important** | **bool** | Whether this field should be considered important to this container (for instance, to display in the list view of items in the container). | [optional] 
**insert_before** | **str** | A gid of a Custom Field Setting on this container, before which the new Custom Field Setting will be added.  &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. | [optional] 
**insert_after** | **str** | A gid of a Custom Field Setting on this container, after which the new Custom Field Setting will be added.  &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. | [optional] 

## Example

```python
from asana_asyncio.models.add_custom_field_setting_request import AddCustomFieldSettingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomFieldSettingRequest from a JSON string
add_custom_field_setting_request_instance = AddCustomFieldSettingRequest.from_json(json)
# print the JSON string representation of the object
print(AddCustomFieldSettingRequest.to_json())

# convert the object into a dict
add_custom_field_setting_request_dict = add_custom_field_setting_request_instance.to_dict()
# create an instance of AddCustomFieldSettingRequest from a dict
add_custom_field_setting_request_from_dict = AddCustomFieldSettingRequest.from_dict(add_custom_field_setting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


