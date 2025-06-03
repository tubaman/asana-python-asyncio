# OrganizationExportCompact

An *organization_export* object represents a request to export the complete data of an Organization in JSON format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**download_url** | **str** | Download this URL to retreive the full export of the organization in JSON format. It will be compressed in a gzip (.gz) container.  *Note: May be null if the export is still in progress or failed.  If present, this URL may only be valid for 1 hour from the time of retrieval. You should avoid persisting this URL somewhere and rather refresh on demand to ensure you do not keep stale URLs.* | [optional] [readonly] 
**state** | **str** | The current state of the export. | [optional] [readonly] 
**organization** | [**WorkspaceCompact**](WorkspaceCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.organization_export_compact import OrganizationExportCompact

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationExportCompact from a JSON string
organization_export_compact_instance = OrganizationExportCompact.from_json(json)
# print the JSON string representation of the object
print(OrganizationExportCompact.to_json())

# convert the object into a dict
organization_export_compact_dict = organization_export_compact_instance.to_dict()
# create an instance of OrganizationExportCompact from a dict
organization_export_compact_from_dict = OrganizationExportCompact.from_dict(organization_export_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


