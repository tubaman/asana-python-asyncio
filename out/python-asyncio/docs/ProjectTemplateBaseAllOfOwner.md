# ProjectTemplateBaseAllOfOwner

The current owner of the project template, may be null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.project_template_base_all_of_owner import ProjectTemplateBaseAllOfOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateBaseAllOfOwner from a JSON string
project_template_base_all_of_owner_instance = ProjectTemplateBaseAllOfOwner.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateBaseAllOfOwner.to_json()

# convert the object into a dict
project_template_base_all_of_owner_dict = project_template_base_all_of_owner_instance.to_dict()
# create an instance of ProjectTemplateBaseAllOfOwner from a dict
project_template_base_all_of_owner_form_dict = project_template_base_all_of_owner.from_dict(project_template_base_all_of_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


