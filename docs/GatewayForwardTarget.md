# GatewayForwardTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** | An attached private network&#39;s id. | 
**address** | **str** | A host of that network, other than the gateway. | 
**port_start** | **int** | The first public port goes here, the next ones follow in order. | 

## Example

```python
from pidginhost_sdk.models.gateway_forward_target import GatewayForwardTarget

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayForwardTarget from a JSON string
gateway_forward_target_instance = GatewayForwardTarget.from_json(json)
# print the JSON string representation of the object
print(GatewayForwardTarget.to_json())

# convert the object into a dict
gateway_forward_target_dict = gateway_forward_target_instance.to_dict()
# create an instance of GatewayForwardTarget from a dict
gateway_forward_target_from_dict = GatewayForwardTarget.from_dict(gateway_forward_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


