# ProjectTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project template. | [optional] 
**description** | **str** | Free-form textual information associated with the project template | [optional] 
**html_description** | **str** | The description of the project template with formatting as HTML. | [optional] 
**public** | **bool** | True if the project template is public to its team. | [optional] 
**owner** | [**ProjectTemplateBaseAllOfOwner**](ProjectTemplateBaseAllOfOwner.md) |  | [optional] 
**team** | [**TeamCompact**](TeamCompact.md) |  | [optional] 
**requested_dates** | [**List[DateVariableCompact]**](DateVariableCompact.md) | Array of date variables in this project template. Calendar dates must be provided for these variables when instantiating a project. | [optional] [readonly] 
**color** | **str** | Color of the project template. | [optional] 
**requested_roles** | [**List[TemplateRole]**](TemplateRole.md) | Array of template roles in this project template. User Ids can be provided for these variables when instantiating a project to assign template tasks to the user. | [optional] 

## Example

```python
from asana_asyncio.models.project_template_response import ProjectTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateResponse from a JSON string
project_template_response_instance = ProjectTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplateResponse.to_json())

# convert the object into a dict
project_template_response_dict = project_template_response_instance.to_dict()
# create an instance of ProjectTemplateResponse from a dict
project_template_response_from_dict = ProjectTemplateResponse.from_dict(project_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


