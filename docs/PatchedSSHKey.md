# PatchedSSHKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**alias** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] [readonly] 
**key** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_ssh_key import PatchedSSHKey

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSSHKey from a JSON string
patched_ssh_key_instance = PatchedSSHKey.from_json(json)
# print the JSON string representation of the object
print(PatchedSSHKey.to_json())

# convert the object into a dict
patched_ssh_key_dict = patched_ssh_key_instance.to_dict()
# create an instance of PatchedSSHKey from a dict
patched_ssh_key_from_dict = PatchedSSHKey.from_dict(patched_ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


