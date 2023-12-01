# GetStatusesForObject200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StatusUpdateCompact]**](StatusUpdateCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_statuses_for_object200_response import GetStatusesForObject200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusesForObject200Response from a JSON string
get_statuses_for_object200_response_instance = GetStatusesForObject200Response.from_json(json)
# print the JSON string representation of the object
print GetStatusesForObject200Response.to_json()

# convert the object into a dict
get_statuses_for_object200_response_dict = get_statuses_for_object200_response_instance.to_dict()
# create an instance of GetStatusesForObject200Response from a dict
get_statuses_for_object200_response_form_dict = get_statuses_for_object200_response.from_dict(get_statuses_for_object200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


