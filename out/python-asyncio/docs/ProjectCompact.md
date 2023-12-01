# ProjectCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 

## Example

```python
from asana_asyncio.models.project_compact import ProjectCompact

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCompact from a JSON string
project_compact_instance = ProjectCompact.from_json(json)
# print the JSON string representation of the object
print ProjectCompact.to_json()

# convert the object into a dict
project_compact_dict = project_compact_instance.to_dict()
# create an instance of ProjectCompact from a dict
project_compact_form_dict = project_compact.from_dict(project_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


