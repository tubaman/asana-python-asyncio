# GoalMembershipResponseAllOfUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.goal_membership_response_all_of_user import GoalMembershipResponseAllOfUser

# TODO update the JSON string below
json = "{}"
# create an instance of GoalMembershipResponseAllOfUser from a JSON string
goal_membership_response_all_of_user_instance = GoalMembershipResponseAllOfUser.from_json(json)
# print the JSON string representation of the object
print GoalMembershipResponseAllOfUser.to_json()

# convert the object into a dict
goal_membership_response_all_of_user_dict = goal_membership_response_all_of_user_instance.to_dict()
# create an instance of GoalMembershipResponseAllOfUser from a dict
goal_membership_response_all_of_user_form_dict = goal_membership_response_all_of_user.from_dict(goal_membership_response_all_of_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


