# PatchedVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**project** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**size** | **int** | GB | [optional] 
**product** | **str** | ID or slug | [optional] 
**attached** | **bool** |  | [optional] [readonly] 
**server** | **str** |  | [optional] [readonly] [default to '']

## Example

```python
from pidginhost_sdk.models.patched_volume import PatchedVolume

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedVolume from a JSON string
patched_volume_instance = PatchedVolume.from_json(json)
# print the JSON string representation of the object
print(PatchedVolume.to_json())

# convert the object into a dict
patched_volume_dict = patched_volume_instance.to_dict()
# create an instance of PatchedVolume from a dict
patched_volume_from_dict = PatchedVolume.from_dict(patched_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


