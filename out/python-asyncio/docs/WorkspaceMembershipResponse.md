# WorkspaceMembershipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 
**workspace** | [**WorkspaceCompact**](WorkspaceCompact.md) |  | [optional] 
**user_task_list** | [**UserTaskListCompact**](UserTaskListCompact.md) |  | [optional] 
**is_active** | **bool** | Reflects if this user still a member of the workspace. | [optional] [readonly] 
**is_admin** | **bool** | Reflects if this user is an admin of the workspace. | [optional] [readonly] 
**is_guest** | **bool** | Reflects if this user is a guest of the workspace. | [optional] [readonly] 
**vacation_dates** | [**WorkspaceMembershipResponseAllOfVacationDates**](WorkspaceMembershipResponseAllOfVacationDates.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.workspace_membership_response import WorkspaceMembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembershipResponse from a JSON string
workspace_membership_response_instance = WorkspaceMembershipResponse.from_json(json)
# print the JSON string representation of the object
print WorkspaceMembershipResponse.to_json()

# convert the object into a dict
workspace_membership_response_dict = workspace_membership_response_instance.to_dict()
# create an instance of WorkspaceMembershipResponse from a dict
workspace_membership_response_form_dict = workspace_membership_response.from_dict(workspace_membership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


