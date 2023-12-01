# Preview

A collection of rich text that will be displayed as a preview to another app.  This is read-only except for a small group of whitelisted apps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback** | **str** | Some fallback text to display if unable to display the full preview. | [optional] 
**footer** | **str** | Text to display in the footer. | [optional] 
**header** | **str** | Text to display in the header. | [optional] 
**header_link** | **str** | Where the header will link to. | [optional] 
**html_text** | **str** | HTML formatted text for the body of the preview. | [optional] 
**text** | **str** | Text for the body of the preview. | [optional] 
**title** | **str** | Text to display as the title. | [optional] 
**title_link** | **str** | Where to title will link to. | [optional] 

## Example

```python
from asana_asyncio.models.preview import Preview

# TODO update the JSON string below
json = "{}"
# create an instance of Preview from a JSON string
preview_instance = Preview.from_json(json)
# print the JSON string representation of the object
print Preview.to_json()

# convert the object into a dict
preview_dict = preview_instance.to_dict()
# create an instance of Preview from a dict
preview_form_dict = preview.from_dict(preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


