# TagBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the tag. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 
**color** | **str** | Color of the tag. | [optional] 
**notes** | **str** | Free-form textual information associated with the tag (i.e. its description). | [optional] 

## Example

```python
from asana_asyncio.models.tag_base import TagBase

# TODO update the JSON string below
json = "{}"
# create an instance of TagBase from a JSON string
tag_base_instance = TagBase.from_json(json)
# print the JSON string representation of the object
print TagBase.to_json()

# convert the object into a dict
tag_base_dict = tag_base_instance.to_dict()
# create an instance of TagBase from a dict
tag_base_form_dict = tag_base.from_dict(tag_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


