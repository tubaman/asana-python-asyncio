# RuleTriggerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message providing more detail about the result | [optional] 

## Example

```python
from asana_asyncio.models.rule_trigger_response import RuleTriggerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuleTriggerResponse from a JSON string
rule_trigger_response_instance = RuleTriggerResponse.from_json(json)
# print the JSON string representation of the object
print(RuleTriggerResponse.to_json())

# convert the object into a dict
rule_trigger_response_dict = rule_trigger_response_instance.to_dict()
# create an instance of RuleTriggerResponse from a dict
rule_trigger_response_from_dict = RuleTriggerResponse.from_dict(rule_trigger_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


