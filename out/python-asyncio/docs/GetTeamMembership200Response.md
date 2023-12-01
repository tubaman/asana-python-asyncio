# GetTeamMembership200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TeamMembershipCompact**](TeamMembershipCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_team_membership200_response import GetTeamMembership200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTeamMembership200Response from a JSON string
get_team_membership200_response_instance = GetTeamMembership200Response.from_json(json)
# print the JSON string representation of the object
print GetTeamMembership200Response.to_json()

# convert the object into a dict
get_team_membership200_response_dict = get_team_membership200_response_instance.to_dict()
# create an instance of GetTeamMembership200Response from a dict
get_team_membership200_response_form_dict = get_team_membership200_response.from_dict(get_team_membership200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


