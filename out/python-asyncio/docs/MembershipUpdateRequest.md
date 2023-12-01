# MembershipUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role given to the member. Can be &#x60;editor&#x60; or &#x60;commenter&#x60;. | [optional] 

## Example

```python
from asana_asyncio.models.membership_update_request import MembershipUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipUpdateRequest from a JSON string
membership_update_request_instance = MembershipUpdateRequest.from_json(json)
# print the JSON string representation of the object
print MembershipUpdateRequest.to_json()

# convert the object into a dict
membership_update_request_dict = membership_update_request_instance.to_dict()
# create an instance of MembershipUpdateRequest from a dict
membership_update_request_form_dict = membership_update_request.from_dict(membership_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


