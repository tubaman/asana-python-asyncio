# InsertSectionForProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProjectSectionInsertRequest**](ProjectSectionInsertRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.insert_section_for_project_request import InsertSectionForProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsertSectionForProjectRequest from a JSON string
insert_section_for_project_request_instance = InsertSectionForProjectRequest.from_json(json)
# print the JSON string representation of the object
print(InsertSectionForProjectRequest.to_json())

# convert the object into a dict
insert_section_for_project_request_dict = insert_section_for_project_request_instance.to_dict()
# create an instance of InsertSectionForProjectRequest from a dict
insert_section_for_project_request_from_dict = InsertSectionForProjectRequest.from_dict(insert_section_for_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


