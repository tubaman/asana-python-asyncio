# CustomTypeCompact

Custom Types extend the types of Asana Objects, currently only Custom Tasks are supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the custom type. | [optional] 

## Example

```python
from asana_asyncio.models.custom_type_compact import CustomTypeCompact

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTypeCompact from a JSON string
custom_type_compact_instance = CustomTypeCompact.from_json(json)
# print the JSON string representation of the object
print(CustomTypeCompact.to_json())

# convert the object into a dict
custom_type_compact_dict = custom_type_compact_instance.to_dict()
# create an instance of CustomTypeCompact from a dict
custom_type_compact_from_dict = CustomTypeCompact.from_dict(custom_type_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


