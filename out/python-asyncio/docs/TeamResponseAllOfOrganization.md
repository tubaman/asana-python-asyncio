# TeamResponseAllOfOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the workspace. | [optional] 

## Example

```python
from asana_asyncio.models.team_response_all_of_organization import TeamResponseAllOfOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of TeamResponseAllOfOrganization from a JSON string
team_response_all_of_organization_instance = TeamResponseAllOfOrganization.from_json(json)
# print the JSON string representation of the object
print(TeamResponseAllOfOrganization.to_json())

# convert the object into a dict
team_response_all_of_organization_dict = team_response_all_of_organization_instance.to_dict()
# create an instance of TeamResponseAllOfOrganization from a dict
team_response_all_of_organization_from_dict = TeamResponseAllOfOrganization.from_dict(team_response_all_of_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


