# SectionTaskInsertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | **str** | The task to add to this section. | 
**insert_before** | **str** | An existing task within this section before which the added task should be inserted. Cannot be provided together with insert_after. | [optional] 
**insert_after** | **str** | An existing task within this section after which the added task should be inserted. Cannot be provided together with insert_before. | [optional] 

## Example

```python
from asana_asyncio.models.section_task_insert_request import SectionTaskInsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SectionTaskInsertRequest from a JSON string
section_task_insert_request_instance = SectionTaskInsertRequest.from_json(json)
# print the JSON string representation of the object
print(SectionTaskInsertRequest.to_json())

# convert the object into a dict
section_task_insert_request_dict = section_task_insert_request_instance.to_dict()
# create an instance of SectionTaskInsertRequest from a dict
section_task_insert_request_from_dict = SectionTaskInsertRequest.from_dict(section_task_insert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


