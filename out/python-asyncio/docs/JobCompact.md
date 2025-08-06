# JobCompact

A *job* is an object representing a process that handles asynchronous work.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**status** | **str** | The current status of this job. | [optional] [readonly] 
**new_project** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**new_task** | [**JobCompactNewTask**](JobCompactNewTask.md) |  | [optional] 
**new_project_template** | [**ProjectTemplateCompact**](ProjectTemplateCompact.md) |  | [optional] 
**new_graph_export** | [**GraphExportCompact**](GraphExportCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.job_compact import JobCompact

# TODO update the JSON string below
json = "{}"
# create an instance of JobCompact from a JSON string
job_compact_instance = JobCompact.from_json(json)
# print the JSON string representation of the object
print(JobCompact.to_json())

# convert the object into a dict
job_compact_dict = job_compact_instance.to_dict()
# create an instance of JobCompact from a dict
job_compact_from_dict = JobCompact.from_dict(job_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


