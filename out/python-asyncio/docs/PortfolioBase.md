# PortfolioBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the portfolio. | [optional] 
**archived** | **bool** | [Opt In](/docs/inputoutput-options). True if the portfolio is archived, false if not. Archived portfolios do not show in the UI by default and may be treated differently for queries. | [optional] 
**color** | **str** | Color of the portfolio. | [optional] 

## Example

```python
from asana_asyncio.models.portfolio_base import PortfolioBase

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioBase from a JSON string
portfolio_base_instance = PortfolioBase.from_json(json)
# print the JSON string representation of the object
print(PortfolioBase.to_json())

# convert the object into a dict
portfolio_base_dict = portfolio_base_instance.to_dict()
# create an instance of PortfolioBase from a dict
portfolio_base_from_dict = PortfolioBase.from_dict(portfolio_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


