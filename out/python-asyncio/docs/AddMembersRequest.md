# AddMembersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **str** | An array of strings identifying users. These can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 

## Example

```python
from asana_asyncio.models.add_members_request import AddMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddMembersRequest from a JSON string
add_members_request_instance = AddMembersRequest.from_json(json)
# print the JSON string representation of the object
print AddMembersRequest.to_json()

# convert the object into a dict
add_members_request_dict = add_members_request_instance.to_dict()
# create an instance of AddMembersRequest from a dict
add_members_request_form_dict = add_members_request.from_dict(add_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


