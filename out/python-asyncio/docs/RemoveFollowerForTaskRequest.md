# RemoveFollowerForTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskRemoveFollowersRequest**](TaskRemoveFollowersRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_follower_for_task_request import RemoveFollowerForTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFollowerForTaskRequest from a JSON string
remove_follower_for_task_request_instance = RemoveFollowerForTaskRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveFollowerForTaskRequest.to_json())

# convert the object into a dict
remove_follower_for_task_request_dict = remove_follower_for_task_request_instance.to_dict()
# create an instance of RemoveFollowerForTaskRequest from a dict
remove_follower_for_task_request_from_dict = RemoveFollowerForTaskRequest.from_dict(remove_follower_for_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


