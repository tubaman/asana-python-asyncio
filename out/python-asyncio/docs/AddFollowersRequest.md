# AddFollowersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskAddFollowersRequest**](TaskAddFollowersRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_followers_request import AddFollowersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddFollowersRequest from a JSON string
add_followers_request_instance = AddFollowersRequest.from_json(json)
# print the JSON string representation of the object
print AddFollowersRequest.to_json()

# convert the object into a dict
add_followers_request_dict = add_followers_request_instance.to_dict()
# create an instance of AddFollowersRequest from a dict
add_followers_request_form_dict = add_followers_request.from_dict(add_followers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


