# Like

An object to represent a user's like.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the object, as a string. | [optional] [readonly] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.like import Like

# TODO update the JSON string below
json = "{}"
# create an instance of Like from a JSON string
like_instance = Like.from_json(json)
# print the JSON string representation of the object
print Like.to_json()

# convert the object into a dict
like_dict = like_instance.to_dict()
# create an instance of Like from a dict
like_form_dict = like.from_dict(like_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


