# WorkspaceAddUserRequest

A user identification object for specification with the addUser/removeUser endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 

## Example

```python
from asana_asyncio.models.workspace_add_user_request import WorkspaceAddUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceAddUserRequest from a JSON string
workspace_add_user_request_instance = WorkspaceAddUserRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceAddUserRequest.to_json())

# convert the object into a dict
workspace_add_user_request_dict = workspace_add_user_request_instance.to_dict()
# create an instance of WorkspaceAddUserRequest from a dict
workspace_add_user_request_from_dict = WorkspaceAddUserRequest.from_dict(workspace_add_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


