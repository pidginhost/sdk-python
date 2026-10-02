# ServerDetailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**ssh_pub_key** | **str** | Public key to apply for SSH login. Applying a non-empty key regenerates cloud-init and reboots a running server. Clearing removes the key from future cloud-init data, but does not revoke keys already in the guest. | [optional] 

## Example

```python
from pidginhost_sdk.models.server_detail_request import ServerDetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerDetailRequest from a JSON string
server_detail_request_instance = ServerDetailRequest.from_json(json)
# print the JSON string representation of the object
print(ServerDetailRequest.to_json())

# convert the object into a dict
server_detail_request_dict = server_detail_request_instance.to_dict()
# create an instance of ServerDetailRequest from a dict
server_detail_request_from_dict = ServerDetailRequest.from_dict(server_detail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


