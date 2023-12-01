# RemoveUserForTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TeamRemoveUserRequest**](TeamRemoveUserRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_user_for_team_request import RemoveUserForTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserForTeamRequest from a JSON string
remove_user_for_team_request_instance = RemoveUserForTeamRequest.from_json(json)
# print the JSON string representation of the object
print RemoveUserForTeamRequest.to_json()

# convert the object into a dict
remove_user_for_team_request_dict = remove_user_for_team_request_instance.to_dict()
# create an instance of RemoveUserForTeamRequest from a dict
remove_user_for_team_request_form_dict = remove_user_for_team_request.from_dict(remove_user_for_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


