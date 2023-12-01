# DuplicateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProjectDuplicateRequest**](ProjectDuplicateRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.duplicate_project_request import DuplicateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateProjectRequest from a JSON string
duplicate_project_request_instance = DuplicateProjectRequest.from_json(json)
# print the JSON string representation of the object
print DuplicateProjectRequest.to_json()

# convert the object into a dict
duplicate_project_request_dict = duplicate_project_request_instance.to_dict()
# create an instance of DuplicateProjectRequest from a dict
duplicate_project_request_form_dict = duplicate_project_request.from_dict(duplicate_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


