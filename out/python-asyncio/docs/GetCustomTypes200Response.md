# GetCustomTypes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomTypeResponse]**](CustomTypeResponse.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_custom_types200_response import GetCustomTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomTypes200Response from a JSON string
get_custom_types200_response_instance = GetCustomTypes200Response.from_json(json)
# print the JSON string representation of the object
print(GetCustomTypes200Response.to_json())

# convert the object into a dict
get_custom_types200_response_dict = get_custom_types200_response_instance.to_dict()
# create an instance of GetCustomTypes200Response from a dict
get_custom_types200_response_from_dict = GetCustomTypes200Response.from_dict(get_custom_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


