# PortfolioCompact

A *portfolio* gives a high-level overview of the status of multiple initiatives in Asana. Portfolios provide a dashboard overview of the state of multiple projects, including a progress report and the most recent [project status](/reference/project-statuses) update. Portfolios have some restrictions on size. Each portfolio has a max of 1500 items and, like projects, a max of 20 custom fields.

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
print(PortfolioCompact.to_json())

# convert the object into a dict
portfolio_compact_dict = portfolio_compact_instance.to_dict()
# create an instance of PortfolioCompact from a dict
portfolio_compact_from_dict = PortfolioCompact.from_dict(portfolio_compact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


