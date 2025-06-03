# TaskRemoveTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | The tag&#39;s gid to remove from the task. | 

## Example

```python
from asana_asyncio.models.task_remove_tag_request import TaskRemoveTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskRemoveTagRequest from a JSON string
task_remove_tag_request_instance = TaskRemoveTagRequest.from_json(json)
# print the JSON string representation of the object
print(TaskRemoveTagRequest.to_json())

# convert the object into a dict
task_remove_tag_request_dict = task_remove_tag_request_instance.to_dict()
# create an instance of TaskRemoveTagRequest from a dict
task_remove_tag_request_from_dict = TaskRemoveTagRequest.from_dict(task_remove_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


