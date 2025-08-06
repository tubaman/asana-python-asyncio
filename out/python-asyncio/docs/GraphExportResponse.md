# GraphExportResponse

A generic Asana Resource, containing a globally unique identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | A *graph_export* object represents a request to export the data starting from a parent object | [optional] [readonly] 
**status** | **str** | The current status of this job. | [optional] [readonly] 
**new_graph_export** | [**GraphExportCompact**](GraphExportCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.graph_export_response import GraphExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GraphExportResponse from a JSON string
graph_export_response_instance = GraphExportResponse.from_json(json)
# print the JSON string representation of the object
print(GraphExportResponse.to_json())

# convert the object into a dict
graph_export_response_dict = graph_export_response_instance.to_dict()
# create an instance of GraphExportResponse from a dict
graph_export_response_from_dict = GraphExportResponse.from_dict(graph_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


