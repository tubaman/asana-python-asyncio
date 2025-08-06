# GraphExportCompact

A *graph_export* object represents a request to export the data starting from a parent object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**download_url** | **str** | Download this URL to retrieve the full export in JSON format. It will be compressed in a gzip (.gz) container.  *Note: May be null if the export is still in progress or failed.  If present, this URL may only be valid for 1 hour from the time of retrieval. You should avoid persisting this URL somewhere and rather refresh on demand to ensure you do not keep stale URLs.* | [optional] [readonly] 
**completed_at** | **datetime** | The time at which this resource was completed. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.graph_export_compact import GraphExportCompact

# TODO update the JSON string below
json = "{}"
# create an instance of GraphExportCompact from a JSON string
graph_export_compact_instance = GraphExportCompact.from_json(json)
# print the JSON string representation of the object
print(GraphExportCompact.to_json())

# convert the object into a dict
graph_export_compact_dict = graph_export_compact_instance.to_dict()
# create an instance of GraphExportCompact from a dict
graph_export_compact_from_dict = GraphExportCompact.from_dict(graph_export_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


