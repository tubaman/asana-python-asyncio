# UpdateGoalRelationshipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoalRelationshipRequest**](GoalRelationshipRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_goal_relationship_request import UpdateGoalRelationshipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalRelationshipRequest from a JSON string
update_goal_relationship_request_instance = UpdateGoalRelationshipRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGoalRelationshipRequest.to_json())

# convert the object into a dict
update_goal_relationship_request_dict = update_goal_relationship_request_instance.to_dict()
# create an instance of UpdateGoalRelationshipRequest from a dict
update_goal_relationship_request_from_dict = UpdateGoalRelationshipRequest.from_dict(update_goal_relationship_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


