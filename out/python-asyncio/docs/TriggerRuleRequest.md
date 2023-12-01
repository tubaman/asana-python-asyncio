# TriggerRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RuleTriggerRequest**](RuleTriggerRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.trigger_rule_request import TriggerRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerRuleRequest from a JSON string
trigger_rule_request_instance = TriggerRuleRequest.from_json(json)
# print the JSON string representation of the object
print TriggerRuleRequest.to_json()

# convert the object into a dict
trigger_rule_request_dict = trigger_rule_request_instance.to_dict()
# create an instance of TriggerRuleRequest from a dict
trigger_rule_request_form_dict = trigger_rule_request.from_dict(trigger_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


