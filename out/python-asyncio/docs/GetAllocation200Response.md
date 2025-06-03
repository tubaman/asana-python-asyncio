# GetAllocation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AllocationResponse**](AllocationResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_allocation200_response import GetAllocation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllocation200Response from a JSON string
get_allocation200_response_instance = GetAllocation200Response.from_json(json)
# print the JSON string representation of the object
print(GetAllocation200Response.to_json())

# convert the object into a dict
get_allocation200_response_dict = get_allocation200_response_instance.to_dict()
# create an instance of GetAllocation200Response from a dict
get_allocation200_response_from_dict = GetAllocation200Response.from_dict(get_allocation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


