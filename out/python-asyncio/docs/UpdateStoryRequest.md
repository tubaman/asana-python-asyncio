# UpdateStoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StoryBase**](StoryBase.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_story_request import UpdateStoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStoryRequest from a JSON string
update_story_request_instance = UpdateStoryRequest.from_json(json)
# print the JSON string representation of the object
print UpdateStoryRequest.to_json()

# convert the object into a dict
update_story_request_dict = update_story_request_instance.to_dict()
# create an instance of UpdateStoryRequest from a dict
update_story_request_form_dict = update_story_request.from_dict(update_story_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


