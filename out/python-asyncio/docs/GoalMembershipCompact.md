# GoalMembershipCompact


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
**is_commenter** | **bool** | *Deprecated: new integrations should prefer the &#x60;role&#x60; field.* Describes if the member is comment only in goal. | [optional] [readonly] 
**is_editor** | **bool** | *Deprecated: new integrations should prefer the &#x60;role&#x60; field.* Describes if the member is editor in goal. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.goal_membership_compact import GoalMembershipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of GoalMembershipCompact from a JSON string
goal_membership_compact_instance = GoalMembershipCompact.from_json(json)
# print the JSON string representation of the object
print GoalMembershipCompact.to_json()

# convert the object into a dict
goal_membership_compact_dict = goal_membership_compact_instance.to_dict()
# create an instance of GoalMembershipCompact from a dict
goal_membership_compact_form_dict = goal_membership_compact.from_dict(goal_membership_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


