# ProjectSaveAsTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProjectSaveAsTemplateRequest**](ProjectSaveAsTemplateRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.project_save_as_template_request import ProjectSaveAsTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSaveAsTemplateRequest from a JSON string
project_save_as_template_request_instance = ProjectSaveAsTemplateRequest.from_json(json)
# print the JSON string representation of the object
print ProjectSaveAsTemplateRequest.to_json()

# convert the object into a dict
project_save_as_template_request_dict = project_save_as_template_request_instance.to_dict()
# create an instance of ProjectSaveAsTemplateRequest from a dict
project_save_as_template_request_form_dict = project_save_as_template_request.from_dict(project_save_as_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


