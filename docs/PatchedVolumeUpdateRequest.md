# PatchedVolumeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**size** | **int** | GB | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_volume_update_request import PatchedVolumeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedVolumeUpdateRequest from a JSON string
patched_volume_update_request_instance = PatchedVolumeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedVolumeUpdateRequest.to_json())

# convert the object into a dict
patched_volume_update_request_dict = patched_volume_update_request_instance.to_dict()
# create an instance of PatchedVolumeUpdateRequest from a dict
patched_volume_update_request_from_dict = PatchedVolumeUpdateRequest.from_dict(patched_volume_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


