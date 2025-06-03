# AddTaskForSectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SectionTaskInsertRequest**](SectionTaskInsertRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_task_for_section_request import AddTaskForSectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTaskForSectionRequest from a JSON string
add_task_for_section_request_instance = AddTaskForSectionRequest.from_json(json)
# print the JSON string representation of the object
print(AddTaskForSectionRequest.to_json())

# convert the object into a dict
add_task_for_section_request_dict = add_task_for_section_request_instance.to_dict()
# create an instance of AddTaskForSectionRequest from a dict
add_task_for_section_request_from_dict = AddTaskForSectionRequest.from_dict(add_task_for_section_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


