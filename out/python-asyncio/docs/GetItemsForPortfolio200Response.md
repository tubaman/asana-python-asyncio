# GetItemsForPortfolio200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProjectCompact]**](ProjectCompact.md) |  | [optional] 
**next_page** | [**NextPage**](NextPage.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_items_for_portfolio200_response import GetItemsForPortfolio200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetItemsForPortfolio200Response from a JSON string
get_items_for_portfolio200_response_instance = GetItemsForPortfolio200Response.from_json(json)
# print the JSON string representation of the object
print(GetItemsForPortfolio200Response.to_json())

# convert the object into a dict
get_items_for_portfolio200_response_dict = get_items_for_portfolio200_response_instance.to_dict()
# create an instance of GetItemsForPortfolio200Response from a dict
get_items_for_portfolio200_response_from_dict = GetItemsForPortfolio200Response.from_dict(get_items_for_portfolio200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


