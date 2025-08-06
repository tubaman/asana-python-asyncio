# AllocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**start_date** | **date** | The localized day on which the allocation starts. | [optional] 
**end_date** | **date** | The localized day on which the allocation ends. | [optional] 
**effort** | [**AllocationBaseEffort**](AllocationBaseEffort.md) |  | [optional] 
**assignee** | [**AllocationResponseAllOfAssignee**](AllocationResponseAllOfAssignee.md) |  | [optional] 
**created_by** | **object** |  | [optional] 
**parent** | **object** |  | [optional] 
**resource_subtype** | **str** | The subtype of the allocation. | [optional] 

## Example

```python
from asana_asyncio.models.allocation_response import AllocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationResponse from a JSON string
allocation_response_instance = AllocationResponse.from_json(json)
# print the JSON string representation of the object
print(AllocationResponse.to_json())

# convert the object into a dict
allocation_response_dict = allocation_response_instance.to_dict()
# create an instance of AllocationResponse from a dict
allocation_response_from_dict = AllocationResponse.from_dict(allocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


