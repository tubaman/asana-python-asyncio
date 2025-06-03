# MembershipCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | Type of the membership. | [optional] 
**member** | [**UserCompact**](UserCompact.md) |  | [optional] 
**parent** | [**CustomFieldCompact**](CustomFieldCompact.md) |  | [optional] 
**role** | **str** | *Deprecated: Describes if the member is a commenter or editor in goal.* | [optional] 
**access_level** | **str** | Whether the member has admin, editor, or user access to the custom field. | [optional] [readonly] 
**goal** | [**GoalMembershipBaseGoal**](GoalMembershipBaseGoal.md) |  | [optional] 
**is_commenter** | **bool** | *Deprecated: new integrations should prefer the &#x60;role&#x60; field.* Describes if the member is comment only in goal. | [optional] [readonly] 
**is_editor** | **bool** | *Deprecated: new integrations should prefer the &#x60;role&#x60; field.* Describes if the member is editor in goal. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.membership_compact import MembershipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipCompact from a JSON string
membership_compact_instance = MembershipCompact.from_json(json)
# print the JSON string representation of the object
print(MembershipCompact.to_json())

# convert the object into a dict
membership_compact_dict = membership_compact_instance.to_dict()
# create an instance of MembershipCompact from a dict
membership_compact_from_dict = MembershipCompact.from_dict(membership_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


