# PatchedProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_profile_request import PatchedProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProfileRequest from a JSON string
patched_profile_request_instance = PatchedProfileRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedProfileRequest.to_json())

# convert the object into a dict
patched_profile_request_dict = patched_profile_request_instance.to_dict()
# create an instance of PatchedProfileRequest from a dict
patched_profile_request_from_dict = PatchedProfileRequest.from_dict(patched_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


