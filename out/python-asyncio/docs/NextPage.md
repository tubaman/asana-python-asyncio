# NextPage

*Conditional*. This property is only present when a limit query parameter is provided in the request. When making a paginated request, the API will return a number of results as specified by the limit parameter. If more results exist, then the response will contain a next_page attribute, which will include an offset, a relative path attribute, and a full uri attribute. If there are no more pages available, next_page will be null and no offset will be provided. Note that an offset token will expire after some time, as data may have changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **str** | Pagination offset for the request. | [optional] [readonly] 
**path** | **str** | A relative path containing the query parameters to fetch for next_page | [optional] [readonly] 
**uri** | **str** | A full uri containing the query parameters to fetch for next_page | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.next_page import NextPage

# TODO update the JSON string below
json = "{}"
# create an instance of NextPage from a JSON string
next_page_instance = NextPage.from_json(json)
# print the JSON string representation of the object
print NextPage.to_json()

# convert the object into a dict
next_page_dict = next_page_instance.to_dict()
# create an instance of NextPage from a dict
next_page_form_dict = next_page.from_dict(next_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


