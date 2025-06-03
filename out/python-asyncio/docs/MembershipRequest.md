# MembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **str** | Sets the access level for the member. Goals can have access levels &#x60;editor&#x60; or &#x60;commenter&#x60;. Projects can have access levels &#x60;admin&#x60;, &#x60;editor&#x60; or &#x60;commenter&#x60;. Portfolios can have access levels &#x60;admin&#x60;, &#x60;editor&#x60; or &#x60;viewer&#x60;. Custom Fields can have access levels &#x60;admin&#x60;, &#x60;editor&#x60; or &#x60;user&#x60;. | [optional] 

## Example

```python
from asana_asyncio.models.membership_request import MembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipRequest from a JSON string
membership_request_instance = MembershipRequest.from_json(json)
# print the JSON string representation of the object
print(MembershipRequest.to_json())

# convert the object into a dict
membership_request_dict = membership_request_instance.to_dict()
# create an instance of MembershipRequest from a dict
membership_request_from_dict = MembershipRequest.from_dict(membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


