# TagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resource_type** | **str** | The base type of this resource. | [optional] [readonly] 
**name** | **str** | Name of the tag. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 
**color** | **str** | Color of the tag. | [optional] 
**notes** | **str** | Free-form textual information associated with the tag (i.e. its description). | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] [readonly] 
**followers** | [**List[UserCompact]**](UserCompact.md) | &lt;p&gt;&lt;strong style&#x3D;\&quot;color: #4573D2\&quot;&gt;Full object requires scope: &lt;/strong&gt;&lt;code&gt;users:read&lt;/code&gt;&lt;/p&gt;  Array of users following this tag. | [optional] [readonly] 
**workspace** | [**WorkspaceCompact**](WorkspaceCompact.md) |  | [optional] 
**permalink_url** | **str** | A url that points directly to the object within Asana. | [optional] [readonly] 

## Example

```python
from asana_asyncio.models.tag_response import TagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagResponse from a JSON string
tag_response_instance = TagResponse.from_json(json)
# print the JSON string representation of the object
print(TagResponse.to_json())

# convert the object into a dict
tag_response_dict = tag_response_instance.to_dict()
# create an instance of TagResponse from a dict
tag_response_from_dict = TagResponse.from_dict(tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


