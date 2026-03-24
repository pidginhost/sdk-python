# LBFirewallRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
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
**created** | **str** |  | [readonly] 
**updated** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.lb_firewall_rule import LBFirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of LBFirewallRule from a JSON string
lb_firewall_rule_instance = LBFirewallRule.from_json(json)
# print the JSON string representation of the object
print(LBFirewallRule.to_json())

# convert the object into a dict
lb_firewall_rule_dict = lb_firewall_rule_instance.to_dict()
# create an instance of LBFirewallRule from a dict
lb_firewall_rule_from_dict = LBFirewallRule.from_dict(lb_firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


