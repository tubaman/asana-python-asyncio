# ProjectResponseAllOfProjectBrief


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.project_response_all_of_project_brief import ProjectResponseAllOfProjectBrief

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponseAllOfProjectBrief from a JSON string
project_response_all_of_project_brief_instance = ProjectResponseAllOfProjectBrief.from_json(json)
# print the JSON string representation of the object
print ProjectResponseAllOfProjectBrief.to_json()

# convert the object into a dict
project_response_all_of_project_brief_dict = project_response_all_of_project_brief_instance.to_dict()
# create an instance of ProjectResponseAllOfProjectBrief from a dict
project_response_all_of_project_brief_form_dict = project_response_all_of_project_brief.from_dict(project_response_all_of_project_brief_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


