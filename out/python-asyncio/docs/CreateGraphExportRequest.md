# CreateGraphExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GraphExportRequest**](GraphExportRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_graph_export_request import CreateGraphExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGraphExportRequest from a JSON string
create_graph_export_request_instance = CreateGraphExportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGraphExportRequest.to_json())

# convert the object into a dict
create_graph_export_request_dict = create_graph_export_request_instance.to_dict()
# create an instance of CreateGraphExportRequest from a dict
create_graph_export_request_from_dict = CreateGraphExportRequest.from_dict(create_graph_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


