# TaskCompactAllOfCreatedBy

[Opt In](/docs/inputoutput-options). A *user* object represents an account in Asana that can be given access to various workspaces, projects, and tasks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource. | [optional] 
**resource_type** | **str** | The type of resource. | [optional] 

## Example

```python
from asana_asyncio.models.task_compact_all_of_created_by import TaskCompactAllOfCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCompactAllOfCreatedBy from a JSON string
task_compact_all_of_created_by_instance = TaskCompactAllOfCreatedBy.from_json(json)
# print the JSON string representation of the object
print TaskCompactAllOfCreatedBy.to_json()

# convert the object into a dict
task_compact_all_of_created_by_dict = task_compact_all_of_created_by_instance.to_dict()
# create an instance of TaskCompactAllOfCreatedBy from a dict
task_compact_all_of_created_by_form_dict = task_compact_all_of_created_by.from_dict(task_compact_all_of_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


