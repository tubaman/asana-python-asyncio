# ProjectStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**title** | **str** | The title of the project status update. | [optional] 
**text** | **str** | The text content of the status update. | [optional] 
**html_text** | **str** | [Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML. | [optional] 
**color** | **str** | The color associated with the status update. | [optional] 
**author** | [**UserCompact**](UserCompact.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**created_by** | [**UserCompact**](UserCompact.md) |  | [optional] 
**modified_at** | **datetime** | The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the project status.* | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.project_status_response import ProjectStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatusResponse from a JSON string
project_status_response_instance = ProjectStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectStatusResponse.to_json())

# convert the object into a dict
project_status_response_dict = project_status_response_instance.to_dict()
# create an instance of ProjectStatusResponse from a dict
project_status_response_from_dict = ProjectStatusResponse.from_dict(project_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


