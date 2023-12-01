# ProjectSectionInsertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | **str** | The section to reorder. | 
**before_section** | **str** | Insert the given section immediately before the section specified by this parameter. | [optional] 
**after_section** | **str** | Insert the given section immediately after the section specified by this parameter. | [optional] 

## Example

```python
from asana_asyncio.models.project_section_insert_request import ProjectSectionInsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSectionInsertRequest from a JSON string
project_section_insert_request_instance = ProjectSectionInsertRequest.from_json(json)
# print the JSON string representation of the object
print ProjectSectionInsertRequest.to_json()

# convert the object into a dict
project_section_insert_request_dict = project_section_insert_request_instance.to_dict()
# create an instance of ProjectSectionInsertRequest from a dict
project_section_insert_request_form_dict = project_section_insert_request.from_dict(project_section_insert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


