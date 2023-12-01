# UserBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 
**email** | **str** | The user&#39;s email address. | [optional] [readonly] 
**photo** | [**UserBaseResponseAllOfPhoto**](UserBaseResponseAllOfPhoto.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.user_base_response import UserBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserBaseResponse from a JSON string
user_base_response_instance = UserBaseResponse.from_json(json)
# print the JSON string representation of the object
print UserBaseResponse.to_json()

# convert the object into a dict
user_base_response_dict = user_base_response_instance.to_dict()
# create an instance of UserBaseResponse from a dict
user_base_response_form_dict = user_base_response.from_dict(user_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


