# SSHKeyUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.ssh_key_update_request import SSHKeyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SSHKeyUpdateRequest from a JSON string
ssh_key_update_request_instance = SSHKeyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SSHKeyUpdateRequest.to_json())

# convert the object into a dict
ssh_key_update_request_dict = ssh_key_update_request_instance.to_dict()
# create an instance of SSHKeyUpdateRequest from a dict
ssh_key_update_request_from_dict = SSHKeyUpdateRequest.from_dict(ssh_key_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


