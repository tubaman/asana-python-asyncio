# GetTimeTrackingEntriesForTask200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TimeTrackingEntryCompact]**](TimeTrackingEntryCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_time_tracking_entries_for_task200_response import GetTimeTrackingEntriesForTask200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimeTrackingEntriesForTask200Response from a JSON string
get_time_tracking_entries_for_task200_response_instance = GetTimeTrackingEntriesForTask200Response.from_json(json)
# print the JSON string representation of the object
print GetTimeTrackingEntriesForTask200Response.to_json()

# convert the object into a dict
get_time_tracking_entries_for_task200_response_dict = get_time_tracking_entries_for_task200_response_instance.to_dict()
# create an instance of GetTimeTrackingEntriesForTask200Response from a dict
get_time_tracking_entries_for_task200_response_form_dict = get_time_tracking_entries_for_task200_response.from_dict(get_time_tracking_entries_for_task200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


