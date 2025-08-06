# ProjectTemplateCompact

A *project template* is an object that allows new projects to be created with a predefined setup, which may include tasks, sections, Rules, etc. It simplifies the process of running a workflow that involves a similar set of work every time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project template. | [optional] 

## Example

```python
from asana_asyncio.models.project_template_compact import ProjectTemplateCompact

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateCompact from a JSON string
project_template_compact_instance = ProjectTemplateCompact.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplateCompact.to_json())

# convert the object into a dict
project_template_compact_dict = project_template_compact_instance.to_dict()
# create an instance of ProjectTemplateCompact from a dict
project_template_compact_from_dict = ProjectTemplateCompact.from_dict(project_template_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


