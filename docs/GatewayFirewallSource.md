# GatewayFirewallSource

Exactly one of network and cidr.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** | A private network the gateway is attached to. | [optional] 
**cidr** | **str** | An IPv4 network, such as 10.0.0.0/24. | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_firewall_source import GatewayFirewallSource

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayFirewallSource from a JSON string
gateway_firewall_source_instance = GatewayFirewallSource.from_json(json)
# print the JSON string representation of the object
print(GatewayFirewallSource.to_json())

# convert the object into a dict
gateway_firewall_source_dict = gateway_firewall_source_instance.to_dict()
# create an instance of GatewayFirewallSource from a dict
gateway_firewall_source_from_dict = GatewayFirewallSource.from_dict(gateway_firewall_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


