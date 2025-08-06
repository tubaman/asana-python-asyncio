# AccessRequestResponse

A *access request* object represents a request to access a shareable resource within Asana. It includes the requester's information, approval status, and target resource details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**message** | **str** | The message included in the access request, if any. | [optional] 
**approval_status** | **str** | The current approval status of the request. | [optional] 
**requester** | [**UserCompact**](UserCompact.md) |  | [optional] 
**target** | [**AccessRequestTargetIdCompact**](AccessRequestTargetIdCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.access_request_response import AccessRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestResponse from a JSON string
access_request_response_instance = AccessRequestResponse.from_json(json)
# print the JSON string representation of the object
print(AccessRequestResponse.to_json())

# convert the object into a dict
access_request_response_dict = access_request_response_instance.to_dict()
# create an instance of AccessRequestResponse from a dict
access_request_response_from_dict = AccessRequestResponse.from_dict(access_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


