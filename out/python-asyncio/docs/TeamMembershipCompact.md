# TeamMembershipCompact

This object represents a user's connection to a team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 
**team** | [**TeamCompact**](TeamCompact.md) |  | [optional] 
**is_guest** | **bool** | Describes if the user is a guest in the team. | [optional] 
**is_limited_access** | **bool** | Describes if the user has limited access to the team. | [optional] [readonly] 
**is_admin** | **bool** | Describes if the user is a team admin. | [optional] 

## Example

```python
from asana_asyncio.models.team_membership_compact import TeamMembershipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMembershipCompact from a JSON string
team_membership_compact_instance = TeamMembershipCompact.from_json(json)
# print the JSON string representation of the object
print(TeamMembershipCompact.to_json())

# convert the object into a dict
team_membership_compact_dict = team_membership_compact_instance.to_dict()
# create an instance of TeamMembershipCompact from a dict
team_membership_compact_from_dict = TeamMembershipCompact.from_dict(team_membership_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


