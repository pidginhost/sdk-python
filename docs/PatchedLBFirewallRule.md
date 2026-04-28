# PatchedLBFirewallRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**direction** | [**LBFirewallRuleDirectionEnum**](LBFirewallRuleDirectionEnum.md) |  | [optional] 
**action** | [**LBFirewallRuleActionEnum**](LBFirewallRuleActionEnum.md) |  | [optional] 
**protocol** | **str** | tcp, udp, icmp, etc. | [optional] 
**source** | **str** | IP address or CIDR | [optional] 
**sport** | **str** | Port or range (e.g., 1024-65535) | [optional] 
**destination** | **str** | IP address or CIDR | [optional] 
**dport** | **str** | Port or range (e.g., 80, 8000-9000) | [optional] 
**comment** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**position** | **int** | Rule order (lower &#x3D; higher priority) | [optional] 
**created** | **str** |  | [optional] [readonly] 
**updated** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_lb_firewall_rule import PatchedLBFirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLBFirewallRule from a JSON string
patched_lb_firewall_rule_instance = PatchedLBFirewallRule.from_json(json)
# print the JSON string representation of the object
print(PatchedLBFirewallRule.to_json())

# convert the object into a dict
patched_lb_firewall_rule_dict = patched_lb_firewall_rule_instance.to_dict()
# create an instance of PatchedLBFirewallRule from a dict
patched_lb_firewall_rule_from_dict = PatchedLBFirewallRule.from_dict(patched_lb_firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


