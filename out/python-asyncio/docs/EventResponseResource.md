# EventResponseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the object. | [optional] 

## Example

```python
from asana_asyncio.models.event_response_resource import EventResponseResource

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponseResource from a JSON string
event_response_resource_instance = EventResponseResource.from_json(json)
# print the JSON string representation of the object
print EventResponseResource.to_json()

# convert the object into a dict
event_response_resource_dict = event_response_resource_instance.to_dict()
# create an instance of EventResponseResource from a dict
event_response_resource_form_dict = event_response_resource.from_dict(event_response_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


