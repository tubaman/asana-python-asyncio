# ProjectStatusBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**title** | **str** | The title of the project status update. | [optional] 
**text** | **str** | The text content of the status update. | [optional] 
**html_text** | **str** | [Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML. | [optional] 
**color** | **str** | The color associated with the status update. | [optional] 

## Example

```python
from asana_asyncio.models.project_status_base import ProjectStatusBase

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatusBase from a JSON string
project_status_base_instance = ProjectStatusBase.from_json(json)
# print the JSON string representation of the object
print(ProjectStatusBase.to_json())

# convert the object into a dict
project_status_base_dict = project_status_base_instance.to_dict()
# create an instance of ProjectStatusBase from a dict
project_status_base_from_dict = ProjectStatusBase.from_dict(project_status_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


