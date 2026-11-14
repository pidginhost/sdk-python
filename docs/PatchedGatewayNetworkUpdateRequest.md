# PatchedGatewayNetworkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snat** | **bool** | A router network&#39;s internet egress through the gateway. | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_gateway_network_update_request import PatchedGatewayNetworkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGatewayNetworkUpdateRequest from a JSON string
patched_gateway_network_update_request_instance = PatchedGatewayNetworkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGatewayNetworkUpdateRequest.to_json())

# convert the object into a dict
patched_gateway_network_update_request_dict = patched_gateway_network_update_request_instance.to_dict()
# create an instance of PatchedGatewayNetworkUpdateRequest from a dict
patched_gateway_network_update_request_from_dict = PatchedGatewayNetworkUpdateRequest.from_dict(patched_gateway_network_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


