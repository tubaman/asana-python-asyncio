# AllocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**start_date** | **date** | The localized day on which the allocation starts. | [optional] 
**end_date** | **date** | The localized day on which the allocation ends. | [optional] 
**effort** | [**AllocationBaseEffort**](AllocationBaseEffort.md) |  | [optional] 
**assignee** | **str** | Globally unique identifier for the user or placeholder assigned to the allocation. | [optional] 
**parent** | **str** | Globally unique identifier for the project the allocation is on. | [optional] 

## Example

```python
from asana_asyncio.models.allocation_request import AllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationRequest from a JSON string
allocation_request_instance = AllocationRequest.from_json(json)
# print the JSON string representation of the object
print(AllocationRequest.to_json())

# convert the object into a dict
allocation_request_dict = allocation_request_instance.to_dict()
# create an instance of AllocationRequest from a dict
allocation_request_from_dict = AllocationRequest.from_dict(allocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


