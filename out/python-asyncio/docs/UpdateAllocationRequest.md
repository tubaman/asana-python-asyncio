# UpdateAllocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AllocationRequest**](AllocationRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_allocation_request import UpdateAllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAllocationRequest from a JSON string
update_allocation_request_instance = UpdateAllocationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAllocationRequest.to_json())

# convert the object into a dict
update_allocation_request_dict = update_allocation_request_instance.to_dict()
# create an instance of UpdateAllocationRequest from a dict
update_allocation_request_from_dict = UpdateAllocationRequest.from_dict(update_allocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


