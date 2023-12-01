# AddItemForPortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PortfolioAddItemRequest**](PortfolioAddItemRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_item_for_portfolio_request import AddItemForPortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemForPortfolioRequest from a JSON string
add_item_for_portfolio_request_instance = AddItemForPortfolioRequest.from_json(json)
# print the JSON string representation of the object
print AddItemForPortfolioRequest.to_json()

# convert the object into a dict
add_item_for_portfolio_request_dict = add_item_for_portfolio_request_instance.to_dict()
# create an instance of AddItemForPortfolioRequest from a dict
add_item_for_portfolio_request_form_dict = add_item_for_portfolio_request.from_dict(add_item_for_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


