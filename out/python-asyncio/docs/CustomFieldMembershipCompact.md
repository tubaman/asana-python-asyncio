# CustomFieldMembershipCompact

This object describes a user's membership to a custom field including their level of access (Admin, Editor, or User).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | Type of the membership. | [optional] 
**parent** | [**CustomFieldCompact**](CustomFieldCompact.md) |  | [optional] 
**member** | [**UserCompact**](UserCompact.md) |  | [optional] 
**access_level** | **str** | Whether the member has admin, editor, or user access to the custom field. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.custom_field_membership_compact import CustomFieldMembershipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldMembershipCompact from a JSON string
custom_field_membership_compact_instance = CustomFieldMembershipCompact.from_json(json)
# print the JSON string representation of the object
print(CustomFieldMembershipCompact.to_json())

# convert the object into a dict
custom_field_membership_compact_dict = custom_field_membership_compact_instance.to_dict()
# create an instance of CustomFieldMembershipCompact from a dict
custom_field_membership_compact_from_dict = CustomFieldMembershipCompact.from_dict(custom_field_membership_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


