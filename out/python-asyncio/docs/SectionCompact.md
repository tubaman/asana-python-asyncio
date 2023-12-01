# SectionCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the section (i.e. the text displayed as the section header). | [optional] 

## Example

```python
from asana_asyncio.models.section_compact import SectionCompact

# TODO update the JSON string below
json = "{}"
# create an instance of SectionCompact from a JSON string
section_compact_instance = SectionCompact.from_json(json)
# print the JSON string representation of the object
print SectionCompact.to_json()

# convert the object into a dict
section_compact_dict = section_compact_instance.to_dict()
# create an instance of SectionCompact from a dict
section_compact_form_dict = section_compact.from_dict(section_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


