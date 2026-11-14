# GatewayFirewallDestinationRequest

Exactly one of network, cidr and internet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** | A private network the gateway is attached to. | [optional] 
**cidr** | **str** | An IPv4 network, such as 10.0.0.0/24. | [optional] 
**internet** | **bool** | True: egress by the gateway&#39;s WAN. | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_firewall_destination_request import GatewayFirewallDestinationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayFirewallDestinationRequest from a JSON string
gateway_firewall_destination_request_instance = GatewayFirewallDestinationRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayFirewallDestinationRequest.to_json())

# convert the object into a dict
gateway_firewall_destination_request_dict = gateway_firewall_destination_request_instance.to_dict()
# create an instance of GatewayFirewallDestinationRequest from a dict
gateway_firewall_destination_request_from_dict = GatewayFirewallDestinationRequest.from_dict(gateway_firewall_destination_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


