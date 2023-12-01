# PortfolioResponseAllOfWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the workspace. | [optional] 

## Example

```python
from asana_asyncio.models.portfolio_response_all_of_workspace import PortfolioResponseAllOfWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioResponseAllOfWorkspace from a JSON string
portfolio_response_all_of_workspace_instance = PortfolioResponseAllOfWorkspace.from_json(json)
# print the JSON string representation of the object
print PortfolioResponseAllOfWorkspace.to_json()

# convert the object into a dict
portfolio_response_all_of_workspace_dict = portfolio_response_all_of_workspace_instance.to_dict()
# create an instance of PortfolioResponseAllOfWorkspace from a dict
portfolio_response_all_of_workspace_form_dict = portfolio_response_all_of_workspace.from_dict(portfolio_response_all_of_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


