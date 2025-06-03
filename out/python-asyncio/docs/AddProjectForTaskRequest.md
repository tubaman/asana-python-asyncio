# AddProjectForTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskAddProjectRequest**](TaskAddProjectRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_project_for_task_request import AddProjectForTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddProjectForTaskRequest from a JSON string
add_project_for_task_request_instance = AddProjectForTaskRequest.from_json(json)
# print the JSON string representation of the object
print(AddProjectForTaskRequest.to_json())

# convert the object into a dict
add_project_for_task_request_dict = add_project_for_task_request_instance.to_dict()
# create an instance of AddProjectForTaskRequest from a dict
add_project_for_task_request_from_dict = AddProjectForTaskRequest.from_dict(add_project_for_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


