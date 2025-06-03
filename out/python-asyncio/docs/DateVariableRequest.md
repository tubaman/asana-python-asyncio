# DateVariableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the date field in the project template. A value of &#x60;1&#x60; refers to the project start date, while &#x60;2&#x60; refers to the project due date. | [optional] 
**value** | **datetime** | The date with which the date variable should be replaced when instantiating a project. This takes a date with &#x60;YYYY-MM-DD&#x60; format. | [optional] 

## Example

```python
from asana_asyncio.models.date_variable_request import DateVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DateVariableRequest from a JSON string
date_variable_request_instance = DateVariableRequest.from_json(json)
# print the JSON string representation of the object
print(DateVariableRequest.to_json())

# convert the object into a dict
date_variable_request_dict = date_variable_request_instance.to_dict()
# create an instance of DateVariableRequest from a dict
date_variable_request_from_dict = DateVariableRequest.from_dict(date_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


