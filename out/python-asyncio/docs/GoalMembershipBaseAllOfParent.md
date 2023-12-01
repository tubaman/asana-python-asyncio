# GoalMembershipBaseAllOfParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the goal. | [optional] 
**owner** | [**GoalCompactAllOfOwner**](GoalCompactAllOfOwner.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.goal_membership_base_all_of_parent import GoalMembershipBaseAllOfParent

# TODO update the JSON string below
json = "{}"
# create an instance of GoalMembershipBaseAllOfParent from a JSON string
goal_membership_base_all_of_parent_instance = GoalMembershipBaseAllOfParent.from_json(json)
# print the JSON string representation of the object
print GoalMembershipBaseAllOfParent.to_json()

# convert the object into a dict
goal_membership_base_all_of_parent_dict = goal_membership_base_all_of_parent_instance.to_dict()
# create an instance of GoalMembershipBaseAllOfParent from a dict
goal_membership_base_all_of_parent_form_dict = goal_membership_base_all_of_parent.from_dict(goal_membership_base_all_of_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


