# TaskBaseAllOfExternal

*OAuth Required*. *Conditional*. This field is returned only if external values are set or included by using [Opt In] (/docs/inputoutput-options). The external field allows you to store app-specific metadata on tasks, including a gid that can be used to retrieve tasks and a data blob that can store app-specific character strings. Note that you will need to authenticate with Oauth to access or modify this data. Once an external gid is set, you can use the notation `external:custom_gid` to reference your object anywhere in the API where you may use the original object gid. See the page on Custom External Data for more details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from asana_asyncio.models.task_base_all_of_external import TaskBaseAllOfExternal

# TODO update the JSON string below
json = "{}"
# create an instance of TaskBaseAllOfExternal from a JSON string
task_base_all_of_external_instance = TaskBaseAllOfExternal.from_json(json)
# print the JSON string representation of the object
print TaskBaseAllOfExternal.to_json()

# convert the object into a dict
task_base_all_of_external_dict = task_base_all_of_external_instance.to_dict()
# create an instance of TaskBaseAllOfExternal from a dict
task_base_all_of_external_form_dict = task_base_all_of_external.from_dict(task_base_all_of_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


