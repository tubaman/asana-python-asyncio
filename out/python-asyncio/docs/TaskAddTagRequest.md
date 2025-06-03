# TaskAddTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | The tag&#39;s gid to add to the task. | 

## Example

```python
from asana_asyncio.models.task_add_tag_request import TaskAddTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskAddTagRequest from a JSON string
task_add_tag_request_instance = TaskAddTagRequest.from_json(json)
# print the JSON string representation of the object
print(TaskAddTagRequest.to_json())

# convert the object into a dict
task_add_tag_request_dict = task_add_tag_request_instance.to_dict()
# create an instance of TaskAddTagRequest from a dict
task_add_tag_request_from_dict = TaskAddTagRequest.from_dict(task_add_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


