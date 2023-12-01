# EnumOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the enum option. | [optional] 
**enabled** | **bool** | Whether or not the enum option is a selectable value for the custom field. | [optional] 
**color** | **str** | The color of the enum option. Defaults to ‘none’. | [optional] 

## Example

```python
from asana_asyncio.models.enum_option import EnumOption

# TODO update the JSON string below
json = "{}"
# create an instance of EnumOption from a JSON string
enum_option_instance = EnumOption.from_json(json)
# print the JSON string representation of the object
print EnumOption.to_json()

# convert the object into a dict
enum_option_dict = enum_option_instance.to_dict()
# create an instance of EnumOption from a dict
enum_option_form_dict = enum_option.from_dict(enum_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


