# CreateStatusForObjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StatusUpdateRequest**](StatusUpdateRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_status_for_object_request import CreateStatusForObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStatusForObjectRequest from a JSON string
create_status_for_object_request_instance = CreateStatusForObjectRequest.from_json(json)
# print the JSON string representation of the object
print CreateStatusForObjectRequest.to_json()

# convert the object into a dict
create_status_for_object_request_dict = create_status_for_object_request_instance.to_dict()
# create an instance of CreateStatusForObjectRequest from a dict
create_status_for_object_request_form_dict = create_status_for_object_request.from_dict(create_status_for_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


