# TeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the team. | [optional] 
**description** | **str** | The description of the team.  | [optional] 
**html_description** | **str** | The description of the team with formatting as HTML.  | [optional] 
**organization** | **str** | The organization/workspace the team belongs to. This must be the same organization you are in and cannot be changed once set.  | [optional] 
**visibility** | **str** | The visibility of the team to users in the same organization  | [optional] 
**edit_team_name_or_description_access_level** | **str** | Controls who can edit team name and description  | [optional] [readonly] 
**edit_team_visibility_or_trash_team_access_level** | **str** | Controls who can edit team visibility and trash teams  | [optional] [readonly] 
**member_invite_management_access_level** | **str** | Controls who can accept or deny member invites for a given team  | [optional] [readonly] 
**guest_invite_management_access_level** | **str** | Controls who can accept or deny guest invites for a given team  | [optional] [readonly] 
**join_request_management_access_level** | **str** | Controls who can accept or deny join team requests for a Membership by Request team  | [optional] [readonly] 
**team_member_removal_access_level** | **str** | Controls who can remove team members  | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.team_request import TeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRequest from a JSON string
team_request_instance = TeamRequest.from_json(json)
# print the JSON string representation of the object
print TeamRequest.to_json()

# convert the object into a dict
team_request_dict = team_request_instance.to_dict()
# create an instance of TeamRequest from a dict
team_request_form_dict = team_request.from_dict(team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

