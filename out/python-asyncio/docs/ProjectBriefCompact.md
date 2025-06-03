# ProjectBriefCompact

A *Project Brief* allows you to explain the what and why of the project to your team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.project_brief_compact import ProjectBriefCompact

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBriefCompact from a JSON string
project_brief_compact_instance = ProjectBriefCompact.from_json(json)
# print the JSON string representation of the object
print(ProjectBriefCompact.to_json())

# convert the object into a dict
project_brief_compact_dict = project_brief_compact_instance.to_dict()
# create an instance of ProjectBriefCompact from a dict
project_brief_compact_from_dict = ProjectBriefCompact.from_dict(project_brief_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


