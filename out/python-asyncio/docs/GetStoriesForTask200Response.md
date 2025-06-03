# GetStoriesForTask200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StoryCompact]**](StoryCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_stories_for_task200_response import GetStoriesForTask200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStoriesForTask200Response from a JSON string
get_stories_for_task200_response_instance = GetStoriesForTask200Response.from_json(json)
# print the JSON string representation of the object
print(GetStoriesForTask200Response.to_json())

# convert the object into a dict
get_stories_for_task200_response_dict = get_stories_for_task200_response_instance.to_dict()
# create an instance of GetStoriesForTask200Response from a dict
get_stories_for_task200_response_from_dict = GetStoriesForTask200Response.from_dict(get_stories_for_task200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


