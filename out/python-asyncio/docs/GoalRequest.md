# GoalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the goal. | [optional] 
**html_notes** | **str** | The notes of the goal with formatting as HTML. | [optional] 
**notes** | **str** | Free-form textual information associated with the goal (i.e. its description). | [optional] 
**due_on** | **str** | The localized day on which this goal is due. This takes a date with format &#x60;YYYY-MM-DD&#x60;. | [optional] 
**start_on** | **str** | The day on which work for this goal begins, or null if the goal has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format, and cannot be set unless there is an accompanying due date. | [optional] 
**is_workspace_level** | **bool** | *Conditional*. This property is only present when the &#x60;workspace&#x60; provided is an organization. Whether the goal belongs to the &#x60;workspace&#x60; (and is listed as part of the workspace’s goals) or not. If it isn’t a workspace-level goal, it is a team-level goal, and is associated with the goal’s team. | [optional] 
**liked** | **bool** | True if the goal is liked by the authorized user, false if not. | [optional] 
**team** | **str** | *Conditional*. This property is only present when the &#x60;workspace&#x60; provided is an organization. | [optional] 
**workspace** | **str** | The &#x60;gid&#x60; of a workspace. | [optional] 
**time_period** | **str** | The &#x60;gid&#x60; of a time period. | [optional] 
**owner** | **str** | The &#x60;gid&#x60; of a user. | [optional] 
**followers** | **List[str]** |  | [optional] 

## Example

```python
from asana_asyncio.models.goal_request import GoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRequest from a JSON string
goal_request_instance = GoalRequest.from_json(json)
# print the JSON string representation of the object
print(GoalRequest.to_json())

# convert the object into a dict
goal_request_dict = goal_request_instance.to_dict()
# create an instance of GoalRequest from a dict
goal_request_from_dict = GoalRequest.from_dict(goal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


