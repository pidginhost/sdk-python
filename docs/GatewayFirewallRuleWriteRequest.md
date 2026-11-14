# GatewayFirewallRuleWriteRequest

The fields a customer writes; gateway.firewall.clean_rule decides what they may hold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | 
**source** | [**GatewayFirewallSourceRequest**](GatewayFirewallSourceRequest.md) |  | 
**destination** | [**GatewayFirewallDestinationRequest**](GatewayFirewallDestinationRequest.md) |  | 
**protocol** | [**GatewayFirewallProtocolEnum**](GatewayFirewallProtocolEnum.md) |  | 
**ports** | [**List[GatewayPortRangeRequest]**](GatewayPortRangeRequest.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_firewall_rule_write_request import GatewayFirewallRuleWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayFirewallRuleWriteRequest from a JSON string
gateway_firewall_rule_write_request_instance = GatewayFirewallRuleWriteRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayFirewallRuleWriteRequest.to_json())

# convert the object into a dict
gateway_firewall_rule_write_request_dict = gateway_firewall_rule_write_request_instance.to_dict()
# create an instance of GatewayFirewallRuleWriteRequest from a dict
gateway_firewall_rule_write_request_from_dict = GatewayFirewallRuleWriteRequest.from_dict(gateway_firewall_rule_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


