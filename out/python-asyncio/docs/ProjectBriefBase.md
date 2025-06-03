# ProjectBriefBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**title** | **str** | The title of the project brief. | [optional] 
**html_text** | **str** | HTML formatted text for the project brief. | [optional] 

## Example

```python
from asana_asyncio.models.project_brief_base import ProjectBriefBase

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBriefBase from a JSON string
project_brief_base_instance = ProjectBriefBase.from_json(json)
# print the JSON string representation of the object
print(ProjectBriefBase.to_json())

# convert the object into a dict
project_brief_base_dict = project_brief_base_instance.to_dict()
# create an instance of ProjectBriefBase from a dict
project_brief_base_from_dict = ProjectBriefBase.from_dict(project_brief_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


