# AddSupportingRelationshipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoalAddSupportingRelationshipRequest**](GoalAddSupportingRelationshipRequest.md) |  | [optional] 

## Example

```python
from asana_asyncio.models.add_supporting_relationship_request import AddSupportingRelationshipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddSupportingRelationshipRequest from a JSON string
add_supporting_relationship_request_instance = AddSupportingRelationshipRequest.from_json(json)
# print the JSON string representation of the object
print AddSupportingRelationshipRequest.to_json()

# convert the object into a dict
add_supporting_relationship_request_dict = add_supporting_relationship_request_instance.to_dict()
# create an instance of AddSupportingRelationshipRequest from a dict
add_supporting_relationship_request_form_dict = add_supporting_relationship_request.from_dict(add_supporting_relationship_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


