# CustomTypeStatusOptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the custom type status option. | [optional] 
**completion_state** | **str** | The completion state the custom type status option corresponds to, all custom types must have one ‘Incomplete’ and ‘Complete’ status option. | [optional] 
**enabled** | **bool** | Whether or not the custom type status option is a selectable value for the custom type. | [optional] 
**color** | **str** | The color associated with the custom type status option. Defaults to ‘none’. | [optional] 

## Example

```python
from asana_asyncio.models.custom_type_status_option_response import CustomTypeStatusOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTypeStatusOptionResponse from a JSON string
custom_type_status_option_response_instance = CustomTypeStatusOptionResponse.from_json(json)
# print the JSON string representation of the object
print(CustomTypeStatusOptionResponse.to_json())

# convert the object into a dict
custom_type_status_option_response_dict = custom_type_status_option_response_instance.to_dict()
# create an instance of CustomTypeStatusOptionResponse from a dict
custom_type_status_option_response_from_dict = CustomTypeStatusOptionResponse.from_dict(custom_type_status_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


