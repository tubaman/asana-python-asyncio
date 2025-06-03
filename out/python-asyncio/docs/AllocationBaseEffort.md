# AllocationBaseEffort

The amount of time associated with the allocation, represented as a percentage or number of hours

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The units used for tracking effort on an allocation, either \&quot;hours\&quot; or \&quot;percent\&quot;. | [optional] 
**value** | **float** | The numeric effort value on the allocation. | [optional] 

## Example

```python
from asana_asyncio.models.allocation_base_effort import AllocationBaseEffort

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationBaseEffort from a JSON string
allocation_base_effort_instance = AllocationBaseEffort.from_json(json)
# print the JSON string representation of the object
print(AllocationBaseEffort.to_json())

# convert the object into a dict
allocation_base_effort_dict = allocation_base_effort_instance.to_dict()
# create an instance of AllocationBaseEffort from a dict
allocation_base_effort_from_dict = AllocationBaseEffort.from_dict(allocation_base_effort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


