# AddCustomFieldSettingForPortfolioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AddCustomFieldSettingRequest**](AddCustomFieldSettingRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_custom_field_setting_for_portfolio_request import AddCustomFieldSettingForPortfolioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomFieldSettingForPortfolioRequest from a JSON string
add_custom_field_setting_for_portfolio_request_instance = AddCustomFieldSettingForPortfolioRequest.from_json(json)
# print the JSON string representation of the object
print(AddCustomFieldSettingForPortfolioRequest.to_json())

# convert the object into a dict
add_custom_field_setting_for_portfolio_request_dict = add_custom_field_setting_for_portfolio_request_instance.to_dict()
# create an instance of AddCustomFieldSettingForPortfolioRequest from a dict
add_custom_field_setting_for_portfolio_request_from_dict = AddCustomFieldSettingForPortfolioRequest.from_dict(add_custom_field_setting_for_portfolio_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


