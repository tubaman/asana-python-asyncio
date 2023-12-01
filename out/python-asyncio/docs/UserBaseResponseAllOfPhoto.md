# UserBaseResponseAllOfPhoto

A map of the user’s profile photo in various sizes, or null if no photo is set. Sizes provided are 21, 27, 36, 60, 128, and 1024. All images are in PNG format, except for 1024 (which is in JPEG format).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_21x21** | **str** |  | [optional] 
**image_27x27** | **str** |  | [optional] 
**image_36x36** | **str** |  | [optional] 
**image_60x60** | **str** |  | [optional] 
**image_128x128** | **str** |  | [optional] 
**image_1024x1024** | **str** |  | [optional] 

## Example

```python
from asana_asyncio.models.user_base_response_all_of_photo import UserBaseResponseAllOfPhoto

# TODO update the JSON string below
json = "{}"
# create an instance of UserBaseResponseAllOfPhoto from a JSON string
user_base_response_all_of_photo_instance = UserBaseResponseAllOfPhoto.from_json(json)
# print the JSON string representation of the object
print UserBaseResponseAllOfPhoto.to_json()

# convert the object into a dict
user_base_response_all_of_photo_dict = user_base_response_all_of_photo_instance.to_dict()
# create an instance of UserBaseResponseAllOfPhoto from a dict
user_base_response_all_of_photo_form_dict = user_base_response_all_of_photo.from_dict(user_base_response_all_of_photo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


