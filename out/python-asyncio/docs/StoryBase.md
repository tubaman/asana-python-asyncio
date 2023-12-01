# StoryBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**text** | **str** | The plain text of the comment to add. Cannot be used with html_text. | [optional] 
**html_text** | **str** | [Opt In](/docs/inputoutput-options). HTML formatted text for a comment. This will not include the name of the creator. | [optional] 
**is_pinned** | **bool** | *Conditional*. Whether the story should be pinned on the resource. | [optional] 
**sticker_name** | **str** | The name of the sticker in this story. &#x60;null&#x60; if there is no sticker. | [optional] 

## Example

```python
from asana_asyncio.models.story_base import StoryBase

# TODO update the JSON string below
json = "{}"
# create an instance of StoryBase from a JSON string
story_base_instance = StoryBase.from_json(json)
# print the JSON string representation of the object
print StoryBase.to_json()

# convert the object into a dict
story_base_dict = story_base_instance.to_dict()
# create an instance of StoryBase from a dict
story_base_form_dict = story_base.from_dict(story_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


