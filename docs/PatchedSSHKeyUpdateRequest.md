# PatchedSSHKeyUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_ssh_key_update_request import PatchedSSHKeyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSSHKeyUpdateRequest from a JSON string
patched_ssh_key_update_request_instance = PatchedSSHKeyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSSHKeyUpdateRequest.to_json())

# convert the object into a dict
patched_ssh_key_update_request_dict = patched_ssh_key_update_request_instance.to_dict()
# create an instance of PatchedSSHKeyUpdateRequest from a dict
patched_ssh_key_update_request_from_dict = PatchedSSHKeyUpdateRequest.from_dict(patched_ssh_key_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


