# ProjectBriefRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**title** | **str** | The title of the project brief. | [optional] 
**html_text** | **str** | HTML formatted text for the project brief. | [optional] 
**text** | **str** | The plain text of the project brief. When writing to a project brief, you can specify either &#x60;html_text&#x60; (preferred) or &#x60;text&#x60;, but not both. | [optional] 

## Example

```python
from asana_asyncio.models.project_brief_request import ProjectBriefRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBriefRequest from a JSON string
project_brief_request_instance = ProjectBriefRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectBriefRequest.to_json())

# convert the object into a dict
project_brief_request_dict = project_brief_request_instance.to_dict()
# create an instance of ProjectBriefRequest from a dict
project_brief_request_from_dict = ProjectBriefRequest.from_dict(project_brief_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


