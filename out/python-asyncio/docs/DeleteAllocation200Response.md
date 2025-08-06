# DeleteAllocation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | An empty object. Some endpoints do not return an object on success. The success is conveyed through a 2-- status code and returning an empty object. | [optional] 

## Example

```python
from asana_asyncio.models.delete_allocation200_response import DeleteAllocation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAllocation200Response from a JSON string
delete_allocation200_response_instance = DeleteAllocation200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteAllocation200Response.to_json())

# convert the object into a dict
delete_allocation200_response_dict = delete_allocation200_response_instance.to_dict()
# create an instance of DeleteAllocation200Response from a dict
delete_allocation200_response_from_dict = DeleteAllocation200Response.from_dict(delete_allocation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


