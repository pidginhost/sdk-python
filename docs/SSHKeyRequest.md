# SSHKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 
**key** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.ssh_key_request import SSHKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SSHKeyRequest from a JSON string
ssh_key_request_instance = SSHKeyRequest.from_json(json)
# print the JSON string representation of the object
print(SSHKeyRequest.to_json())

# convert the object into a dict
ssh_key_request_dict = ssh_key_request_instance.to_dict()
# create an instance of SSHKeyRequest from a dict
ssh_key_request_from_dict = SSHKeyRequest.from_dict(ssh_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


