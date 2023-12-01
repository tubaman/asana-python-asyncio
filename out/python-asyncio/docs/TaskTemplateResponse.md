# TaskTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the task template. | [optional] 
**project** | [**TaskTemplateResponseAllOfProject**](TaskTemplateResponseAllOfProject.md) |  | [optional] 
**template** | [**TaskTemplateResponseAllOfTemplate**](TaskTemplateResponseAllOfTemplate.md) |  | [optional] 
**created_by** | [**TaskTemplateResponseAllOfCreatedBy**](TaskTemplateResponseAllOfCreatedBy.md) |  | [optional] 
**created_at** | **datetime** | The time at which this task template was created. | [optional] 

## Example

```python
from asana_asyncio.models.task_template_response import TaskTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateResponse from a JSON string
task_template_response_instance = TaskTemplateResponse.from_json(json)
# print the JSON string representation of the object
print TaskTemplateResponse.to_json()

# convert the object into a dict
task_template_response_dict = task_template_response_instance.to_dict()
# create an instance of TaskTemplateResponse from a dict
task_template_response_form_dict = task_template_response.from_dict(task_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


