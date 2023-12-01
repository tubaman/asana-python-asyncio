# TeamRemoveUserRequest

A user identification object for specification with the addUser/removeUser endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 

## Example

```python
from asana_asyncio.models.team_remove_user_request import TeamRemoveUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRemoveUserRequest from a JSON string
team_remove_user_request_instance = TeamRemoveUserRequest.from_json(json)
# print the JSON string representation of the object
print TeamRemoveUserRequest.to_json()

# convert the object into a dict
team_remove_user_request_dict = team_remove_user_request_instance.to_dict()
# create an instance of TeamRemoveUserRequest from a dict
team_remove_user_request_form_dict = team_remove_user_request.from_dict(team_remove_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


