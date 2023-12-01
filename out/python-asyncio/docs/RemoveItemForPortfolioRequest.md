# RemoveItemForPortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PortfolioRemoveItemRequest**](PortfolioRemoveItemRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_item_for_portfolio_request import RemoveItemForPortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveItemForPortfolioRequest from a JSON string
remove_item_for_portfolio_request_instance = RemoveItemForPortfolioRequest.from_json(json)
# print the JSON string representation of the object
print RemoveItemForPortfolioRequest.to_json()

# convert the object into a dict
remove_item_for_portfolio_request_dict = remove_item_for_portfolio_request_instance.to_dict()
# create an instance of RemoveItemForPortfolioRequest from a dict
remove_item_for_portfolio_request_form_dict = remove_item_for_portfolio_request.from_dict(remove_item_for_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


