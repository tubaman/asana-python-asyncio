# TeamCompact

A *team* is used to group related projects and people together within an organization. Each project in an organization is associated with a team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the team. | [optional] 

## Example

```python
from asana_asyncio.models.team_compact import TeamCompact

# TODO update the JSON string below
json = "{}"
# create an instance of TeamCompact from a JSON string
team_compact_instance = TeamCompact.from_json(json)
# print the JSON string representation of the object
print(TeamCompact.to_json())

# convert the object into a dict
team_compact_dict = team_compact_instance.to_dict()
# create an instance of TeamCompact from a dict
team_compact_from_dict = TeamCompact.from_dict(team_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


