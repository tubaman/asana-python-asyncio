# AsanaResource

A generic Asana Resource, containing a globally unique identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.asana_resource import AsanaResource

# TODO update the JSON string below
json = "{}"
# create an instance of AsanaResource from a JSON string
asana_resource_instance = AsanaResource.from_json(json)
# print the JSON string representation of the object
print(AsanaResource.to_json())

# convert the object into a dict
asana_resource_dict = asana_resource_instance.to_dict()
# create an instance of AsanaResource from a dict
asana_resource_from_dict = AsanaResource.from_dict(asana_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


