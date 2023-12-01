# GetWorkspaceMembership200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WorkspaceMembershipResponse**](WorkspaceMembershipResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_workspace_membership200_response import GetWorkspaceMembership200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkspaceMembership200Response from a JSON string
get_workspace_membership200_response_instance = GetWorkspaceMembership200Response.from_json(json)
# print the JSON string representation of the object
print GetWorkspaceMembership200Response.to_json()

# convert the object into a dict
get_workspace_membership200_response_dict = get_workspace_membership200_response_instance.to_dict()
# create an instance of GetWorkspaceMembership200Response from a dict
get_workspace_membership200_response_form_dict = get_workspace_membership200_response.from_dict(get_workspace_membership200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


