# StoryResponseAllOfTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the task. | [optional] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The resource_subtype &#x60;milestone&#x60; represent a single moment in time. This means tasks with this subtype cannot have a start_date. | [optional] 
**created_by** | [**TaskCompactAllOfCreatedBy**](TaskCompactAllOfCreatedBy.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.story_response_all_of_target import StoryResponseAllOfTarget

# TODO update the JSON string below
json = "{}"
# create an instance of StoryResponseAllOfTarget from a JSON string
story_response_all_of_target_instance = StoryResponseAllOfTarget.from_json(json)
# print the JSON string representation of the object
print StoryResponseAllOfTarget.to_json()

# convert the object into a dict
story_response_all_of_target_dict = story_response_all_of_target_instance.to_dict()
# create an instance of StoryResponseAllOfTarget from a dict
story_response_all_of_target_form_dict = story_response_all_of_target.from_dict(story_response_all_of_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


