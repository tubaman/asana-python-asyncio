# SectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The text to be displayed as the section name. This cannot be an empty string. | 
**insert_before** | **str** | An existing section within this project before which the added section should be inserted. Cannot be provided together with insert_after. | [optional] 
**insert_after** | **str** | An existing section within this project after which the added section should be inserted. Cannot be provided together with insert_before. | [optional] 

## Example

```python
from asana_asyncio.models.section_request import SectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SectionRequest from a JSON string
section_request_instance = SectionRequest.from_json(json)
# print the JSON string representation of the object
print(SectionRequest.to_json())

# convert the object into a dict
section_request_dict = section_request_instance.to_dict()
# create an instance of SectionRequest from a dict
section_request_from_dict = SectionRequest.from_dict(section_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


