# UserCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.user_compact import UserCompact

# TODO update the JSON string below
json = "{}"
# create an instance of UserCompact from a JSON string
user_compact_instance = UserCompact.from_json(json)
# print the JSON string representation of the object
print UserCompact.to_json()

# convert the object into a dict
user_compact_dict = user_compact_instance.to_dict()
# create an instance of UserCompact from a dict
user_compact_form_dict = user_compact.from_dict(user_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


