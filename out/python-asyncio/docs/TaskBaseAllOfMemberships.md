# TaskBaseAllOfMemberships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**section** | [**SectionCompact**](SectionCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.task_base_all_of_memberships import TaskBaseAllOfMemberships

# TODO update the JSON string below
json = "{}"
# create an instance of TaskBaseAllOfMemberships from a JSON string
task_base_all_of_memberships_instance = TaskBaseAllOfMemberships.from_json(json)
# print the JSON string representation of the object
print TaskBaseAllOfMemberships.to_json()

# convert the object into a dict
task_base_all_of_memberships_dict = task_base_all_of_memberships_instance.to_dict()
# create an instance of TaskBaseAllOfMemberships from a dict
task_base_all_of_memberships_form_dict = task_base_all_of_memberships.from_dict(task_base_all_of_memberships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


