# RemoveMembersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **str** | An array of strings identifying users. These can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 

## Example

```python
from asana_asyncio.models.remove_members_request import RemoveMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMembersRequest from a JSON string
remove_members_request_instance = RemoveMembersRequest.from_json(json)
# print the JSON string representation of the object
print RemoveMembersRequest.to_json()

# convert the object into a dict
remove_members_request_dict = remove_members_request_instance.to_dict()
# create an instance of RemoveMembersRequest from a dict
remove_members_request_form_dict = remove_members_request.from_dict(remove_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


