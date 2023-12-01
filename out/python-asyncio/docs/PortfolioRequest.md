# PortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the portfolio. | [optional] 
**color** | **str** | Color of the portfolio. | [optional] 
**members** | **List[str]** | An array of strings identifying users. These can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] [readonly] 
**workspace** | **str** | Gid of an object. | [optional] 
**public** | **bool** | True if the portfolio is public to its workspace members. | [optional] 

## Example

```python
from asana_asyncio.models.portfolio_request import PortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioRequest from a JSON string
portfolio_request_instance = PortfolioRequest.from_json(json)
# print the JSON string representation of the object
print PortfolioRequest.to_json()

# convert the object into a dict
portfolio_request_dict = portfolio_request_instance.to_dict()
# create an instance of PortfolioRequest from a dict
portfolio_request_form_dict = portfolio_request.from_dict(portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


