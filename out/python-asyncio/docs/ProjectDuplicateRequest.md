# ProjectDuplicateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new project. | 
**team** | **str** | Sets the team of the new project. If team is not defined, the new project will be in the same team as the the original project. | [optional] 
**include** | **str** | A comma-separated list of elements that will be duplicated to the new project. Tasks are always included. ##### Fields - forms - members - notes - task_assignee - task_attachments - task_dates - task_dependencies - task_followers - task_notes - task_projects - task_subtasks - task_tags | [optional] 
**schedule_dates** | [**ProjectDuplicateRequestScheduleDates**](ProjectDuplicateRequestScheduleDates.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.project_duplicate_request import ProjectDuplicateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDuplicateRequest from a JSON string
project_duplicate_request_instance = ProjectDuplicateRequest.from_json(json)
# print the JSON string representation of the object
print ProjectDuplicateRequest.to_json()

# convert the object into a dict
project_duplicate_request_dict = project_duplicate_request_instance.to_dict()
# create an instance of ProjectDuplicateRequest from a dict
project_duplicate_request_form_dict = project_duplicate_request.from_dict(project_duplicate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


