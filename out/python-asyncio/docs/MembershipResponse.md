# MembershipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**resource_subtype** | **str** | Type of the membership. | [optional] 
**member** | [**MemberCompact**](MemberCompact.md) |  | [optional] 
**parent** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**role** | **str** | Describes if the member is a commenter or editor in goal. | [optional] 
**goal** | [**GoalMembershipBaseAllOfGoal**](GoalMembershipBaseAllOfGoal.md) |  | [optional] 
**user** | [**GoalMembershipResponseAllOfUser**](GoalMembershipResponseAllOfUser.md) |  | [optional] 
**workspace** | [**GoalMembershipResponseAllOfWorkspace**](GoalMembershipResponseAllOfWorkspace.md) |  | [optional] 
**access_level** | **str** | Whether the member has admin, editor, commenter, or viewer access to the project. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.membership_response import MembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipResponse from a JSON string
membership_response_instance = MembershipResponse.from_json(json)
# print the JSON string representation of the object
print MembershipResponse.to_json()

# convert the object into a dict
membership_response_dict = membership_response_instance.to_dict()
# create an instance of MembershipResponse from a dict
membership_response_form_dict = membership_response.from_dict(membership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

