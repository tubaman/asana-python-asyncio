# TaskTemplateResponseAllOfTemplate

The configuration for the task that will be created from this template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the task that will be created from this template. | [optional] 
**task_resource_subtype** | **str** | The subtype of the task that will be created from this template. | [optional] 
**description** | **str** | Description of the task that will be created from this template. | [optional] 
**html_description** | **str** | HTML description of the task that will be created from this template. | [optional] 
**memberships** | [**List[ProjectCompact]**](ProjectCompact.md) | Array of projects that the task created from this template will be added to | [optional] 
**relative_start_on** | **int** | The number of days after the task has been instantiated on which that the task will start | [optional] 
**relative_due_on** | **int** | The number of days after the task has been instantiated on which that the task will be due | [optional] 
**due_time** | **str** | The time of day that the task will be due | [optional] 
**dependencies** | [**List[TaskTemplateRecipeCompact]**](TaskTemplateRecipeCompact.md) | Array of task templates that the task created from this template will depend on | [optional] 
**dependents** | [**List[TaskTemplateRecipeCompact]**](TaskTemplateRecipeCompact.md) | Array of task templates that will depend on the task created from this template | [optional] 
**followers** | [**List[UserCompact]**](UserCompact.md) | Array of users that will be added as followers to the task created from this template | [optional] 
**attachments** | [**List[AttachmentCompact]**](AttachmentCompact.md) | Array of attachments that will be added to the task created from this template | [optional] 
**subtasks** | [**List[TaskTemplateRecipeCompact]**](TaskTemplateRecipeCompact.md) | Array of subtasks that will be added to the task created from this template | [optional] 
**custom_fields** | [**List[CustomFieldCompact]**](CustomFieldCompact.md) | Array of custom fields that will be added to the task created from this template | [optional] 

## Example

```python
from asana_asyncio.models.task_template_response_all_of_template import TaskTemplateResponseAllOfTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateResponseAllOfTemplate from a JSON string
task_template_response_all_of_template_instance = TaskTemplateResponseAllOfTemplate.from_json(json)
# print the JSON string representation of the object
print TaskTemplateResponseAllOfTemplate.to_json()

# convert the object into a dict
task_template_response_all_of_template_dict = task_template_response_all_of_template_instance.to_dict()
# create an instance of TaskTemplateResponseAllOfTemplate from a dict
task_template_response_all_of_template_form_dict = task_template_response_all_of_template.from_dict(task_template_response_all_of_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


