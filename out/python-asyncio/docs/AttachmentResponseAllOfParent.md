# AttachmentResponseAllOfParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the task. | [optional] 
**resource_subtype** | **str** | The resource subtype of the parent resource that the filter applies to. | [optional] 
**created_by** | [**TaskCompactCreatedBy**](TaskCompactCreatedBy.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.attachment_response_all_of_parent import AttachmentResponseAllOfParent

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentResponseAllOfParent from a JSON string
attachment_response_all_of_parent_instance = AttachmentResponseAllOfParent.from_json(json)
# print the JSON string representation of the object
print(AttachmentResponseAllOfParent.to_json())

# convert the object into a dict
attachment_response_all_of_parent_dict = attachment_response_all_of_parent_instance.to_dict()
# create an instance of AttachmentResponseAllOfParent from a dict
attachment_response_all_of_parent_from_dict = AttachmentResponseAllOfParent.from_dict(attachment_response_all_of_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


