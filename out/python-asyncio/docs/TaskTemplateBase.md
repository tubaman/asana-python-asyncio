# TaskTemplateBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the task template. | [optional] 

## Example

```python
from asana_asyncio.models.task_template_base import TaskTemplateBase

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateBase from a JSON string
task_template_base_instance = TaskTemplateBase.from_json(json)
# print the JSON string representation of the object
print TaskTemplateBase.to_json()

# convert the object into a dict
task_template_base_dict = task_template_base_instance.to_dict()
# create an instance of TaskTemplateBase from a dict
task_template_base_form_dict = task_template_base.from_dict(task_template_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


