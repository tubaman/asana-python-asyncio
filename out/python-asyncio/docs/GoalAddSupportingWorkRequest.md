# GoalAddSupportingWorkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supporting_work** | **str** | The project/task/portfolio gid to add as supporting work for a goal | 

## Example

```python
from asana_asyncio.models.goal_add_supporting_work_request import GoalAddSupportingWorkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalAddSupportingWorkRequest from a JSON string
goal_add_supporting_work_request_instance = GoalAddSupportingWorkRequest.from_json(json)
# print the JSON string representation of the object
print GoalAddSupportingWorkRequest.to_json()

# convert the object into a dict
goal_add_supporting_work_request_dict = goal_add_supporting_work_request_instance.to_dict()
# create an instance of GoalAddSupportingWorkRequest from a dict
goal_add_supporting_work_request_form_dict = goal_add_supporting_work_request.from_dict(goal_add_supporting_work_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


