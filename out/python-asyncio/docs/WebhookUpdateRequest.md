# WebhookUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[WebhookResponseAllOfFilters]**](WebhookResponseAllOfFilters.md) | An array of WebhookFilter objects to specify a whitelist of filters to apply to events from this webhook. If a webhook event passes any of the filters the event will be delivered; otherwise no event will be sent to the receiving server. | [optional] 

## Example

```python
from asana_asyncio.models.webhook_update_request import WebhookUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookUpdateRequest from a JSON string
webhook_update_request_instance = WebhookUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WebhookUpdateRequest.to_json())

# convert the object into a dict
webhook_update_request_dict = webhook_update_request_instance.to_dict()
# create an instance of WebhookUpdateRequest from a dict
webhook_update_request_from_dict = WebhookUpdateRequest.from_dict(webhook_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


