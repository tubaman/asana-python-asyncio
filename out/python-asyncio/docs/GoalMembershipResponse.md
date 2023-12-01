# GoalMembershipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | The type of membership. | [optional] [readonly] 
**member** | [**MemberCompact**](MemberCompact.md) |  | [optional] 
**parent** | [**GoalMembershipBaseAllOfParent**](GoalMembershipBaseAllOfParent.md) |  | [optional] 
**role** | **str** | Describes if the member is a commenter or editor in goal. | [optional] 
**goal** | [**GoalMembershipBaseAllOfGoal**](GoalMembershipBaseAllOfGoal.md) |  | [optional] 
**user** | [**GoalMembershipResponseAllOfUser**](GoalMembershipResponseAllOfUser.md) |  | [optional] 
**workspace** | [**GoalMembershipResponseAllOfWorkspace**](GoalMembershipResponseAllOfWorkspace.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.goal_membership_response import GoalMembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoalMembershipResponse from a JSON string
goal_membership_response_instance = GoalMembershipResponse.from_json(json)
# print the JSON string representation of the object
print GoalMembershipResponse.to_json()

# convert the object into a dict
goal_membership_response_dict = goal_membership_response_instance.to_dict()
# create an instance of GoalMembershipResponse from a dict
goal_membership_response_form_dict = goal_membership_response.from_dict(goal_membership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


