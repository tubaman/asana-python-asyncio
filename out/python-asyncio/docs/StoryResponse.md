# StoryResponse


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
**created_by** | [**UserCompact**](UserCompact.md) |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**is_editable** | **bool** | *Conditional*. Whether the text of the story can be edited after creation. | [optional] [readonly] 
**is_edited** | **bool** | *Conditional*. Whether the text of the story has been edited after creation. | [optional] [readonly] 
**hearted** | **bool** | *Deprecated - please use likes instead* *Conditional*. True if the story is hearted by the authorized user, false if not. | [optional] [readonly] 
**hearts** | [**List[Like]**](Like.md) | *Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story. | [optional] [readonly] 
**num_hearts** | **int** | *Deprecated - please use likes instead*  *Conditional*. The number of users who have hearted this story. | [optional] [readonly] 
**liked** | **bool** | *Conditional*. True if the story is liked by the authorized user, false if not. | [optional] [readonly] 
**likes** | [**List[Like]**](Like.md) | *Conditional*. Array of likes for users who have liked this story. | [optional] [readonly] 
**num_likes** | **int** | *Conditional*. The number of users who have liked this story. | [optional] [readonly] 
**previews** | [**List[Preview]**](Preview.md) | *Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.* | [optional] [readonly] 
**old_name** | **str** | *Conditional*&#39; | [optional] 
**new_name** | **str** | *Conditional* | [optional] [readonly] 
**old_dates** | [**StoryResponseDates**](StoryResponseDates.md) |  | [optional] 
**new_dates** | [**StoryResponseDates**](StoryResponseDates.md) |  | [optional] 
**old_resource_subtype** | **str** | *Conditional* | [optional] [readonly] 
**new_resource_subtype** | **str** | *Conditional* | [optional] [readonly] 
**story** | [**StoryCompact**](StoryCompact.md) |  | [optional] 
**assignee** | [**UserCompact**](UserCompact.md) |  | [optional] 
**follower** | [**UserCompact**](UserCompact.md) |  | [optional] 
**old_section** | [**SectionCompact**](SectionCompact.md) |  | [optional] 
**new_section** | [**SectionCompact**](SectionCompact.md) |  | [optional] 
**task** | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**project** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**tag** | [**TagCompact**](TagCompact.md) |  | [optional] 
**custom_field** | [**CustomFieldCompact**](CustomFieldCompact.md) |  | [optional] 
**old_text_value** | **str** | *Conditional* | [optional] [readonly] 
**new_text_value** | **str** | *Conditional* | [optional] [readonly] 
**old_number_value** | **int** | *Conditional* | [optional] [readonly] 
**new_number_value** | **int** | *Conditional* | [optional] [readonly] 
**old_enum_value** | [**EnumOption**](EnumOption.md) |  | [optional] 
**new_enum_value** | [**EnumOption**](EnumOption.md) |  | [optional] 
**old_date_value** | [**StoryResponseAllOfOldDateValue**](StoryResponseAllOfOldDateValue.md) |  | [optional] 
**new_date_value** | [**StoryResponseAllOfNewDateValue**](StoryResponseAllOfNewDateValue.md) |  | [optional] 
**old_people_value** | [**List[UserCompact]**](UserCompact.md) | *Conditional*. The old value of a people custom field story. | [optional] [readonly] 
**new_people_value** | [**List[UserCompact]**](UserCompact.md) | *Conditional*. The new value of a people custom field story. | [optional] [readonly] 
**old_multi_enum_values** | [**List[EnumOption]**](EnumOption.md) | *Conditional*. The old value of a multi-enum custom field story. | [optional] [readonly] 
**new_multi_enum_values** | [**List[EnumOption]**](EnumOption.md) | *Conditional*. The new value of a multi-enum custom field story. | [optional] [readonly] 
**new_approval_status** | **str** | *Conditional*. The new value of approval status. | [optional] [readonly] 
**old_approval_status** | **str** | *Conditional*. The old value of approval status. | [optional] [readonly] 
**duplicate_of** | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**duplicated_from** | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**dependency** | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**source** | **str** | The component of the Asana product the user used to trigger the story. | [optional] [readonly] 
**target** | [**StoryResponseAllOfTarget**](StoryResponseAllOfTarget.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.story_response import StoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StoryResponse from a JSON string
story_response_instance = StoryResponse.from_json(json)
# print the JSON string representation of the object
print StoryResponse.to_json()

# convert the object into a dict
story_response_dict = story_response_instance.to_dict()
# create an instance of StoryResponse from a dict
story_response_form_dict = story_response.from_dict(story_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


