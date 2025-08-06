# TaskTemplateCompact

A *task template* is an object that allows new tasks to be created with a predefined setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the task template. | [optional] 

## Example

```python
from asana_asyncio.models.task_template_compact import TaskTemplateCompact

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateCompact from a JSON string
task_template_compact_instance = TaskTemplateCompact.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateCompact.to_json())

# convert the object into a dict
task_template_compact_dict = task_template_compact_instance.to_dict()
# create an instance of TaskTemplateCompact from a dict
task_template_compact_from_dict = TaskTemplateCompact.from_dict(task_template_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


