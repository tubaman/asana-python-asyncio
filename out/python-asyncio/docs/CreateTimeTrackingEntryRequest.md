# CreateTimeTrackingEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateTimeTrackingEntryRequest**](CreateTimeTrackingEntryRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_time_tracking_entry_request import CreateTimeTrackingEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimeTrackingEntryRequest from a JSON string
create_time_tracking_entry_request_instance = CreateTimeTrackingEntryRequest.from_json(json)
# print the JSON string representation of the object
print CreateTimeTrackingEntryRequest.to_json()

# convert the object into a dict
create_time_tracking_entry_request_dict = create_time_tracking_entry_request_instance.to_dict()
# create an instance of CreateTimeTrackingEntryRequest from a dict
create_time_tracking_entry_request_form_dict = create_time_tracking_entry_request.from_dict(create_time_tracking_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


