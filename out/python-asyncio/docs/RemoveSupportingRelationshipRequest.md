# RemoveSupportingRelationshipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoalRemoveSupportingRelationshipRequest**](GoalRemoveSupportingRelationshipRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.remove_supporting_relationship_request import RemoveSupportingRelationshipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveSupportingRelationshipRequest from a JSON string
remove_supporting_relationship_request_instance = RemoveSupportingRelationshipRequest.from_json(json)
# print the JSON string representation of the object
print RemoveSupportingRelationshipRequest.to_json()

# convert the object into a dict
remove_supporting_relationship_request_dict = remove_supporting_relationship_request_instance.to_dict()
# create an instance of RemoveSupportingRelationshipRequest from a dict
remove_supporting_relationship_request_form_dict = remove_supporting_relationship_request.from_dict(remove_supporting_relationship_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


