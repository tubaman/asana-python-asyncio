# UpdateSectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SectionRequest**](SectionRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_section_request import UpdateSectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSectionRequest from a JSON string
update_section_request_instance = UpdateSectionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSectionRequest.to_json())

# convert the object into a dict
update_section_request_dict = update_section_request_instance.to_dict()
# create an instance of UpdateSectionRequest from a dict
update_section_request_from_dict = UpdateSectionRequest.from_dict(update_section_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


