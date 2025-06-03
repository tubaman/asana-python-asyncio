# StoryResponseDates

*Conditional*

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_on** | **date** | The day on which work for this goal begins, or null if the goal has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format, and cannot be set unless there is an accompanying due date. | [optional] 
**due_at** | **datetime** | The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with &#x60;due_on&#x60;. | [optional] 
**due_on** | **date** | The localized day on which this goal is due. This takes a date with format &#x60;YYYY-MM-DD&#x60;. | [optional] 

## Example

```python
from asana_asyncio.models.story_response_dates import StoryResponseDates

# TODO update the JSON string below
json = "{}"
# create an instance of StoryResponseDates from a JSON string
story_response_dates_instance = StoryResponseDates.from_json(json)
# print the JSON string representation of the object
print(StoryResponseDates.to_json())

# convert the object into a dict
story_response_dates_dict = story_response_dates_instance.to_dict()
# create an instance of StoryResponseDates from a dict
story_response_dates_from_dict = StoryResponseDates.from_dict(story_response_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


