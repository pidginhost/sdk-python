# PatchedGatewayFirewallRuleWriteRequest

The fields a customer writes; gateway.firewall.clean_rule decides what they may hold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [optional] 
**source** | [**GatewayFirewallSourceRequest**](GatewayFirewallSourceRequest.md) |  | [optional] 
**destination** | [**GatewayFirewallDestinationRequest**](GatewayFirewallDestinationRequest.md) |  | [optional] 
**protocol** | [**GatewayFirewallProtocolEnum**](GatewayFirewallProtocolEnum.md) |  | [optional] 
**ports** | [**List[GatewayPortRangeRequest]**](GatewayPortRangeRequest.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_gateway_firewall_rule_write_request import PatchedGatewayFirewallRuleWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGatewayFirewallRuleWriteRequest from a JSON string
patched_gateway_firewall_rule_write_request_instance = PatchedGatewayFirewallRuleWriteRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGatewayFirewallRuleWriteRequest.to_json())

# convert the object into a dict
patched_gateway_firewall_rule_write_request_dict = patched_gateway_firewall_rule_write_request_instance.to_dict()
# create an instance of PatchedGatewayFirewallRuleWriteRequest from a dict
patched_gateway_firewall_rule_write_request_from_dict = PatchedGatewayFirewallRuleWriteRequest.from_dict(patched_gateway_firewall_rule_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


