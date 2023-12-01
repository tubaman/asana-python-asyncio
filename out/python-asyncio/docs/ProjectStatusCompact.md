# ProjectStatusCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**title** | **str** | The title of the project status update. | [optional] 

## Example

```python
from asana_asyncio.models.project_status_compact import ProjectStatusCompact

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatusCompact from a JSON string
project_status_compact_instance = ProjectStatusCompact.from_json(json)
# print the JSON string representation of the object
print ProjectStatusCompact.to_json()

# convert the object into a dict
project_status_compact_dict = project_status_compact_instance.to_dict()
# create an instance of ProjectStatusCompact from a dict
project_status_compact_form_dict = project_status_compact.from_dict(project_status_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


