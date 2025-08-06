# AllocationResponseAllOfAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of allocation resource. | [optional] 

## Example

```python
from asana_asyncio.models.allocation_response_all_of_assignee import AllocationResponseAllOfAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationResponseAllOfAssignee from a JSON string
allocation_response_all_of_assignee_instance = AllocationResponseAllOfAssignee.from_json(json)
# print the JSON string representation of the object
print(AllocationResponseAllOfAssignee.to_json())

# convert the object into a dict
allocation_response_all_of_assignee_dict = allocation_response_all_of_assignee_instance.to_dict()
# create an instance of AllocationResponseAllOfAssignee from a dict
allocation_response_all_of_assignee_from_dict = AllocationResponseAllOfAssignee.from_dict(allocation_response_all_of_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


