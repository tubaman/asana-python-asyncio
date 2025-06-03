# CreateBatchRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BatchResponse]**](BatchResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_batch_request200_response import CreateBatchRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchRequest200Response from a JSON string
create_batch_request200_response_instance = CreateBatchRequest200Response.from_json(json)
# print the JSON string representation of the object
print(CreateBatchRequest200Response.to_json())

# convert the object into a dict
create_batch_request200_response_dict = create_batch_request200_response_instance.to_dict()
# create an instance of CreateBatchRequest200Response from a dict
create_batch_request200_response_from_dict = CreateBatchRequest200Response.from_dict(create_batch_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


