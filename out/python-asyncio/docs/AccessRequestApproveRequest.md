# AccessRequestApproveRequest

A request to approve access for a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_gid** | **str** | The ID of the access request that the user is approving. | [optional] 

## Example

```python
from asana_asyncio.models.access_request_approve_request import AccessRequestApproveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestApproveRequest from a JSON string
access_request_approve_request_instance = AccessRequestApproveRequest.from_json(json)
# print the JSON string representation of the object
print(AccessRequestApproveRequest.to_json())

# convert the object into a dict
access_request_approve_request_dict = access_request_approve_request_instance.to_dict()
# create an instance of AccessRequestApproveRequest from a dict
access_request_approve_request_from_dict = AccessRequestApproveRequest.from_dict(access_request_approve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


