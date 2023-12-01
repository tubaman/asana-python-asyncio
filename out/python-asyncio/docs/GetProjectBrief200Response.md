# GetProjectBrief200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProjectBriefResponse**](ProjectBriefResponse.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.get_project_brief200_response import GetProjectBrief200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectBrief200Response from a JSON string
get_project_brief200_response_instance = GetProjectBrief200Response.from_json(json)
# print the JSON string representation of the object
print GetProjectBrief200Response.to_json()

# convert the object into a dict
get_project_brief200_response_dict = get_project_brief200_response_instance.to_dict()
# create an instance of GetProjectBrief200Response from a dict
get_project_brief200_response_form_dict = get_project_brief200_response.from_dict(get_project_brief200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


