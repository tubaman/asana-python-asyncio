# EventResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.event_response_user import EventResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponseUser from a JSON string
event_response_user_instance = EventResponseUser.from_json(json)
# print the JSON string representation of the object
print EventResponseUser.to_json()

# convert the object into a dict
event_response_user_dict = event_response_user_instance.to_dict()
# create an instance of EventResponseUser from a dict
event_response_user_form_dict = event_response_user.from_dict(event_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


