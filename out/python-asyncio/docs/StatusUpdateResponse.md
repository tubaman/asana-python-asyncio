# StatusUpdateResponse


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
**author** | [**UserCompact**](UserCompact.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**created_by** | [**UserCompact**](UserCompact.md) |  | [optional] 
**hearted** | **bool** | *Deprecated - please use liked instead* True if the status is hearted by the authorized user, false if not. | [optional] [readonly] 
**hearts** | [**List[Like]**](Like.md) | *Deprecated - please use likes instead* Array of likes for users who have hearted this status. | [optional] [readonly] 
**liked** | **bool** | True if the status is liked by the authorized user, false if not. | [optional] 
**likes** | [**List[Like]**](Like.md) | Array of likes for users who have liked this status. | [optional] [readonly] 
**modified_at** | **datetime** | The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the status.* | [optional] [readonly] 
**num_hearts** | **int** | *Deprecated - please use likes instead* The number of users who have hearted this status. | [optional] [readonly] 
**num_likes** | **int** | The number of users who have liked this status. | [optional] [readonly] 
**parent** | [**StatusUpdateResponseAllOfParent**](StatusUpdateResponseAllOfParent.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.status_update_response import StatusUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusUpdateResponse from a JSON string
status_update_response_instance = StatusUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(StatusUpdateResponse.to_json())

# convert the object into a dict
status_update_response_dict = status_update_response_instance.to_dict()
# create an instance of StatusUpdateResponse from a dict
status_update_response_from_dict = StatusUpdateResponse.from_dict(status_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


