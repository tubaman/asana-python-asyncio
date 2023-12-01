# CustomFieldResponseAllOfCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | *Read-only except when same user as requester*. The user’s name. | [optional] 

## Example

```python
from asana_asyncio.models.custom_field_response_all_of_created_by import CustomFieldResponseAllOfCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldResponseAllOfCreatedBy from a JSON string
custom_field_response_all_of_created_by_instance = CustomFieldResponseAllOfCreatedBy.from_json(json)
# print the JSON string representation of the object
print CustomFieldResponseAllOfCreatedBy.to_json()

# convert the object into a dict
custom_field_response_all_of_created_by_dict = custom_field_response_all_of_created_by_instance.to_dict()
# create an instance of CustomFieldResponseAllOfCreatedBy from a dict
custom_field_response_all_of_created_by_form_dict = custom_field_response_all_of_created_by.from_dict(custom_field_response_all_of_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


