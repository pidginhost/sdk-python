# PatchedFirewallRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**direction** | [**FirewallRuleDirectionEnum**](FirewallRuleDirectionEnum.md) |  | [optional] 
**action** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [optional] 
**protocol** | **str** |  | [optional] 
**source** | **str** | single IP, range (20.34.101.207-201.3.9.99) or comma separated list | [optional] 
**sport** | **str** | numbers (0-65535), range (\&quot;\\d+:\\d+\&quot;, like \&quot;80:85\&quot;), comma separated list | [optional] 
**destination** | **str** | single IP, range (20.34.101.207-201.3.9.99) or comma separated list | [optional] 
**dport** | **str** | numbers (0-65535), range (\&quot;\\d+:\\d+\&quot;, like \&quot;80:85\&quot;), comma separated list | [optional] 
**enabled** | **bool** |  | [optional] 
**position** | **int** |  | [optional] 
**has_error** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_firewall_rule import PatchedFirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFirewallRule from a JSON string
patched_firewall_rule_instance = PatchedFirewallRule.from_json(json)
# print the JSON string representation of the object
print(PatchedFirewallRule.to_json())

# convert the object into a dict
patched_firewall_rule_dict = patched_firewall_rule_instance.to_dict()
# create an instance of PatchedFirewallRule from a dict
patched_firewall_rule_from_dict = PatchedFirewallRule.from_dict(patched_firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


