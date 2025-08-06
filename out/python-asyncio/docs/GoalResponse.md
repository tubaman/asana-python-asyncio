# GoalResponse


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
**likes** | [**List[Like]**](Like.md) | Array of likes for users who have liked this goal. | [optional] [readonly] 
**num_likes** | **int** | The number of users who have liked this goal. | [optional] [readonly] 
**team** | [**GoalResponseAllOfTeam**](GoalResponseAllOfTeam.md) |  | [optional] 
**workspace** | [**GoalResponseAllOfWorkspace**](GoalResponseAllOfWorkspace.md) |  | [optional] 
**followers** | [**List[UserCompact]**](UserCompact.md) | Array of users who are members of this goal. | [optional] 
**time_period** | [**GoalResponseAllOfTimePeriod**](GoalResponseAllOfTimePeriod.md) |  | [optional] 
**metric** | [**GoalResponseAllOfMetric**](GoalResponseAllOfMetric.md) |  | [optional] 
**owner** | [**GoalResponseAllOfOwner**](GoalResponseAllOfOwner.md) |  | [optional] 
**current_status_update** | [**StatusUpdateCompact**](StatusUpdateCompact.md) | The latest &#x60;status_update&#x60; posted to this goal. | [optional] 
**status** | **str** | The current status of this goal. When the goal is open, its status can be &#x60;green&#x60;, &#x60;yellow&#x60;, and &#x60;red&#x60; to reflect \&quot;On Track\&quot;, \&quot;At Risk\&quot;, and \&quot;Off Track\&quot;, respectively. When the goal is closed, the value can be &#x60;missed&#x60;, &#x60;achieved&#x60;, &#x60;partial&#x60;, or &#x60;dropped&#x60;. *Note* you can only write to this property if &#x60;metric&#x60; is set. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.goal_response import GoalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoalResponse from a JSON string
goal_response_instance = GoalResponse.from_json(json)
# print the JSON string representation of the object
print(GoalResponse.to_json())

# convert the object into a dict
goal_response_dict = goal_response_instance.to_dict()
# create an instance of GoalResponse from a dict
goal_response_from_dict = GoalResponse.from_dict(goal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


