# MemberCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The type of the member (team or user) | [optional] 
**name** | **str** | The name of the member | [optional] 

## Example

```python
from asana_asyncio.models.member_compact import MemberCompact

# TODO update the JSON string below
json = "{}"
# create an instance of MemberCompact from a JSON string
member_compact_instance = MemberCompact.from_json(json)
# print the JSON string representation of the object
print MemberCompact.to_json()

# convert the object into a dict
member_compact_dict = member_compact_instance.to_dict()
# create an instance of MemberCompact from a dict
member_compact_form_dict = member_compact.from_dict(member_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


