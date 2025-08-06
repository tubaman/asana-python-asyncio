# PortfolioResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | The name of the portfolio. | [optional] 
**archived** | **bool** | [Opt In](/docs/inputoutput-options). True if the portfolio is archived, false if not. Archived portfolios do not show in the UI by default and may be treated differently for queries. | [optional] 
**color** | **str** | Color of the portfolio. | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**created_by** | [**UserCompact**](UserCompact.md) |  | [optional] 
**custom_field_settings** | [**List[CustomFieldSettingResponse]**](CustomFieldSettingResponse.md) | &lt;p&gt;&lt;strong style&#x3D;\&quot;color: #4573D2\&quot;&gt;Full object requires scope: &lt;/strong&gt;&lt;code&gt;custom_fields:read&lt;/code&gt;&lt;/p&gt;  Array of custom field settings applied to the portfolio. | [optional] 
**current_status_update** | [**StatusUpdateCompact**](StatusUpdateCompact.md) | The latest &#x60;status_update&#x60; posted to this portfolio. | [optional] 
**due_on** | **date** | The localized day on which this portfolio is due. This takes a date with format YYYY-MM-DD. | [optional] 
**custom_fields** | [**List[CustomFieldCompact]**](CustomFieldCompact.md) | &lt;p&gt;&lt;strong style&#x3D;\&quot;color: #4573D2\&quot;&gt;Full object requires scope: &lt;/strong&gt;&lt;code&gt;custom_fields:read&lt;/code&gt;&lt;/p&gt;  Array of Custom Fields. | [optional] 
**members** | [**List[UserCompact]**](UserCompact.md) |  | [optional] [readonly] 
**owner** | [**UserCompact**](UserCompact.md) |  | [optional] 
**start_on** | **date** | The day on which work for this portfolio begins, or null if the portfolio has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] 
**workspace** | [**PortfolioResponseAllOfWorkspace**](PortfolioResponseAllOfWorkspace.md) |  | [optional] 
**permalink_url** | **str** | A url that points directly to the object within Asana. | [optional] [readonly] 
**public** | **bool** | True if the portfolio is public to its workspace members. | [optional] 
**default_access_level** | **str** | The default access level when inviting new members to the portfolio | [optional] 
**privacy_setting** | **str** | The privacy setting of the portfolio. *Note: Administrators in your organization may restrict the values of &#x60;privacy_setting&#x60;.* | [optional] 
**project_templates** | [**List[ProjectTemplateCompact]**](ProjectTemplateCompact.md) | Array of project templates that are in the portfolio | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.portfolio_response import PortfolioResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioResponse from a JSON string
portfolio_response_instance = PortfolioResponse.from_json(json)
# print the JSON string representation of the object
print(PortfolioResponse.to_json())

# convert the object into a dict
portfolio_response_dict = portfolio_response_instance.to_dict()
# create an instance of PortfolioResponse from a dict
portfolio_response_from_dict = PortfolioResponse.from_dict(portfolio_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


