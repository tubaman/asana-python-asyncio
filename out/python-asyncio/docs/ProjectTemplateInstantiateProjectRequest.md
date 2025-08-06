# ProjectTemplateInstantiateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new project. | 
**team** | **str** | *Optional*. Sets the team of the new project. If the project template exists in an _organization_, you may specify a value for &#x60;team&#x60;. If no value is provided then it defaults to the same team as the project template. | [optional] 
**public** | **bool** | *Deprecated:* new integrations use &#x60;privacy_setting&#x60; instead. | [optional] 
**privacy_setting** | **str** | The privacy setting of the project. *Note: Administrators in your organization may restrict the values of &#x60;privacy_setting&#x60;.* | [optional] 
**is_strict** | **bool** | *Optional*. If set to &#x60;true&#x60;, the endpoint returns an \&quot;Unprocessable Entity\&quot; error if you fail to provide a calendar date value for any date variable. If set to &#x60;false&#x60;, a default date is used for each unfulfilled date variable (e.g., the current date is used as the Start Date of a project). | [optional] 
**requested_dates** | [**List[DateVariableRequest]**](DateVariableRequest.md) | *Conditional*. Array of mappings of date variables to calendar dates. This property is required in the instantiation request if the project template includes dates (e.g., a start date on a task). | [optional] 
**requested_roles** | [**List[RequestedRoleRequest]**](RequestedRoleRequest.md) | Array of mappings of template roles to user ids | [optional] 

## Example

```python
from asana_asyncio.models.project_template_instantiate_project_request import ProjectTemplateInstantiateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateInstantiateProjectRequest from a JSON string
project_template_instantiate_project_request_instance = ProjectTemplateInstantiateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectTemplateInstantiateProjectRequest.to_json())

# convert the object into a dict
project_template_instantiate_project_request_dict = project_template_instantiate_project_request_instance.to_dict()
# create an instance of ProjectTemplateInstantiateProjectRequest from a dict
project_template_instantiate_project_request_from_dict = ProjectTemplateInstantiateProjectRequest.from_dict(project_template_instantiate_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


