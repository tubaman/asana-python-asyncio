# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message providing more detail about the error that occurred, if available. | [optional] [readonly] 
**help** | **str** | Additional information directing developers to resources on how to address and fix the problem, if available. | [optional] [readonly] 
**phrase** | **str** | *500 errors only*. A unique error phrase which can be used when contacting developer support to help identify the exact occurrence of the problem in Asana&#39;s logs. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


