# TaskAddFollowersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**followers** | **List[str]** | An array of strings identifying users. These can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 

## Example

```python
from asana_asyncio.models.task_add_followers_request import TaskAddFollowersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskAddFollowersRequest from a JSON string
task_add_followers_request_instance = TaskAddFollowersRequest.from_json(json)
# print the JSON string representation of the object
print TaskAddFollowersRequest.to_json()

# convert the object into a dict
task_add_followers_request_dict = task_add_followers_request_instance.to_dict()
# create an instance of TaskAddFollowersRequest from a dict
task_add_followers_request_form_dict = task_add_followers_request.from_dict(task_add_followers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


