# EventResponseParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the object. | [optional] 

## Example

```python
from asana_asyncio.models.event_response_parent import EventResponseParent

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponseParent from a JSON string
event_response_parent_instance = EventResponseParent.from_json(json)
# print the JSON string representation of the object
print EventResponseParent.to_json()

# convert the object into a dict
event_response_parent_dict = event_response_parent_instance.to_dict()
# create an instance of EventResponseParent from a dict
event_response_parent_form_dict = event_response_parent.from_dict(event_response_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


