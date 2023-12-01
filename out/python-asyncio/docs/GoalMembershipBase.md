# GoalMembershipBase


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

## Example

```python
from asana_asyncio.models.goal_membership_base import GoalMembershipBase

# TODO update the JSON string below
json = "{}"
# create an instance of GoalMembershipBase from a JSON string
goal_membership_base_instance = GoalMembershipBase.from_json(json)
# print the JSON string representation of the object
print GoalMembershipBase.to_json()

# convert the object into a dict
goal_membership_base_dict = goal_membership_base_instance.to_dict()
# create an instance of GoalMembershipBase from a dict
goal_membership_base_form_dict = goal_membership_base.from_dict(goal_membership_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


