# GetEvents200Response

The full record for all events that have occurred since the sync token was created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventResponse]**](EventResponse.md) |  | [optional] 
**sync** | **str** | A sync token to be used with the next call to the /events endpoint. | [optional] 
**has_more** | **bool** | Indicates whether there are more events to pull. | [optional] 

## Example

```python
from asana_asyncio.models.get_events200_response import GetEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEvents200Response from a JSON string
get_events200_response_instance = GetEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetEvents200Response.to_json())

# convert the object into a dict
get_events200_response_dict = get_events200_response_instance.to_dict()
# create an instance of GetEvents200Response from a dict
get_events200_response_from_dict = GetEvents200Response.from_dict(get_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


