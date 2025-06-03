# TeamAddUserRequest

A user identification object for specification with the addUser/removeUser endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 

## Example

```python
from asana_asyncio.models.team_add_user_request import TeamAddUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamAddUserRequest from a JSON string
team_add_user_request_instance = TeamAddUserRequest.from_json(json)
# print the JSON string representation of the object
print(TeamAddUserRequest.to_json())

# convert the object into a dict
team_add_user_request_dict = team_add_user_request_instance.to_dict()
# create an instance of TeamAddUserRequest from a dict
team_add_user_request_from_dict = TeamAddUserRequest.from_dict(team_add_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


