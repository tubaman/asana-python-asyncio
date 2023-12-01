# WorkspaceMembershipResponseAllOfVacationDates

Contains keys `start_on` and `end_on` for the vacation dates for the user in this workspace. If `start_on` is null, the entire `vacation_dates` object will be null. If `end_on` is before today, the entire `vacation_dates` object will be null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_on** | **str** | The day on which the user&#39;s vacation in this workspace starts. This is a date with &#x60;YYYY-MM-DD&#x60; format. | [optional] 
**end_on** | **str** | The day on which the user&#39;s vacation in this workspace ends, or null if there is no end date. This is a date with &#x60;YYYY-MM-DD&#x60; format. | [optional] 

## Example

```python
from asana_asyncio.models.workspace_membership_response_all_of_vacation_dates import WorkspaceMembershipResponseAllOfVacationDates

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembershipResponseAllOfVacationDates from a JSON string
workspace_membership_response_all_of_vacation_dates_instance = WorkspaceMembershipResponseAllOfVacationDates.from_json(json)
# print the JSON string representation of the object
print WorkspaceMembershipResponseAllOfVacationDates.to_json()

# convert the object into a dict
workspace_membership_response_all_of_vacation_dates_dict = workspace_membership_response_all_of_vacation_dates_instance.to_dict()
# create an instance of WorkspaceMembershipResponseAllOfVacationDates from a dict
workspace_membership_response_all_of_vacation_dates_form_dict = workspace_membership_response_all_of_vacation_dates.from_dict(workspace_membership_response_all_of_vacation_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


