# AddUserForWorkspaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WorkspaceAddUserRequest**](WorkspaceAddUserRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_user_for_workspace_request import AddUserForWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserForWorkspaceRequest from a JSON string
add_user_for_workspace_request_instance = AddUserForWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(AddUserForWorkspaceRequest.to_json())

# convert the object into a dict
add_user_for_workspace_request_dict = add_user_for_workspace_request_instance.to_dict()
# create an instance of AddUserForWorkspaceRequest from a dict
add_user_for_workspace_request_from_dict = AddUserForWorkspaceRequest.from_dict(add_user_for_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


