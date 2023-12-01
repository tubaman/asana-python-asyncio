# AddMembersForPortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AddMembersRequest**](AddMembersRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_members_for_portfolio_request import AddMembersForPortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddMembersForPortfolioRequest from a JSON string
add_members_for_portfolio_request_instance = AddMembersForPortfolioRequest.from_json(json)
# print the JSON string representation of the object
print AddMembersForPortfolioRequest.to_json()

# convert the object into a dict
add_members_for_portfolio_request_dict = add_members_for_portfolio_request_instance.to_dict()
# create an instance of AddMembersForPortfolioRequest from a dict
add_members_for_portfolio_request_form_dict = add_members_for_portfolio_request.from_dict(add_members_for_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


