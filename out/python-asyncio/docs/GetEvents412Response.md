# GetEvents412Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[GetEvents412ResponseErrorsInner]**](GetEvents412ResponseErrorsInner.md) |  | [optional] 
**sync** | **str** | A sync token to be used with the next call to the /events endpoint. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.get_events412_response import GetEvents412Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEvents412Response from a JSON string
get_events412_response_instance = GetEvents412Response.from_json(json)
# print the JSON string representation of the object
print GetEvents412Response.to_json()

# convert the object into a dict
get_events412_response_dict = get_events412_response_instance.to_dict()
# create an instance of GetEvents412Response from a dict
get_events412_response_form_dict = get_events412_response.from_dict(get_events412_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


