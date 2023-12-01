# CreateOrganizationExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrganizationExportRequest**](OrganizationExportRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.create_organization_export_request import CreateOrganizationExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationExportRequest from a JSON string
create_organization_export_request_instance = CreateOrganizationExportRequest.from_json(json)
# print the JSON string representation of the object
print CreateOrganizationExportRequest.to_json()

# convert the object into a dict
create_organization_export_request_dict = create_organization_export_request_instance.to_dict()
# create an instance of CreateOrganizationExportRequest from a dict
create_organization_export_request_form_dict = create_organization_export_request.from_dict(create_organization_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


