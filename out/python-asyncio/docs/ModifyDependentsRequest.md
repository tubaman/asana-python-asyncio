# ModifyDependentsRequest

A set of dependent tasks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependents** | **List[str]** | An array of task gids that are dependents of the given task. | [optional] 

## Example

```python
from asana_asyncio.models.modify_dependents_request import ModifyDependentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyDependentsRequest from a JSON string
modify_dependents_request_instance = ModifyDependentsRequest.from_json(json)
# print the JSON string representation of the object
print ModifyDependentsRequest.to_json()

# convert the object into a dict
modify_dependents_request_dict = modify_dependents_request_instance.to_dict()
# create an instance of ModifyDependentsRequest from a dict
modify_dependents_request_form_dict = modify_dependents_request.from_dict(modify_dependents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


