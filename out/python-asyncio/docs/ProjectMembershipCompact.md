# ProjectMembershipCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**parent** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**member** | [**MemberCompact**](MemberCompact.md) |  | [optional] 
**access_level** | **str** | Whether the member has admin, editor, commenter, or viewer access to the project. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.project_membership_compact import ProjectMembershipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMembershipCompact from a JSON string
project_membership_compact_instance = ProjectMembershipCompact.from_json(json)
# print the JSON string representation of the object
print ProjectMembershipCompact.to_json()

# convert the object into a dict
project_membership_compact_dict = project_membership_compact_instance.to_dict()
# create an instance of ProjectMembershipCompact from a dict
project_membership_compact_form_dict = project_membership_compact.from_dict(project_membership_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


