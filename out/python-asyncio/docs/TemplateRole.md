# TemplateRole

A generic Asana Resource, containing a globally unique identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the template role. | [optional] 

## Example

```python
from asana_asyncio.models.template_role import TemplateRole

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRole from a JSON string
template_role_instance = TemplateRole.from_json(json)
# print the JSON string representation of the object
print(TemplateRole.to_json())

# convert the object into a dict
template_role_dict = template_role_instance.to_dict()
# create an instance of TemplateRole from a dict
template_role_from_dict = TemplateRole.from_dict(template_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


