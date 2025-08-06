# GetAttachment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentResponse**](AttachmentResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_attachment200_response import GetAttachment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAttachment200Response from a JSON string
get_attachment200_response_instance = GetAttachment200Response.from_json(json)
# print the JSON string representation of the object
print(GetAttachment200Response.to_json())

# convert the object into a dict
get_attachment200_response_dict = get_attachment200_response_instance.to_dict()
# create an instance of GetAttachment200Response from a dict
get_attachment200_response_from_dict = GetAttachment200Response.from_dict(get_attachment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


