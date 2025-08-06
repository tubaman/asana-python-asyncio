# AddTagForTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskAddTagRequest**](TaskAddTagRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_tag_for_task_request import AddTagForTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTagForTaskRequest from a JSON string
add_tag_for_task_request_instance = AddTagForTaskRequest.from_json(json)
# print the JSON string representation of the object
print(AddTagForTaskRequest.to_json())

# convert the object into a dict
add_tag_for_task_request_dict = add_tag_for_task_request_instance.to_dict()
# create an instance of AddTagForTaskRequest from a dict
add_tag_for_task_request_from_dict = AddTagForTaskRequest.from_dict(add_tag_for_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


