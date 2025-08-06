# CreateEnumOptionForCustomFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EnumOptionRequest**](EnumOptionRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_enum_option_for_custom_field_request import CreateEnumOptionForCustomFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEnumOptionForCustomFieldRequest from a JSON string
create_enum_option_for_custom_field_request_instance = CreateEnumOptionForCustomFieldRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEnumOptionForCustomFieldRequest.to_json())

# convert the object into a dict
create_enum_option_for_custom_field_request_dict = create_enum_option_for_custom_field_request_instance.to_dict()
# create an instance of CreateEnumOptionForCustomFieldRequest from a dict
create_enum_option_for_custom_field_request_from_dict = CreateEnumOptionForCustomFieldRequest.from_dict(create_enum_option_for_custom_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


