# UpdateProjectBriefRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProjectBriefRequest**](ProjectBriefRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.update_project_brief_request import UpdateProjectBriefRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectBriefRequest from a JSON string
update_project_brief_request_instance = UpdateProjectBriefRequest.from_json(json)
# print the JSON string representation of the object
print UpdateProjectBriefRequest.to_json()

# convert the object into a dict
update_project_brief_request_dict = update_project_brief_request_instance.to_dict()
# create an instance of UpdateProjectBriefRequest from a dict
update_project_brief_request_form_dict = update_project_brief_request.from_dict(update_project_brief_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


