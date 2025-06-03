# CreatePortfolio201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PortfolioResponse**](PortfolioResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_portfolio201_response import CreatePortfolio201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortfolio201Response from a JSON string
create_portfolio201_response_instance = CreatePortfolio201Response.from_json(json)
# print the JSON string representation of the object
print(CreatePortfolio201Response.to_json())

# convert the object into a dict
create_portfolio201_response_dict = create_portfolio201_response_instance.to_dict()
# create an instance of CreatePortfolio201Response from a dict
create_portfolio201_response_from_dict = CreatePortfolio201Response.from_dict(create_portfolio201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


