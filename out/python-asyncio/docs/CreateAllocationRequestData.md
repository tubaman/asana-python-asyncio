# CreateAllocationRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**start_date** | **date** | The localized day on which the allocation starts. | 
**end_date** | **date** | The localized day on which the allocation ends. | 
**effort** | [**AllocationBaseEffort**](AllocationBaseEffort.md) |  | [optional] 
**assignee** | **str** | Globally unique identifier for the user or placeholder assigned to the allocation. | 
**parent** | **str** | Globally unique identifier for the project the allocation is on. | 

## Example

```python
from asana_asyncio.models.create_allocation_request_data import CreateAllocationRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAllocationRequestData from a JSON string
create_allocation_request_data_instance = CreateAllocationRequestData.from_json(json)
# print the JSON string representation of the object
print(CreateAllocationRequestData.to_json())

# convert the object into a dict
create_allocation_request_data_dict = create_allocation_request_data_instance.to_dict()
# create an instance of CreateAllocationRequestData from a dict
create_allocation_request_data_from_dict = CreateAllocationRequestData.from_dict(create_allocation_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


