# GetPortfolioMembership200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeprecatedPortfolioMembershipCompact**](DeprecatedPortfolioMembershipCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_portfolio_membership200_response import GetPortfolioMembership200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioMembership200Response from a JSON string
get_portfolio_membership200_response_instance = GetPortfolioMembership200Response.from_json(json)
# print the JSON string representation of the object
print(GetPortfolioMembership200Response.to_json())

# convert the object into a dict
get_portfolio_membership200_response_dict = get_portfolio_membership200_response_instance.to_dict()
# create an instance of GetPortfolioMembership200Response from a dict
get_portfolio_membership200_response_from_dict = GetPortfolioMembership200Response.from_dict(get_portfolio_membership200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


