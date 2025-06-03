# AllocationBase

A generic Asana Resource, containing a globally unique identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**start_date** | **date** | The localized day on which the allocation starts. | [optional] 
**end_date** | **date** | The localized day on which the allocation ends. | [optional] 
**effort** | [**AllocationBaseEffort**](AllocationBaseEffort.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.allocation_base import AllocationBase

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationBase from a JSON string
allocation_base_instance = AllocationBase.from_json(json)
# print the JSON string representation of the object
print(AllocationBase.to_json())

# convert the object into a dict
allocation_base_dict = allocation_base_instance.to_dict()
# create an instance of AllocationBase from a dict
allocation_base_from_dict = AllocationBase.from_dict(allocation_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


