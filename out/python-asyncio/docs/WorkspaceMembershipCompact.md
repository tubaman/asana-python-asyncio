# WorkspaceMembershipCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 
**workspace** | [**WorkspaceCompact**](WorkspaceCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.workspace_membership_compact import WorkspaceMembershipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembershipCompact from a JSON string
workspace_membership_compact_instance = WorkspaceMembershipCompact.from_json(json)
# print the JSON string representation of the object
print WorkspaceMembershipCompact.to_json()

# convert the object into a dict
workspace_membership_compact_dict = workspace_membership_compact_instance.to_dict()
# create an instance of WorkspaceMembershipCompact from a dict
workspace_membership_compact_form_dict = workspace_membership_compact.from_dict(workspace_membership_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


