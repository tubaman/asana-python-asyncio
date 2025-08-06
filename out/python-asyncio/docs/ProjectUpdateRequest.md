# ProjectUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 
**archived** | **bool** | True if the project is archived, false if not. Archived projects do not show in the UI by default and may be treated differently for queries. | [optional] 
**color** | **str** | Color of the project. | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**current_status** | [**ProjectBaseAllOfCurrentStatus**](ProjectBaseAllOfCurrentStatus.md) |  | [optional] 
**current_status_update** | [**ProjectBaseAllOfCurrentStatusUpdate**](ProjectBaseAllOfCurrentStatusUpdate.md) |  | [optional] 
**custom_field_settings** | [**List[CustomFieldSettingResponse]**](CustomFieldSettingResponse.md) | &lt;p&gt;&lt;strong style&#x3D;\&quot;color: #4573D2\&quot;&gt;Full object requires scope: &lt;/strong&gt;&lt;code&gt;custom_fields:read&lt;/code&gt;&lt;/p&gt;  Array of Custom Field Settings (in compact form). | [optional] [readonly] 
**default_view** | **str** | The default view (list, board, calendar, or timeline) of a project. | [optional] 
**due_date** | **date** | *Deprecated: new integrations should prefer the &#x60;due_on&#x60; field.* | [optional] 
**due_on** | **date** | The day on which this project is due. This takes a date with format YYYY-MM-DD. | [optional] 
**html_notes** | **str** | [Opt In](/docs/inputoutput-options). The notes of the project with formatting as HTML. | [optional] 
**members** | [**List[UserCompact]**](UserCompact.md) | Array of users who are members of this project. | [optional] [readonly] 
**modified_at** | **datetime** | The time at which this project was last modified. *Note: This does not currently reflect any changes in associations such as tasks or comments that may have been added or removed from the project.* | [optional] [readonly] 
**notes** | **str** | Free-form textual information associated with the project (ie., its description). | [optional] 
**public** | **bool** | *Deprecated:* new integrations use &#x60;privacy_setting&#x60; instead. | [optional] 
**privacy_setting** | **str** | The privacy setting of the project. *Note: Administrators in your organization may restrict the values of &#x60;privacy_setting&#x60;.* | [optional] 
**start_on** | **date** | The day on which work for this project begins, or null if the project has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; or &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] 
**default_access_level** | **str** | The default access for users or teams who join or are added as members to the project. | [optional] 
**minimum_access_level_for_customization** | **str** | The minimum access level needed for project members to modify this project&#39;s workflow and appearance. | [optional] 
**minimum_access_level_for_sharing** | **str** | The minimum access level needed for project members to share the project and manage project memberships. | [optional] 
**custom_fields** | **Dict[str, str]** | An object where each key is the GID of a custom field and its corresponding value is either an enum GID, string, number, or object (depending on the custom field type). See the [custom fields guide](/docs/custom-fields-guide) for details on creating and updating custom field values. | [optional] 
**followers** | **str** | *Create-only*. Comma separated string of users. Followers are a subset of members who have opted in to receive \&quot;tasks added\&quot; notifications for a project. | [optional] 
**owner** | **str** | The current owner of the project, may be null. | [optional] 
**team** | **str** | The team that this project is shared with. | [optional] 

## Example

```python
from asana_asyncio.models.project_update_request import ProjectUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdateRequest from a JSON string
project_update_request_instance = ProjectUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectUpdateRequest.to_json())

# convert the object into a dict
project_update_request_dict = project_update_request_instance.to_dict()
# create an instance of ProjectUpdateRequest from a dict
project_update_request_from_dict = ProjectUpdateRequest.from_dict(project_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


