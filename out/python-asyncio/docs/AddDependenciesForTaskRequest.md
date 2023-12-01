# AddDependenciesForTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModifyDependenciesRequest**](ModifyDependenciesRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_dependencies_for_task_request import AddDependenciesForTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDependenciesForTaskRequest from a JSON string
add_dependencies_for_task_request_instance = AddDependenciesForTaskRequest.from_json(json)
# print the JSON string representation of the object
print AddDependenciesForTaskRequest.to_json()

# convert the object into a dict
add_dependencies_for_task_request_dict = add_dependencies_for_task_request_instance.to_dict()
# create an instance of AddDependenciesForTaskRequest from a dict
add_dependencies_for_task_request_form_dict = add_dependencies_for_task_request.from_dict(add_dependencies_for_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


