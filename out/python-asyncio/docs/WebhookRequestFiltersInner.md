# WebhookRequestFiltersInner

A set of filters to specify a whitelist for what types of events will be delivered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | The type of the resource which created the event when modified; for example, to filter to changes on regular tasks this field should be set to &#x60;task&#x60;. | [optional] 
**resource_subtype** | **str** | The resource subtype of the resource that the filter applies to. This should be set to the same value as is returned on the &#x60;resource_subtype&#x60; field on the resources themselves. | [optional] 
**action** | **str** | The type of change on the **resource** to pass through the filter. For more information refer to &#x60;Event.action&#x60; in the [event](/reference/events) schema. This can be one of &#x60;changed&#x60;, &#x60;added&#x60;, &#x60;removed&#x60;, &#x60;deleted&#x60;, and &#x60;undeleted&#x60; depending on the nature of what has occurred on the resource. | [optional] 
**fields** | **List[str]** | *Conditional.* A whitelist of fields for events which will pass the filter when the resource is changed. These can be any combination of the fields on the resources themselves. This field is only valid for &#x60;action&#x60; of type &#x60;changed&#x60; *Note: Subscriptions created on higher-level resources such as a Workspace, Team, or Portfolio do not support fields.* | [optional] 

## Example

```python
from asana_asyncio.models.webhook_request_filters_inner import WebhookRequestFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRequestFiltersInner from a JSON string
webhook_request_filters_inner_instance = WebhookRequestFiltersInner.from_json(json)
# print the JSON string representation of the object
print(WebhookRequestFiltersInner.to_json())

# convert the object into a dict
webhook_request_filters_inner_dict = webhook_request_filters_inner_instance.to_dict()
# create an instance of WebhookRequestFiltersInner from a dict
webhook_request_filters_inner_from_dict = WebhookRequestFiltersInner.from_dict(webhook_request_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


