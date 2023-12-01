# ProjectTemplateBaseAllOfTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the team. | [optional] 

## Example

```python
from asana_asyncio.models.project_template_base_all_of_team import ProjectTemplateBaseAllOfTeam

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateBaseAllOfTeam from a JSON string
project_template_base_all_of_team_instance = ProjectTemplateBaseAllOfTeam.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateBaseAllOfTeam.to_json()

# convert the object into a dict
project_template_base_all_of_team_dict = project_template_base_all_of_team_instance.to_dict()
# create an instance of ProjectTemplateBaseAllOfTeam from a dict
project_template_base_all_of_team_form_dict = project_template_base_all_of_team.from_dict(project_template_base_all_of_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


