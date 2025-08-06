# AttachmentCompact

An *attachment* object represents any file attached to a task in Asana, whether it's an uploaded file or one associated via a third-party service such as Dropbox or Google Drive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the file. | [optional] [readonly] 
**resource_subtype** | **str** | The service hosting the attachment. Valid values are &#x60;asana&#x60;, &#x60;dropbox&#x60;, &#x60;gdrive&#x60;, &#x60;onedrive&#x60;, &#x60;box&#x60;, &#x60;vimeo&#x60;, and &#x60;external&#x60;. | [optional] 

## Example

```python
from asana_asyncio.models.attachment_compact import AttachmentCompact

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentCompact from a JSON string
attachment_compact_instance = AttachmentCompact.from_json(json)
# print the JSON string representation of the object
print(AttachmentCompact.to_json())

# convert the object into a dict
attachment_compact_dict = attachment_compact_instance.to_dict()
# create an instance of AttachmentCompact from a dict
attachment_compact_from_dict = AttachmentCompact.from_dict(attachment_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


