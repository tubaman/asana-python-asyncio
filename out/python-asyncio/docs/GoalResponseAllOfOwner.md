# GoalResponseAllOfOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user&#39;s name. | [optional] 

## Example

```python
from asana_asyncio.models.goal_response_all_of_owner import GoalResponseAllOfOwner

# TODO update the JSON string below
json = "{}"
# create an instance of GoalResponseAllOfOwner from a JSON string
goal_response_all_of_owner_instance = GoalResponseAllOfOwner.from_json(json)
# print the JSON string representation of the object
print(GoalResponseAllOfOwner.to_json())

# convert the object into a dict
goal_response_all_of_owner_dict = goal_response_all_of_owner_instance.to_dict()
# create an instance of GoalResponseAllOfOwner from a dict
goal_response_all_of_owner_from_dict = GoalResponseAllOfOwner.from_dict(goal_response_all_of_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


