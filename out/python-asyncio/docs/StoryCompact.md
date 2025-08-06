# StoryCompact

A story represents an activity associated with an object in the Asana system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**created_by** | [**UserCompact**](UserCompact.md) |  | [optional] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**text** | **str** | *Create-only*. Human-readable text for the story or comment. This will not include the name of the creator. *Note: This is not guaranteed to be stable for a given type of story. For example, text for a reassignment may not always say “assigned to …” as the text for a story can both be edited and change based on the language settings of the user making the request.* Use the &#x60;resource_subtype&#x60; property to discover the action that created the story. | [optional] 

## Example

```python
from asana_asyncio.models.story_compact import StoryCompact

# TODO update the JSON string below
json = "{}"
# create an instance of StoryCompact from a JSON string
story_compact_instance = StoryCompact.from_json(json)
# print the JSON string representation of the object
print(StoryCompact.to_json())

# convert the object into a dict
story_compact_dict = story_compact_instance.to_dict()
# create an instance of StoryCompact from a dict
story_compact_from_dict = StoryCompact.from_dict(story_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


