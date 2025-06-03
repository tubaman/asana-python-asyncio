# TaskTemplateRecipeCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the task that will be created from this template. | [optional] 
**task_resource_subtype** | **str** | The subtype of the task that will be created from this template. | [optional] 

## Example

```python
from asana_asyncio.models.task_template_recipe_compact import TaskTemplateRecipeCompact

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateRecipeCompact from a JSON string
task_template_recipe_compact_instance = TaskTemplateRecipeCompact.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateRecipeCompact.to_json())

# convert the object into a dict
task_template_recipe_compact_dict = task_template_recipe_compact_instance.to_dict()
# create an instance of TaskTemplateRecipeCompact from a dict
task_template_recipe_compact_from_dict = TaskTemplateRecipeCompact.from_dict(task_template_recipe_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


