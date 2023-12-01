# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] [readonly] 
**photo** | [**UserBaseResponseAllOfPhoto**](UserBaseResponseAllOfPhoto.md) |  | [optional] 
**workspaces** | [**List[WorkspaceCompact]**](WorkspaceCompact.md) | Workspaces and organizations this user may access. Note\\: The API will only return workspaces and organizations that also contain the authenticated user. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print UserResponse.to_json()

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_form_dict = user_response.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


