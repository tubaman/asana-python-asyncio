# ProjectResponseAllOfCreatedFromTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project template. | [optional] 

## Example

```python
from asana_asyncio.models.project_response_all_of_created_from_template import ProjectResponseAllOfCreatedFromTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponseAllOfCreatedFromTemplate from a JSON string
project_response_all_of_created_from_template_instance = ProjectResponseAllOfCreatedFromTemplate.from_json(json)
# print the JSON string representation of the object
print(ProjectResponseAllOfCreatedFromTemplate.to_json())

# convert the object into a dict
project_response_all_of_created_from_template_dict = project_response_all_of_created_from_template_instance.to_dict()
# create an instance of ProjectResponseAllOfCreatedFromTemplate from a dict
project_response_all_of_created_from_template_from_dict = ProjectResponseAllOfCreatedFromTemplate.from_dict(project_response_all_of_created_from_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


