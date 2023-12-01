# ProjectResponseAllOfOwner

The current owner of the project, may be null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.project_response_all_of_owner import ProjectResponseAllOfOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponseAllOfOwner from a JSON string
project_response_all_of_owner_instance = ProjectResponseAllOfOwner.from_json(json)
# print the JSON string representation of the object
print ProjectResponseAllOfOwner.to_json()

# convert the object into a dict
project_response_all_of_owner_dict = project_response_all_of_owner_instance.to_dict()
# create an instance of ProjectResponseAllOfOwner from a dict
project_response_all_of_owner_form_dict = project_response_all_of_owner.from_dict(project_response_all_of_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


