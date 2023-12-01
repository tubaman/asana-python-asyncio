# StatusUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**title** | **str** | The title of the status update. | [optional] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The &#x60;resource_subtype&#x60;s for &#x60;status&#x60; objects represent the type of their parent. | [optional] [readonly] 
**text** | **str** | The text content of the status update. | 
**html_text** | **str** | [Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML. | [optional] 
**status_type** | **str** | The type associated with the status update. This represents the current state of the object this object is on. | 
**parent** | **object** |  | 

## Example

```python
from asana_asyncio.models.status_update_request import StatusUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StatusUpdateRequest from a JSON string
status_update_request_instance = StatusUpdateRequest.from_json(json)
# print the JSON string representation of the object
print StatusUpdateRequest.to_json()

# convert the object into a dict
status_update_request_dict = status_update_request_instance.to_dict()
# create an instance of StatusUpdateRequest from a dict
status_update_request_form_dict = status_update_request.from_dict(status_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

