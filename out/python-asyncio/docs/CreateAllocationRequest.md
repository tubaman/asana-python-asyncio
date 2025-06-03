# CreateAllocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateAllocationRequestData**](CreateAllocationRequestData.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_allocation_request import CreateAllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAllocationRequest from a JSON string
create_allocation_request_instance = CreateAllocationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAllocationRequest.to_json())

# convert the object into a dict
create_allocation_request_dict = create_allocation_request_instance.to_dict()
# create an instance of CreateAllocationRequest from a dict
create_allocation_request_from_dict = CreateAllocationRequest.from_dict(create_allocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


