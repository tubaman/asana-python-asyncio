# DeprecatedPortfolioMembershipCompact

This object determines if a user is a member of a portfolio.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**portfolio** | [**PortfolioCompact**](PortfolioCompact.md) |  | [optional] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 
**access_level** | **str** | Whether the member has admin, editor, or viewer access to the portfolio. Portfolios do not support commenter access yet. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.deprecated_portfolio_membership_compact import DeprecatedPortfolioMembershipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedPortfolioMembershipCompact from a JSON string
deprecated_portfolio_membership_compact_instance = DeprecatedPortfolioMembershipCompact.from_json(json)
# print the JSON string representation of the object
print(DeprecatedPortfolioMembershipCompact.to_json())

# convert the object into a dict
deprecated_portfolio_membership_compact_dict = deprecated_portfolio_membership_compact_instance.to_dict()
# create an instance of DeprecatedPortfolioMembershipCompact from a dict
deprecated_portfolio_membership_compact_from_dict = DeprecatedPortfolioMembershipCompact.from_dict(deprecated_portfolio_membership_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


