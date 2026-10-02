# PatchedLBFirewallRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

## Example

```python
from pidginhost_sdk.models.patched_lb_firewall_rule_request import PatchedLBFirewallRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLBFirewallRuleRequest from a JSON string
patched_lb_firewall_rule_request_instance = PatchedLBFirewallRuleRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedLBFirewallRuleRequest.to_json())

# convert the object into a dict
patched_lb_firewall_rule_request_dict = patched_lb_firewall_rule_request_instance.to_dict()
# create an instance of PatchedLBFirewallRuleRequest from a dict
patched_lb_firewall_rule_request_from_dict = PatchedLBFirewallRuleRequest.from_dict(patched_lb_firewall_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


