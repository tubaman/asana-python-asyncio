# PortfolioAddItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | **str** | The item to add to the portfolio. | 
**insert_before** | **str** | An id of an item in this portfolio. The new item will be added before the one specified here. &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. | [optional] 
**insert_after** | **str** | An id of an item in this portfolio. The new item will be added after the one specified here. &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. | [optional] 

## Example

```python
from asana_asyncio.models.portfolio_add_item_request import PortfolioAddItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioAddItemRequest from a JSON string
portfolio_add_item_request_instance = PortfolioAddItemRequest.from_json(json)
# print the JSON string representation of the object
print(PortfolioAddItemRequest.to_json())

# convert the object into a dict
portfolio_add_item_request_dict = portfolio_add_item_request_instance.to_dict()
# create an instance of PortfolioAddItemRequest from a dict
portfolio_add_item_request_from_dict = PortfolioAddItemRequest.from_dict(portfolio_add_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


