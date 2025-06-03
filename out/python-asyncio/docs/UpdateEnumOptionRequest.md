# UpdateEnumOptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EnumOption**](EnumOption.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_enum_option_request import UpdateEnumOptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEnumOptionRequest from a JSON string
update_enum_option_request_instance = UpdateEnumOptionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEnumOptionRequest.to_json())

# convert the object into a dict
update_enum_option_request_dict = update_enum_option_request_instance.to_dict()
# create an instance of UpdateEnumOptionRequest from a dict
update_enum_option_request_from_dict = UpdateEnumOptionRequest.from_dict(update_enum_option_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


