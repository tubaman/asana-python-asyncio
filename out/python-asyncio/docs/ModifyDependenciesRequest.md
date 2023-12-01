# ModifyDependenciesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | **List[str]** | An array of task gids that a task depends on. | [optional] 

## Example

```python
from asana_asyncio.models.modify_dependencies_request import ModifyDependenciesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyDependenciesRequest from a JSON string
modify_dependencies_request_instance = ModifyDependenciesRequest.from_json(json)
# print the JSON string representation of the object
print ModifyDependenciesRequest.to_json()

# convert the object into a dict
modify_dependencies_request_dict = modify_dependencies_request_instance.to_dict()
# create an instance of ModifyDependenciesRequest from a dict
modify_dependencies_request_form_dict = modify_dependencies_request.from_dict(modify_dependencies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


