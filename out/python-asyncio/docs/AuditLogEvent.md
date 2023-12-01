# AuditLogEvent

An object representing a single event within an Asana domain.  Every audit log event is comprised of an `event_type`, `actor`, `resource`, and `context`. Some events will include additional metadata about the event under `details`. See our [currently supported list of events](/docs/audit-log-events#supported-audit-log-events) for more details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the &#x60;AuditLogEvent&#x60;, as a string. | [optional] 
**created_at** | **datetime** | The time the event was created. | [optional] 
**event_type** | **str** | The type of the event. | [optional] 
**event_category** | **str** | The category that this &#x60;event_type&#x60; belongs to. | [optional] 
**actor** | [**AuditLogEventActor**](AuditLogEventActor.md) |  | [optional] 
**resource** | [**AuditLogEventResource**](AuditLogEventResource.md) |  | [optional] 
**details** | **object** | Event specific details. The schema will vary depending on the &#x60;event_type&#x60;. | [optional] 
**context** | [**AuditLogEventContext**](AuditLogEventContext.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.audit_log_event import AuditLogEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEvent from a JSON string
audit_log_event_instance = AuditLogEvent.from_json(json)
# print the JSON string representation of the object
print AuditLogEvent.to_json()

# convert the object into a dict
audit_log_event_dict = audit_log_event_instance.to_dict()
# create an instance of AuditLogEvent from a dict
audit_log_event_form_dict = audit_log_event.from_dict(audit_log_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


