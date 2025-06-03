# GetGoal200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoalResponse**](GoalResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_goal200_response import GetGoal200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGoal200Response from a JSON string
get_goal200_response_instance = GetGoal200Response.from_json(json)
# print the JSON string representation of the object
print(GetGoal200Response.to_json())

# convert the object into a dict
get_goal200_response_dict = get_goal200_response_instance.to_dict()
# create an instance of GetGoal200Response from a dict
get_goal200_response_from_dict = GetGoal200Response.from_dict(get_goal200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


