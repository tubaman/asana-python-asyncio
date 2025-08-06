# InstantiateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProjectTemplateInstantiateProjectRequest**](ProjectTemplateInstantiateProjectRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.instantiate_project_request import InstantiateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiateProjectRequest from a JSON string
instantiate_project_request_instance = InstantiateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(InstantiateProjectRequest.to_json())

# convert the object into a dict
instantiate_project_request_dict = instantiate_project_request_instance.to_dict()
# create an instance of InstantiateProjectRequest from a dict
instantiate_project_request_from_dict = InstantiateProjectRequest.from_dict(instantiate_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


