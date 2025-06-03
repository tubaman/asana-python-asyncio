# WebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**active** | **bool** | If true, the webhook will send events - if false it is considered inactive and will not generate events. | [optional] [readonly] 
**resource** | [**AsanaNamedResource**](AsanaNamedResource.md) |  | [optional] 
**target** | **str** | The URL to receive the HTTP POST. | [optional] [readonly] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**last_failure_at** | **datetime** | The timestamp when the webhook last received an error when sending an event to the target. | [optional] [readonly] 
**last_failure_content** | **str** | The contents of the last error response sent to the webhook when attempting to deliver events to the target. | [optional] [readonly] 
**last_success_at** | **datetime** | The timestamp when the webhook last successfully sent an event to the target. | [optional] [readonly] 
**delivery_retry_count** | **int** | The number of times the webhook has retried delivery of events to the target (resets after a successful attempt). | [optional] [readonly] 
**next_attempt_after** | **datetime** | The timestamp after which the webhook will next attempt to deliver an event to the target. | [optional] [readonly] 
**failure_deletion_timestamp** | **datetime** | The timestamp when the webhook will be deleted if there is no successful attempt to deliver events to the target | [optional] [readonly] 
**filters** | [**List[WebhookResponseAllOfFilters]**](WebhookResponseAllOfFilters.md) | Whitelist of filters to apply to events from this webhook. If a webhook event passes any of the filters the event will be delivered; otherwise no event will be sent to the receiving server. | [optional] 

## Example

```python
from asana_asyncio.models.webhook_response import WebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResponse from a JSON string
webhook_response_instance = WebhookResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookResponse.to_json())

# convert the object into a dict
webhook_response_dict = webhook_response_instance.to_dict()
# create an instance of WebhookResponse from a dict
webhook_response_from_dict = WebhookResponse.from_dict(webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


