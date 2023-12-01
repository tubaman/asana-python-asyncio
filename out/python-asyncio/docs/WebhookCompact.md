# WebhookCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**active** | **bool** | If true, the webhook will send events - if false it is considered inactive and will not generate events. | [optional] [readonly] 
**resource** | [**AsanaNamedResource**](AsanaNamedResource.md) |  | [optional] 
**target** | **str** | The URL to receive the HTTP POST. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.webhook_compact import WebhookCompact

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCompact from a JSON string
webhook_compact_instance = WebhookCompact.from_json(json)
# print the JSON string representation of the object
print WebhookCompact.to_json()

# convert the object into a dict
webhook_compact_dict = webhook_compact_instance.to_dict()
# create an instance of WebhookCompact from a dict
webhook_compact_form_dict = webhook_compact.from_dict(webhook_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


