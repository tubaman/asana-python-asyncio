# AuditLogEventResource

The primary object that was affected by this event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | The type of resource. | [optional] 
**resource_subtype** | **str** | The subtype of resource. Most resources will not have a subtype. | [optional] 
**gid** | **str** | Globally unique identifier of the resource. | [optional] 
**name** | **str** | The name of the resource. | [optional] 
**email** | **str** | The email of the resource, if applicable. | [optional] 

## Example

```python
from asana_asyncio.models.audit_log_event_resource import AuditLogEventResource

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEventResource from a JSON string
audit_log_event_resource_instance = AuditLogEventResource.from_json(json)
# print the JSON string representation of the object
print(AuditLogEventResource.to_json())

# convert the object into a dict
audit_log_event_resource_dict = audit_log_event_resource_instance.to_dict()
# create an instance of AuditLogEventResource from a dict
audit_log_event_resource_from_dict = AuditLogEventResource.from_dict(audit_log_event_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


