# RemoveTagForTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskRemoveTagRequest**](TaskRemoveTagRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_tag_for_task_request import RemoveTagForTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveTagForTaskRequest from a JSON string
remove_tag_for_task_request_instance = RemoveTagForTaskRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveTagForTaskRequest.to_json())

# convert the object into a dict
remove_tag_for_task_request_dict = remove_tag_for_task_request_instance.to_dict()
# create an instance of RemoveTagForTaskRequest from a dict
remove_tag_for_task_request_from_dict = RemoveTagForTaskRequest.from_dict(remove_tag_for_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


