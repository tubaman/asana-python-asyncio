# AddDependentsForTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModifyDependentsRequest**](ModifyDependentsRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_dependents_for_task_request import AddDependentsForTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDependentsForTaskRequest from a JSON string
add_dependents_for_task_request_instance = AddDependentsForTaskRequest.from_json(json)
# print the JSON string representation of the object
print AddDependentsForTaskRequest.to_json()

# convert the object into a dict
add_dependents_for_task_request_dict = add_dependents_for_task_request_instance.to_dict()
# create an instance of AddDependentsForTaskRequest from a dict
add_dependents_for_task_request_form_dict = add_dependents_for_task_request.from_dict(add_dependents_for_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


