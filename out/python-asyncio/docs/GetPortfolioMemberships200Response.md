# GetPortfolioMemberships200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PortfolioMembershipCompact]**](PortfolioMembershipCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_portfolio_memberships200_response import GetPortfolioMemberships200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolioMemberships200Response from a JSON string
get_portfolio_memberships200_response_instance = GetPortfolioMemberships200Response.from_json(json)
# print the JSON string representation of the object
print GetPortfolioMemberships200Response.to_json()

# convert the object into a dict
get_portfolio_memberships200_response_dict = get_portfolio_memberships200_response_instance.to_dict()
# create an instance of GetPortfolioMemberships200Response from a dict
get_portfolio_memberships200_response_form_dict = get_portfolio_memberships200_response.from_dict(get_portfolio_memberships200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


