# PatchedProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**funds** | **decimal.Decimal** |  | [optional] [readonly] 
**phone** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_profile import PatchedProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProfile from a JSON string
patched_profile_instance = PatchedProfile.from_json(json)
# print the JSON string representation of the object
print(PatchedProfile.to_json())

# convert the object into a dict
patched_profile_dict = patched_profile_instance.to_dict()
# create an instance of PatchedProfile from a dict
patched_profile_from_dict = PatchedProfile.from_dict(patched_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


