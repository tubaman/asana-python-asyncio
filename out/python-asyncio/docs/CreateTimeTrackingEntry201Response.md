# CreateTimeTrackingEntry201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TimeTrackingEntryBase**](TimeTrackingEntryBase.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_time_tracking_entry201_response import CreateTimeTrackingEntry201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimeTrackingEntry201Response from a JSON string
create_time_tracking_entry201_response_instance = CreateTimeTrackingEntry201Response.from_json(json)
# print the JSON string representation of the object
print CreateTimeTrackingEntry201Response.to_json()

# convert the object into a dict
create_time_tracking_entry201_response_dict = create_time_tracking_entry201_response_instance.to_dict()
# create an instance of CreateTimeTrackingEntry201Response from a dict
create_time_tracking_entry201_response_form_dict = create_time_tracking_entry201_response.from_dict(create_time_tracking_entry201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


