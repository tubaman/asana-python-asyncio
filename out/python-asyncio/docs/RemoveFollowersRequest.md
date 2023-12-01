# RemoveFollowersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**followers** | **str** | An array of strings identifying users. These can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 

## Example

```python
from asana_asyncio.models.remove_followers_request import RemoveFollowersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFollowersRequest from a JSON string
remove_followers_request_instance = RemoveFollowersRequest.from_json(json)
# print the JSON string representation of the object
print RemoveFollowersRequest.to_json()

# convert the object into a dict
remove_followers_request_dict = remove_followers_request_instance.to_dict()
# create an instance of RemoveFollowersRequest from a dict
remove_followers_request_form_dict = remove_followers_request.from_dict(remove_followers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


