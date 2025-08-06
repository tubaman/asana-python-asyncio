# GetMemberships200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MembershipCompact]**](MembershipCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_memberships200_response import GetMemberships200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMemberships200Response from a JSON string
get_memberships200_response_instance = GetMemberships200Response.from_json(json)
# print the JSON string representation of the object
print(GetMemberships200Response.to_json())

# convert the object into a dict
get_memberships200_response_dict = get_memberships200_response_instance.to_dict()
# create an instance of GetMemberships200Response from a dict
get_memberships200_response_from_dict = GetMemberships200Response.from_dict(get_memberships200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


