# AddUserForTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TeamAddUserRequest**](TeamAddUserRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_user_for_team_request import AddUserForTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserForTeamRequest from a JSON string
add_user_for_team_request_instance = AddUserForTeamRequest.from_json(json)
# print the JSON string representation of the object
print AddUserForTeamRequest.to_json()

# convert the object into a dict
add_user_for_team_request_dict = add_user_for_team_request_instance.to_dict()
# create an instance of AddUserForTeamRequest from a dict
add_user_for_team_request_form_dict = add_user_for_team_request.from_dict(add_user_for_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


