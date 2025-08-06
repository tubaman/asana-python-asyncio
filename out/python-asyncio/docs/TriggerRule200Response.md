# TriggerRule200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RuleTriggerResponse**](RuleTriggerResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.trigger_rule200_response import TriggerRule200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerRule200Response from a JSON string
trigger_rule200_response_instance = TriggerRule200Response.from_json(json)
# print the JSON string representation of the object
print(TriggerRule200Response.to_json())

# convert the object into a dict
trigger_rule200_response_dict = trigger_rule200_response_instance.to_dict()
# create an instance of TriggerRule200Response from a dict
trigger_rule200_response_from_dict = TriggerRule200Response.from_dict(trigger_rule200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


