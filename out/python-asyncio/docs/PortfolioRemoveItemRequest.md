# PortfolioRemoveItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | **str** | The item to remove from the portfolio. | 

## Example

```python
from asana_asyncio.models.portfolio_remove_item_request import PortfolioRemoveItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioRemoveItemRequest from a JSON string
portfolio_remove_item_request_instance = PortfolioRemoveItemRequest.from_json(json)
# print the JSON string representation of the object
print PortfolioRemoveItemRequest.to_json()

# convert the object into a dict
portfolio_remove_item_request_dict = portfolio_remove_item_request_instance.to_dict()
# create an instance of PortfolioRemoveItemRequest from a dict
portfolio_remove_item_request_form_dict = portfolio_remove_item_request.from_dict(portfolio_remove_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


