# TaskTemplateInstantiateTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new task. If not provided, the name of the task template will be used. | [optional] 

## Example

```python
from asana_asyncio.models.task_template_instantiate_task_request import TaskTemplateInstantiateTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateInstantiateTaskRequest from a JSON string
task_template_instantiate_task_request_instance = TaskTemplateInstantiateTaskRequest.from_json(json)
# print the JSON string representation of the object
print TaskTemplateInstantiateTaskRequest.to_json()

# convert the object into a dict
task_template_instantiate_task_request_dict = task_template_instantiate_task_request_instance.to_dict()
# create an instance of TaskTemplateInstantiateTaskRequest from a dict
task_template_instantiate_task_request_form_dict = task_template_instantiate_task_request.from_dict(task_template_instantiate_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


