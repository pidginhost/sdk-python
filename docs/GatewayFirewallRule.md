# GatewayFirewallRule

A firewall rule (spec 5.7): first match wins in position order; a change is pending until applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**position** | **int** |  | [readonly] 
**action** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [readonly] 
**source** | [**GatewayFirewallSource**](GatewayFirewallSource.md) |  | [readonly] 
**destination** | [**GatewayFirewallDestination**](GatewayFirewallDestination.md) |  | [readonly] 
**protocol** | [**GatewayFirewallProtocolEnum**](GatewayFirewallProtocolEnum.md) |  | [readonly] 
**ports** | [**List[GatewayPortRange]**](GatewayPortRange.md) |  | [readonly] 
**enabled** | **bool** |  | [readonly] 
**comment** | **str** |  | [readonly] 
**changed_revision** | **int** |  | [readonly] 
**pending** | **bool** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway_firewall_rule import GatewayFirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayFirewallRule from a JSON string
gateway_firewall_rule_instance = GatewayFirewallRule.from_json(json)
# print the JSON string representation of the object
print(GatewayFirewallRule.to_json())

# convert the object into a dict
gateway_firewall_rule_dict = gateway_firewall_rule_instance.to_dict()
# create an instance of GatewayFirewallRule from a dict
gateway_firewall_rule_from_dict = GatewayFirewallRule.from_dict(gateway_firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


