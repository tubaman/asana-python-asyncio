# GetProjectMembershipsForProject200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProjectMembershipCompact]**](ProjectMembershipCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_project_memberships_for_project200_response import GetProjectMembershipsForProject200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectMembershipsForProject200Response from a JSON string
get_project_memberships_for_project200_response_instance = GetProjectMembershipsForProject200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjectMembershipsForProject200Response.to_json())

# convert the object into a dict
get_project_memberships_for_project200_response_dict = get_project_memberships_for_project200_response_instance.to_dict()
# create an instance of GetProjectMembershipsForProject200Response from a dict
get_project_memberships_for_project200_response_from_dict = GetProjectMembershipsForProject200Response.from_dict(get_project_memberships_for_project200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


