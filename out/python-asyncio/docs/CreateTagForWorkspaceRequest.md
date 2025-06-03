# CreateTagForWorkspaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TagCreateTagForWorkspaceRequest**](TagCreateTagForWorkspaceRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_tag_for_workspace_request import CreateTagForWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagForWorkspaceRequest from a JSON string
create_tag_for_workspace_request_instance = CreateTagForWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTagForWorkspaceRequest.to_json())

# convert the object into a dict
create_tag_for_workspace_request_dict = create_tag_for_workspace_request_instance.to_dict()
# create an instance of CreateTagForWorkspaceRequest from a dict
create_tag_for_workspace_request_from_dict = CreateTagForWorkspaceRequest.from_dict(create_tag_for_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


