# GatewayEgressProbe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | 
**latency_ms** | **int** |  | 
**at** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.gateway_egress_probe import GatewayEgressProbe

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayEgressProbe from a JSON string
gateway_egress_probe_instance = GatewayEgressProbe.from_json(json)
# print the JSON string representation of the object
print(GatewayEgressProbe.to_json())

# convert the object into a dict
gateway_egress_probe_dict = gateway_egress_probe_instance.to_dict()
# create an instance of GatewayEgressProbe from a dict
gateway_egress_probe_from_dict = GatewayEgressProbe.from_dict(gateway_egress_probe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


