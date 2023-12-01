# TagCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the tag. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 

## Example

```python
from asana_asyncio.models.tag_compact import TagCompact

# TODO update the JSON string below
json = "{}"
# create an instance of TagCompact from a JSON string
tag_compact_instance = TagCompact.from_json(json)
# print the JSON string representation of the object
print TagCompact.to_json()

# convert the object into a dict
tag_compact_dict = tag_compact_instance.to_dict()
# create an instance of TagCompact from a dict
tag_compact_form_dict = tag_compact.from_dict(tag_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


