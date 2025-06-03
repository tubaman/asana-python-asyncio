# InsertEnumOptionForCustomFieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EnumOptionInsertRequest**](EnumOptionInsertRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.insert_enum_option_for_custom_field_request import InsertEnumOptionForCustomFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsertEnumOptionForCustomFieldRequest from a JSON string
insert_enum_option_for_custom_field_request_instance = InsertEnumOptionForCustomFieldRequest.from_json(json)
# print the JSON string representation of the object
print(InsertEnumOptionForCustomFieldRequest.to_json())

# convert the object into a dict
insert_enum_option_for_custom_field_request_dict = insert_enum_option_for_custom_field_request_instance.to_dict()
# create an instance of InsertEnumOptionForCustomFieldRequest from a dict
insert_enum_option_for_custom_field_request_from_dict = InsertEnumOptionForCustomFieldRequest.from_dict(insert_enum_option_for_custom_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


