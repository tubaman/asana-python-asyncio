# GoalMembershipBaseParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the goal. | [optional] 
**owner** | [**GoalCompactOwner**](GoalCompactOwner.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.goal_membership_base_parent import GoalMembershipBaseParent

# TODO update the JSON string below
json = "{}"
# create an instance of GoalMembershipBaseParent from a JSON string
goal_membership_base_parent_instance = GoalMembershipBaseParent.from_json(json)
# print the JSON string representation of the object
print(GoalMembershipBaseParent.to_json())

# convert the object into a dict
goal_membership_base_parent_dict = goal_membership_base_parent_instance.to_dict()
# create an instance of GoalMembershipBaseParent from a dict
goal_membership_base_parent_from_dict = GoalMembershipBaseParent.from_dict(goal_membership_base_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


