# RemoveMembersForPortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RemoveMembersRequest**](RemoveMembersRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_members_for_portfolio_request import RemoveMembersForPortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMembersForPortfolioRequest from a JSON string
remove_members_for_portfolio_request_instance = RemoveMembersForPortfolioRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveMembersForPortfolioRequest.to_json())

# convert the object into a dict
remove_members_for_portfolio_request_dict = remove_members_for_portfolio_request_instance.to_dict()
# create an instance of RemoveMembersForPortfolioRequest from a dict
remove_members_for_portfolio_request_from_dict = RemoveMembersForPortfolioRequest.from_dict(remove_members_for_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


