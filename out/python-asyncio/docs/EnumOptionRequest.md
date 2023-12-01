# EnumOptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the enum option. | [optional] 
**enabled** | **bool** | Whether or not the enum option is a selectable value for the custom field. | [optional] 
**color** | **str** | The color of the enum option. Defaults to ‘none’. | [optional] 
**insert_before** | **str** | An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option. | [optional] 
**insert_after** | **str** | An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option. | [optional] 

## Example

```python
from asana_asyncio.models.enum_option_request import EnumOptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnumOptionRequest from a JSON string
enum_option_request_instance = EnumOptionRequest.from_json(json)
# print the JSON string representation of the object
print EnumOptionRequest.to_json()

# convert the object into a dict
enum_option_request_dict = enum_option_request_instance.to_dict()
# create an instance of EnumOptionRequest from a dict
enum_option_request_form_dict = enum_option_request.from_dict(enum_option_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


