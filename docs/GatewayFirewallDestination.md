# GatewayFirewallDestination

Exactly one of network, cidr and internet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** | A private network the gateway is attached to. | [optional] 
**cidr** | **str** | An IPv4 network, such as 10.0.0.0/24. | [optional] 
**internet** | **bool** | True: egress by the gateway&#39;s WAN. | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_firewall_destination import GatewayFirewallDestination

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayFirewallDestination from a JSON string
gateway_firewall_destination_instance = GatewayFirewallDestination.from_json(json)
# print the JSON string representation of the object
print(GatewayFirewallDestination.to_json())

# convert the object into a dict
gateway_firewall_destination_dict = gateway_firewall_destination_instance.to_dict()
# create an instance of GatewayFirewallDestination from a dict
gateway_firewall_destination_from_dict = GatewayFirewallDestination.from_dict(gateway_firewall_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


