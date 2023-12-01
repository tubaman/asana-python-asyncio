# TimeTrackingEntryCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**duration_minutes** | **int** | Time in minutes tracked by the entry. | [optional] 
**entered_on** | **date** | The day that this entry is logged on. | [optional] 
**created_by** | [**UserCompact**](UserCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.time_tracking_entry_compact import TimeTrackingEntryCompact

# TODO update the JSON string below
json = "{}"
# create an instance of TimeTrackingEntryCompact from a JSON string
time_tracking_entry_compact_instance = TimeTrackingEntryCompact.from_json(json)
# print the JSON string representation of the object
print TimeTrackingEntryCompact.to_json()

# convert the object into a dict
time_tracking_entry_compact_dict = time_tracking_entry_compact_instance.to_dict()
# create an instance of TimeTrackingEntryCompact from a dict
time_tracking_entry_compact_form_dict = time_tracking_entry_compact.from_dict(time_tracking_entry_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


