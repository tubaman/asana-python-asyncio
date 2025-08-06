# TypeaheadForWorkspace200Response

A generic list of objects, such as those returned by the typeahead search endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AsanaNamedResource]**](AsanaNamedResource.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.typeahead_for_workspace200_response import TypeaheadForWorkspace200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TypeaheadForWorkspace200Response from a JSON string
typeahead_for_workspace200_response_instance = TypeaheadForWorkspace200Response.from_json(json)
# print the JSON string representation of the object
print(TypeaheadForWorkspace200Response.to_json())

# convert the object into a dict
typeahead_for_workspace200_response_dict = typeahead_for_workspace200_response_instance.to_dict()
# create an instance of TypeaheadForWorkspace200Response from a dict
typeahead_for_workspace200_response_from_dict = TypeaheadForWorkspace200Response.from_dict(typeahead_for_workspace200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


