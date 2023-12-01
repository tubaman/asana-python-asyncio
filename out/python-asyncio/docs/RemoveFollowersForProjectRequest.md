# RemoveFollowersForProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RemoveFollowersRequest**](RemoveFollowersRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_followers_for_project_request import RemoveFollowersForProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFollowersForProjectRequest from a JSON string
remove_followers_for_project_request_instance = RemoveFollowersForProjectRequest.from_json(json)
# print the JSON string representation of the object
print RemoveFollowersForProjectRequest.to_json()

# convert the object into a dict
remove_followers_for_project_request_dict = remove_followers_for_project_request_instance.to_dict()
# create an instance of RemoveFollowersForProjectRequest from a dict
remove_followers_for_project_request_form_dict = remove_followers_for_project_request.from_dict(remove_followers_for_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


