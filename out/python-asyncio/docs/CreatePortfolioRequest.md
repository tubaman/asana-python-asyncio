# CreatePortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PortfolioRequest**](PortfolioRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_portfolio_request import CreatePortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortfolioRequest from a JSON string
create_portfolio_request_instance = CreatePortfolioRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePortfolioRequest.to_json())

# convert the object into a dict
create_portfolio_request_dict = create_portfolio_request_instance.to_dict()
# create an instance of CreatePortfolioRequest from a dict
create_portfolio_request_from_dict = CreatePortfolioRequest.from_dict(create_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


