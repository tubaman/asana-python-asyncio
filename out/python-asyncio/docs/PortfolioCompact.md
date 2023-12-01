# PortfolioCompact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the portfolio. | [optional] 

## Example

```python
from asana_asyncio.models.portfolio_compact import PortfolioCompact

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioCompact from a JSON string
portfolio_compact_instance = PortfolioCompact.from_json(json)
# print the JSON string representation of the object
print PortfolioCompact.to_json()

# convert the object into a dict
portfolio_compact_dict = portfolio_compact_instance.to_dict()
# create an instance of PortfolioCompact from a dict
portfolio_compact_form_dict = portfolio_compact.from_dict(portfolio_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


