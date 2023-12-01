# AuditLogEventContext

The context from which this event originated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | The type of context. Can be one of &#x60;web&#x60;, &#x60;desktop&#x60;, &#x60;mobile&#x60;, &#x60;asana_support&#x60;, &#x60;asana&#x60;, &#x60;email&#x60;, or &#x60;api&#x60;. | [optional] 
**api_authentication_method** | **str** | The authentication method used in the context of an API request. Only present if the &#x60;context_type&#x60; is &#x60;api&#x60;. Can be one of &#x60;cookie&#x60;, &#x60;oauth&#x60;, &#x60;personal_access_token&#x60;, or &#x60;service_account&#x60;. | [optional] 
**client_ip_address** | **str** | The IP address of the client that initiated the event, if applicable. | [optional] 
**user_agent** | **str** | The user agent of the client that initiated the event, if applicable. | [optional] 
**oauth_app_name** | **str** | The name of the OAuth App that initiated the event. Only present if the &#x60;api_authentication_method&#x60; is &#x60;oauth&#x60;. | [optional] 

## Example

```python
from asana_asyncio.models.audit_log_event_context import AuditLogEventContext

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEventContext from a JSON string
audit_log_event_context_instance = AuditLogEventContext.from_json(json)
# print the JSON string representation of the object
print AuditLogEventContext.to_json()

# convert the object into a dict
audit_log_event_context_dict = audit_log_event_context_instance.to_dict()
# create an instance of AuditLogEventContext from a dict
audit_log_event_context_form_dict = audit_log_event_context.from_dict(audit_log_event_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


