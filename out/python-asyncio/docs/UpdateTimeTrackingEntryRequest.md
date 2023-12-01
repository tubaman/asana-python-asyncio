# UpdateTimeTrackingEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateTimeTrackingEntryRequest**](UpdateTimeTrackingEntryRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_time_tracking_entry_request import UpdateTimeTrackingEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTimeTrackingEntryRequest from a JSON string
update_time_tracking_entry_request_instance = UpdateTimeTrackingEntryRequest.from_json(json)
# print the JSON string representation of the object
print UpdateTimeTrackingEntryRequest.to_json()

# convert the object into a dict
update_time_tracking_entry_request_dict = update_time_tracking_entry_request_instance.to_dict()
# create an instance of UpdateTimeTrackingEntryRequest from a dict
update_time_tracking_entry_request_form_dict = update_time_tracking_entry_request.from_dict(update_time_tracking_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


