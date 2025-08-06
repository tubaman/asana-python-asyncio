# AddUserForWorkspace200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserBaseResponse**](UserBaseResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_user_for_workspace200_response import AddUserForWorkspace200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserForWorkspace200Response from a JSON string
add_user_for_workspace200_response_instance = AddUserForWorkspace200Response.from_json(json)
# print the JSON string representation of the object
print(AddUserForWorkspace200Response.to_json())

# convert the object into a dict
add_user_for_workspace200_response_dict = add_user_for_workspace200_response_instance.to_dict()
# create an instance of AddUserForWorkspace200Response from a dict
add_user_for_workspace200_response_from_dict = AddUserForWorkspace200Response.from_dict(add_user_for_workspace200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


