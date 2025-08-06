# EnumOptionInsertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enum_option** | **str** | The gid of the enum option to relocate. | 
**before_enum_option** | **str** | An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option. | [optional] 
**after_enum_option** | **str** | An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option. | [optional] 

## Example

```python
from asana_asyncio.models.enum_option_insert_request import EnumOptionInsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnumOptionInsertRequest from a JSON string
enum_option_insert_request_instance = EnumOptionInsertRequest.from_json(json)
# print the JSON string representation of the object
print(EnumOptionInsertRequest.to_json())

# convert the object into a dict
enum_option_insert_request_dict = enum_option_insert_request_instance.to_dict()
# create an instance of EnumOptionInsertRequest from a dict
enum_option_insert_request_from_dict = EnumOptionInsertRequest.from_dict(enum_option_insert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


