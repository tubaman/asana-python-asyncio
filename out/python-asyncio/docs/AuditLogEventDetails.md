# AuditLogEventDetails

Event specific details. The schema will vary depending on the `event_type`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_value** | **str** | The previous value of the field that was modified in the audited event. | [optional] 
**new_value** | **str** | The new value after the modification in the audited event. | [optional] 
**group** | **Dict[str, object]** | The division or organizational unit where the event occurred. Primarily used to scope role change events (e.g., &#x60;user_division_admin_role_changed&#x60;), but may appear in other contexts involving group-level changes. | [optional] 

## Example

```python
from asana_asyncio.models.audit_log_event_details import AuditLogEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEventDetails from a JSON string
audit_log_event_details_instance = AuditLogEventDetails.from_json(json)
# print the JSON string representation of the object
print(AuditLogEventDetails.to_json())

# convert the object into a dict
audit_log_event_details_dict = audit_log_event_details_instance.to_dict()
# create an instance of AuditLogEventDetails from a dict
audit_log_event_details_from_dict = AuditLogEventDetails.from_dict(audit_log_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


