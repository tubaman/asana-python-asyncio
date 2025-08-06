# GraphExportRequest

A *graph_export* request starts a job to export data starting from a parent object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **str** | Globally unique ID of the parent object: project, portfolio, or team. | [optional] 

## Example

```python
from asana_asyncio.models.graph_export_request import GraphExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GraphExportRequest from a JSON string
graph_export_request_instance = GraphExportRequest.from_json(json)
# print the JSON string representation of the object
print(GraphExportRequest.to_json())

# convert the object into a dict
graph_export_request_dict = graph_export_request_instance.to_dict()
# create an instance of GraphExportRequest from a dict
graph_export_request_from_dict = GraphExportRequest.from_dict(graph_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


