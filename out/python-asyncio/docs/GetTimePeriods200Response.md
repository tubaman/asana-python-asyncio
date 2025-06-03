# GetTimePeriods200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TimePeriodCompact]**](TimePeriodCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_time_periods200_response import GetTimePeriods200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimePeriods200Response from a JSON string
get_time_periods200_response_instance = GetTimePeriods200Response.from_json(json)
# print the JSON string representation of the object
print(GetTimePeriods200Response.to_json())

# convert the object into a dict
get_time_periods200_response_dict = get_time_periods200_response_instance.to_dict()
# create an instance of GetTimePeriods200Response from a dict
get_time_periods200_response_from_dict = GetTimePeriods200Response.from_dict(get_time_periods200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


