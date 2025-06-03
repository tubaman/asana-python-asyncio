# CustomTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the custom type. | [optional] 
**status_options** | [**List[CustomTypeStatusOptionResponse]**](CustomTypeStatusOptionResponse.md) | The available options for the custom type. | [optional] 

## Example

```python
from asana_asyncio.models.custom_type_response import CustomTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTypeResponse from a JSON string
custom_type_response_instance = CustomTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CustomTypeResponse.to_json())

# convert the object into a dict
custom_type_response_dict = custom_type_response_instance.to_dict()
# create an instance of CustomTypeResponse from a dict
custom_type_response_from_dict = CustomTypeResponse.from_dict(custom_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


