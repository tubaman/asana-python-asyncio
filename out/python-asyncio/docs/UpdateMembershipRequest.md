# UpdateMembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MembershipRequest**](MembershipRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_membership_request import UpdateMembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembershipRequest from a JSON string
update_membership_request_instance = UpdateMembershipRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMembershipRequest.to_json())

# convert the object into a dict
update_membership_request_dict = update_membership_request_instance.to_dict()
# create an instance of UpdateMembershipRequest from a dict
update_membership_request_from_dict = UpdateMembershipRequest.from_dict(update_membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


