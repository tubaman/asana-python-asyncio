# AuditLogEventActor

The entity that triggered the event. Will typically be a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_type** | **str** | The type of actor. Can be one of &#x60;user&#x60;, &#x60;asana&#x60;, &#x60;asana_support&#x60;, &#x60;anonymous&#x60;, or &#x60;external_administrator&#x60;. | [optional] 
**gid** | **str** | Globally unique identifier of the actor, if it is a user. | [optional] 
**name** | **str** | The name of the actor, if it is a user. | [optional] 
**email** | **str** | The email of the actor, if it is a user. | [optional] 

## Example

```python
from asana_asyncio.models.audit_log_event_actor import AuditLogEventActor

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEventActor from a JSON string
audit_log_event_actor_instance = AuditLogEventActor.from_json(json)
# print the JSON string representation of the object
print AuditLogEventActor.to_json()

# convert the object into a dict
audit_log_event_actor_dict = audit_log_event_actor_instance.to_dict()
# create an instance of AuditLogEventActor from a dict
audit_log_event_actor_form_dict = audit_log_event_actor.from_dict(audit_log_event_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


