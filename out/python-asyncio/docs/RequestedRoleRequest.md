# RequestedRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the template role in the project template. | [optional] 
**value** | **str** | The user id that should be assigned to the template role. | [optional] 

## Example

```python
from asana_asyncio.models.requested_role_request import RequestedRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedRoleRequest from a JSON string
requested_role_request_instance = RequestedRoleRequest.from_json(json)
# print the JSON string representation of the object
print(RequestedRoleRequest.to_json())

# convert the object into a dict
requested_role_request_dict = requested_role_request_instance.to_dict()
# create an instance of RequestedRoleRequest from a dict
requested_role_request_from_dict = RequestedRoleRequest.from_dict(requested_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


