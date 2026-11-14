# GatewayForwardTargetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** | An attached private network&#39;s id. | 
**address** | **str** | A host of that network, other than the gateway. | 
**port_start** | **int** | The first public port goes here, the next ones follow in order. | 

## Example

```python
from pidginhost_sdk.models.gateway_forward_target_request import GatewayForwardTargetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayForwardTargetRequest from a JSON string
gateway_forward_target_request_instance = GatewayForwardTargetRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayForwardTargetRequest.to_json())

# convert the object into a dict
gateway_forward_target_request_dict = gateway_forward_target_request_instance.to_dict()
# create an instance of GatewayForwardTargetRequest from a dict
gateway_forward_target_request_from_dict = GatewayForwardTargetRequest.from_dict(gateway_forward_target_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


