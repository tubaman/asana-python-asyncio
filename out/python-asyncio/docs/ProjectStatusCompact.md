# ProjectStatusCompact

*Deprecated: new integrations should prefer the `status_update` resource.* A *project status* is an update on the progress of a particular project, and is sent out to all project followers when created. These updates include both text describing the update and a color code intended to represent the overall state of the project: \"green\" for projects that are on track, \"yellow\" for projects at risk, and \"red\" for projects that are behind.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**title** | **str** | The title of the project status update. | [optional] 

## Example

```python
from asana_asyncio.models.project_status_compact import ProjectStatusCompact

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatusCompact from a JSON string
project_status_compact_instance = ProjectStatusCompact.from_json(json)
# print the JSON string representation of the object
print(ProjectStatusCompact.to_json())

# convert the object into a dict
project_status_compact_dict = project_status_compact_instance.to_dict()
# create an instance of ProjectStatusCompact from a dict
project_status_compact_from_dict = ProjectStatusCompact.from_dict(project_status_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


