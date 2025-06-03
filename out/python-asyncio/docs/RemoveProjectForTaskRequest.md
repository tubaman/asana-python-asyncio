# RemoveProjectForTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskRemoveProjectRequest**](TaskRemoveProjectRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_project_for_task_request import RemoveProjectForTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProjectForTaskRequest from a JSON string
remove_project_for_task_request_instance = RemoveProjectForTaskRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveProjectForTaskRequest.to_json())

# convert the object into a dict
remove_project_for_task_request_dict = remove_project_for_task_request_instance.to_dict()
# create an instance of RemoveProjectForTaskRequest from a dict
remove_project_for_task_request_from_dict = RemoveProjectForTaskRequest.from_dict(remove_project_for_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


