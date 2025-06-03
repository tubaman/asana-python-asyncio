# RuleTriggerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | The ID of the resource. For the duration of the beta, this resource is always a task, and this task must exist in the project in which the rule is created. | 
**action_data** | **Dict[str, object]** | The dynamic keys and values of the request. These fields are intended to be used in the action for the rule associated with this trigger. | 

## Example

```python
from asana_asyncio.models.rule_trigger_request import RuleTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RuleTriggerRequest from a JSON string
rule_trigger_request_instance = RuleTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(RuleTriggerRequest.to_json())

# convert the object into a dict
rule_trigger_request_dict = rule_trigger_request_instance.to_dict()
# create an instance of RuleTriggerRequest from a dict
rule_trigger_request_from_dict = RuleTriggerRequest.from_dict(rule_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


