# DateVariableCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the date field in the project template. A value of &#x60;1&#x60; refers to the project start date, while &#x60;2&#x60; refers to the project due date. | [optional] [readonly] 
**name** | **str** | The name of the date variable. | [optional] [readonly] 
**description** | **str** | The description of what the date variable is used for when instantiating a project. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.date_variable_compact import DateVariableCompact

# TODO update the JSON string below
json = "{}"
# create an instance of DateVariableCompact from a JSON string
date_variable_compact_instance = DateVariableCompact.from_json(json)
# print the JSON string representation of the object
print(DateVariableCompact.to_json())

# convert the object into a dict
date_variable_compact_dict = date_variable_compact_instance.to_dict()
# create an instance of DateVariableCompact from a dict
date_variable_compact_from_dict = DateVariableCompact.from_dict(date_variable_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


