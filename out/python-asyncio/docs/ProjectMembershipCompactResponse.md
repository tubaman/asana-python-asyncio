# ProjectMembershipCompactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**parent** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**member** | [**MemberCompact**](MemberCompact.md) |  | [optional] 
**access_level** | **str** | Whether the member has admin, editor, commenter, or viewer access to the project. | [optional] [readonly] 
**resource_subtype** | **str** | Type of the membership. | [optional] 

## Example

```python
from asana_asyncio.models.project_membership_compact_response import ProjectMembershipCompactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMembershipCompactResponse from a JSON string
project_membership_compact_response_instance = ProjectMembershipCompactResponse.from_json(json)
# print the JSON string representation of the object
print ProjectMembershipCompactResponse.to_json()

# convert the object into a dict
project_membership_compact_response_dict = project_membership_compact_response_instance.to_dict()
# create an instance of ProjectMembershipCompactResponse from a dict
project_membership_compact_response_form_dict = project_membership_compact_response.from_dict(project_membership_compact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


