# GetPortfolios200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PortfolioCompact]**](PortfolioCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_portfolios200_response import GetPortfolios200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPortfolios200Response from a JSON string
get_portfolios200_response_instance = GetPortfolios200Response.from_json(json)
# print the JSON string representation of the object
print(GetPortfolios200Response.to_json())

# convert the object into a dict
get_portfolios200_response_dict = get_portfolios200_response_instance.to_dict()
# create an instance of GetPortfolios200Response from a dict
get_portfolios200_response_from_dict = GetPortfolios200Response.from_dict(get_portfolios200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


