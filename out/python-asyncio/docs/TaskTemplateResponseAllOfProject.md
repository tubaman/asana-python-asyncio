# TaskTemplateResponseAllOfProject

The project that this task template belongs to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 

## Example

```python
from asana_asyncio.models.task_template_response_all_of_project import TaskTemplateResponseAllOfProject

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateResponseAllOfProject from a JSON string
task_template_response_all_of_project_instance = TaskTemplateResponseAllOfProject.from_json(json)
# print the JSON string representation of the object
print TaskTemplateResponseAllOfProject.to_json()

# convert the object into a dict
task_template_response_all_of_project_dict = task_template_response_all_of_project_instance.to_dict()
# create an instance of TaskTemplateResponseAllOfProject from a dict
task_template_response_all_of_project_form_dict = task_template_response_all_of_project.from_dict(task_template_response_all_of_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


