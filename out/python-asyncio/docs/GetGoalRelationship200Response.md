# GetGoalRelationship200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoalRelationshipResponse**](GoalRelationshipResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_goal_relationship200_response import GetGoalRelationship200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGoalRelationship200Response from a JSON string
get_goal_relationship200_response_instance = GetGoalRelationship200Response.from_json(json)
# print the JSON string representation of the object
print GetGoalRelationship200Response.to_json()

# convert the object into a dict
get_goal_relationship200_response_dict = get_goal_relationship200_response_instance.to_dict()
# create an instance of GetGoalRelationship200Response from a dict
get_goal_relationship200_response_form_dict = get_goal_relationship200_response.from_dict(get_goal_relationship200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


