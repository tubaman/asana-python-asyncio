# AccessRequestCreateRequest

A request to create shareable access for a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | The access requestable object that the user is requesting access to. This is the gid of the target. Supports projects and portfolios. | 
**message** | **str** | The optional message to include with the access request. This can be used to provide context or additional information about the request. | [optional] 

## Example

```python
from asana_asyncio.models.access_request_create_request import AccessRequestCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestCreateRequest from a JSON string
access_request_create_request_instance = AccessRequestCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AccessRequestCreateRequest.to_json())

# convert the object into a dict
access_request_create_request_dict = access_request_create_request_instance.to_dict()
# create an instance of AccessRequestCreateRequest from a dict
access_request_create_request_from_dict = AccessRequestCreateRequest.from_dict(access_request_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


