# AccessRequestRejectRequest

A request to reject access for a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_gid** | **str** | The ID of the access request that the user is rejecting. | [optional] 

## Example

```python
from asana_asyncio.models.access_request_reject_request import AccessRequestRejectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestRejectRequest from a JSON string
access_request_reject_request_instance = AccessRequestRejectRequest.from_json(json)
# print the JSON string representation of the object
print(AccessRequestRejectRequest.to_json())

# convert the object into a dict
access_request_reject_request_dict = access_request_reject_request_instance.to_dict()
# create an instance of AccessRequestRejectRequest from a dict
access_request_reject_request_from_dict = AccessRequestRejectRequest.from_dict(access_request_reject_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


