# PortfolioMembershipCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**portfolio** | [**PortfolioCompact**](PortfolioCompact.md) |  | [optional] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.portfolio_membership_compact import PortfolioMembershipCompact

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioMembershipCompact from a JSON string
portfolio_membership_compact_instance = PortfolioMembershipCompact.from_json(json)
# print the JSON string representation of the object
print PortfolioMembershipCompact.to_json()

# convert the object into a dict
portfolio_membership_compact_dict = portfolio_membership_compact_instance.to_dict()
# create an instance of PortfolioMembershipCompact from a dict
portfolio_membership_compact_form_dict = portfolio_membership_compact.from_dict(portfolio_membership_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


