# PatchedGatewayBackendWriteRequest

The fields a customer writes; gateway.backend_pools.clean_backend decides what they may hold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** | An attached private network&#39;s id. | [optional] 
**address** | **str** | A host of that network, other than the gateway. | [optional] 
**port** | **int** |  | [optional] 
**weight** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_gateway_backend_write_request import PatchedGatewayBackendWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGatewayBackendWriteRequest from a JSON string
patched_gateway_backend_write_request_instance = PatchedGatewayBackendWriteRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGatewayBackendWriteRequest.to_json())

# convert the object into a dict
patched_gateway_backend_write_request_dict = patched_gateway_backend_write_request_instance.to_dict()
# create an instance of PatchedGatewayBackendWriteRequest from a dict
patched_gateway_backend_write_request_from_dict = PatchedGatewayBackendWriteRequest.from_dict(patched_gateway_backend_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


