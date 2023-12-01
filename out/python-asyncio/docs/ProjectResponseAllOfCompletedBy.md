# ProjectResponseAllOfCompletedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.project_response_all_of_completed_by import ProjectResponseAllOfCompletedBy

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponseAllOfCompletedBy from a JSON string
project_response_all_of_completed_by_instance = ProjectResponseAllOfCompletedBy.from_json(json)
# print the JSON string representation of the object
print ProjectResponseAllOfCompletedBy.to_json()

# convert the object into a dict
project_response_all_of_completed_by_dict = project_response_all_of_completed_by_instance.to_dict()
# create an instance of ProjectResponseAllOfCompletedBy from a dict
project_response_all_of_completed_by_form_dict = project_response_all_of_completed_by.from_dict(project_response_all_of_completed_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


