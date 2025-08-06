# GetCustomType200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomTypeResponse**](CustomTypeResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_custom_type200_response import GetCustomType200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomType200Response from a JSON string
get_custom_type200_response_instance = GetCustomType200Response.from_json(json)
# print the JSON string representation of the object
print(GetCustomType200Response.to_json())

# convert the object into a dict
get_custom_type200_response_dict = get_custom_type200_response_instance.to_dict()
# create an instance of GetCustomType200Response from a dict
get_custom_type200_response_from_dict = GetCustomType200Response.from_dict(get_custom_type200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


