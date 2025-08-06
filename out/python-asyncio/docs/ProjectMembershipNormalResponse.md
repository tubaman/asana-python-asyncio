# ProjectMembershipNormalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**parent** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**member** | [**MemberCompact**](MemberCompact.md) |  | [optional] 
**access_level** | **str** | Whether the member has admin, editor, commenter, or viewer access to the project. | [optional] [readonly] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 
**project** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**write_access** | **str** | Whether the member has full access or comment-only access to the project. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.project_membership_normal_response import ProjectMembershipNormalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMembershipNormalResponse from a JSON string
project_membership_normal_response_instance = ProjectMembershipNormalResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectMembershipNormalResponse.to_json())

# convert the object into a dict
project_membership_normal_response_dict = project_membership_normal_response_instance.to_dict()
# create an instance of ProjectMembershipNormalResponse from a dict
project_membership_normal_response_from_dict = ProjectMembershipNormalResponse.from_dict(project_membership_normal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


