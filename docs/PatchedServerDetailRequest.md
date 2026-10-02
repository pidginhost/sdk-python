# PatchedServerDetailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**ssh_pub_key** | **str** | Public key to apply for SSH login. Applying a non-empty key regenerates cloud-init and reboots a running server. Clearing removes the key from future cloud-init data, but does not revoke keys already in the guest. | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_server_detail_request import PatchedServerDetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedServerDetailRequest from a JSON string
patched_server_detail_request_instance = PatchedServerDetailRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedServerDetailRequest.to_json())

# convert the object into a dict
patched_server_detail_request_dict = patched_server_detail_request_instance.to_dict()
# create an instance of PatchedServerDetailRequest from a dict
patched_server_detail_request_from_dict = PatchedServerDetailRequest.from_dict(patched_server_detail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


