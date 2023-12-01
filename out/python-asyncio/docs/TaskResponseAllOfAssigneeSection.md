# TaskResponseAllOfAssigneeSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the section (i.e. the text displayed as the section header). | [optional] 

## Example

```python
from asana_asyncio.models.task_response_all_of_assignee_section import TaskResponseAllOfAssigneeSection

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponseAllOfAssigneeSection from a JSON string
task_response_all_of_assignee_section_instance = TaskResponseAllOfAssigneeSection.from_json(json)
# print the JSON string representation of the object
print TaskResponseAllOfAssigneeSection.to_json()

# convert the object into a dict
task_response_all_of_assignee_section_dict = task_response_all_of_assignee_section_instance.to_dict()
# create an instance of TaskResponseAllOfAssigneeSection from a dict
task_response_all_of_assignee_section_form_dict = task_response_all_of_assignee_section.from_dict(task_response_all_of_assignee_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


