# ProjectBriefResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**title** | **str** | The title of the project brief. | [optional] 
**html_text** | **str** | HTML formatted text for the project brief. | [optional] 
**text** | **str** | [Opt In](/docs/inputoutput-options). The plain text of the project brief. | [optional] 
**permalink_url** | **str** | A url that points directly to the object within Asana. | [optional] [readonly] 
**project** | [**ProjectBriefResponseAllOfProject**](ProjectBriefResponseAllOfProject.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.project_brief_response import ProjectBriefResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBriefResponse from a JSON string
project_brief_response_instance = ProjectBriefResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectBriefResponse.to_json())

# convert the object into a dict
project_brief_response_dict = project_brief_response_instance.to_dict()
# create an instance of ProjectBriefResponse from a dict
project_brief_response_from_dict = ProjectBriefResponse.from_dict(project_brief_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


