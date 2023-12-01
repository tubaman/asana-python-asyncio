# WorkspaceCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the workspace. | [optional] 

## Example

```python
from asana_asyncio.models.workspace_compact import WorkspaceCompact

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCompact from a JSON string
workspace_compact_instance = WorkspaceCompact.from_json(json)
# print the JSON string representation of the object
print WorkspaceCompact.to_json()

# convert the object into a dict
workspace_compact_dict = workspace_compact_instance.to_dict()
# create an instance of WorkspaceCompact from a dict
workspace_compact_form_dict = workspace_compact.from_dict(workspace_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


