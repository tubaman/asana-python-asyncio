# AddFollowersForProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AddFollowersRequest**](AddFollowersRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_followers_for_project_request import AddFollowersForProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddFollowersForProjectRequest from a JSON string
add_followers_for_project_request_instance = AddFollowersForProjectRequest.from_json(json)
# print the JSON string representation of the object
print(AddFollowersForProjectRequest.to_json())

# convert the object into a dict
add_followers_for_project_request_dict = add_followers_for_project_request_instance.to_dict()
# create an instance of AddFollowersForProjectRequest from a dict
add_followers_for_project_request_from_dict = AddFollowersForProjectRequest.from_dict(add_followers_for_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


