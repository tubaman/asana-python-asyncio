# CreateMembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateMembershipRequest**](CreateMembershipRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_membership_request import CreateMembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMembershipRequest from a JSON string
create_membership_request_instance = CreateMembershipRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMembershipRequest.to_json())

# convert the object into a dict
create_membership_request_dict = create_membership_request_instance.to_dict()
# create an instance of CreateMembershipRequest from a dict
create_membership_request_from_dict = CreateMembershipRequest.from_dict(create_membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


