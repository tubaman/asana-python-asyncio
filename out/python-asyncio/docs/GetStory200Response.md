# GetStory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StoryResponse**](StoryResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_story200_response import GetStory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStory200Response from a JSON string
get_story200_response_instance = GetStory200Response.from_json(json)
# print the JSON string representation of the object
print GetStory200Response.to_json()

# convert the object into a dict
get_story200_response_dict = get_story200_response_instance.to_dict()
# create an instance of GetStory200Response from a dict
get_story200_response_form_dict = get_story200_response.from_dict(get_story200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


