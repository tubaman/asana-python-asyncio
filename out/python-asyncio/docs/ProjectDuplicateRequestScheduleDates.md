# ProjectDuplicateRequestScheduleDates

A dictionary of options to auto-shift dates. `task_dates` must be included to use this option. Requires either `start_on` or `due_on`, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_skip_weekends** | **bool** | Determines if the auto-shifted dates should skip weekends. | 
**due_on** | **str** | Sets the last due date in the duplicated project to the given date. The rest of the due dates will be offset by the same amount as the due dates in the original project. | [optional] 
**start_on** | **str** | Sets the first start date in the duplicated project to the given date. The rest of the start dates will be offset by the same amount as the start dates in the original project. | [optional] 

## Example

```python
from asana_asyncio.models.project_duplicate_request_schedule_dates import ProjectDuplicateRequestScheduleDates

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDuplicateRequestScheduleDates from a JSON string
project_duplicate_request_schedule_dates_instance = ProjectDuplicateRequestScheduleDates.from_json(json)
# print the JSON string representation of the object
print ProjectDuplicateRequestScheduleDates.to_json()

# convert the object into a dict
project_duplicate_request_schedule_dates_dict = project_duplicate_request_schedule_dates_instance.to_dict()
# create an instance of ProjectDuplicateRequestScheduleDates from a dict
project_duplicate_request_schedule_dates_form_dict = project_duplicate_request_schedule_dates.from_dict(project_duplicate_request_schedule_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


