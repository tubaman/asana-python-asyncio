# RemoveUserForWorkspaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WorkspaceRemoveUserRequest**](WorkspaceRemoveUserRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_user_for_workspace_request import RemoveUserForWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserForWorkspaceRequest from a JSON string
remove_user_for_workspace_request_instance = RemoveUserForWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveUserForWorkspaceRequest.to_json())

# convert the object into a dict
remove_user_for_workspace_request_dict = remove_user_for_workspace_request_instance.to_dict()
# create an instance of RemoveUserForWorkspaceRequest from a dict
remove_user_for_workspace_request_from_dict = RemoveUserForWorkspaceRequest.from_dict(remove_user_for_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


