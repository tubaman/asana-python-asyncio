# CustomTypeStatusOptionCompact

A generic Asana Resource, containing a globally unique identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the custom type status option. | [optional] 

## Example

```python
from asana_asyncio.models.custom_type_status_option_compact import CustomTypeStatusOptionCompact

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTypeStatusOptionCompact from a JSON string
custom_type_status_option_compact_instance = CustomTypeStatusOptionCompact.from_json(json)
# print the JSON string representation of the object
print(CustomTypeStatusOptionCompact.to_json())

# convert the object into a dict
custom_type_status_option_compact_dict = custom_type_status_option_compact_instance.to_dict()
# create an instance of CustomTypeStatusOptionCompact from a dict
custom_type_status_option_compact_from_dict = CustomTypeStatusOptionCompact.from_dict(custom_type_status_option_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


