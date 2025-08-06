# AccessRequestTargetIdCompact

A *target id* object represents the target resource that the requester wants access to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.access_request_target_id_compact import AccessRequestTargetIdCompact

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestTargetIdCompact from a JSON string
access_request_target_id_compact_instance = AccessRequestTargetIdCompact.from_json(json)
# print the JSON string representation of the object
print(AccessRequestTargetIdCompact.to_json())

# convert the object into a dict
access_request_target_id_compact_dict = access_request_target_id_compact_instance.to_dict()
# create an instance of AccessRequestTargetIdCompact from a dict
access_request_target_id_compact_from_dict = AccessRequestTargetIdCompact.from_dict(access_request_target_id_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


