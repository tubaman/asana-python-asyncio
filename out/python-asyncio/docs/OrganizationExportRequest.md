# OrganizationExportRequest

An *organization_export* request starts a job to export the complete data of the given Organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **str** | Globally unique identifier for the workspace or organization. | [optional] 

## Example

```python
from asana_asyncio.models.organization_export_request import OrganizationExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationExportRequest from a JSON string
organization_export_request_instance = OrganizationExportRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationExportRequest.to_json())

# convert the object into a dict
organization_export_request_dict = organization_export_request_instance.to_dict()
# create an instance of OrganizationExportRequest from a dict
organization_export_request_from_dict = OrganizationExportRequest.from_dict(organization_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


