# CreateProjectStatusForProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProjectStatusBase**](ProjectStatusBase.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_project_status_for_project_request import CreateProjectStatusForProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectStatusForProjectRequest from a JSON string
create_project_status_for_project_request_instance = CreateProjectStatusForProjectRequest.from_json(json)
# print the JSON string representation of the object
print CreateProjectStatusForProjectRequest.to_json()

# convert the object into a dict
create_project_status_for_project_request_dict = create_project_status_for_project_request_instance.to_dict()
# create an instance of CreateProjectStatusForProjectRequest from a dict
create_project_status_for_project_request_form_dict = create_project_status_for_project_request.from_dict(create_project_status_for_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


