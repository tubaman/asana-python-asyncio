# DuplicateTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskDuplicateRequest**](TaskDuplicateRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.duplicate_task_request import DuplicateTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateTaskRequest from a JSON string
duplicate_task_request_instance = DuplicateTaskRequest.from_json(json)
# print the JSON string representation of the object
print DuplicateTaskRequest.to_json()

# convert the object into a dict
duplicate_task_request_dict = duplicate_task_request_instance.to_dict()
# create an instance of DuplicateTaskRequest from a dict
duplicate_task_request_form_dict = duplicate_task_request.from_dict(duplicate_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


