# SectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the section (i.e. the text displayed as the section header). | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**project** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**projects** | [**List[ProjectCompact]**](ProjectCompact.md) | *Deprecated - please use project instead* | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.section_response import SectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SectionResponse from a JSON string
section_response_instance = SectionResponse.from_json(json)
# print the JSON string representation of the object
print(SectionResponse.to_json())

# convert the object into a dict
section_response_dict = section_response_instance.to_dict()
# create an instance of SectionResponse from a dict
section_response_from_dict = SectionResponse.from_dict(section_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


