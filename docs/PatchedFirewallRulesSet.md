# PatchedFirewallRulesSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**status** | [**FirewallRulesSetStatusEnum**](FirewallRulesSetStatusEnum.md) |  | [optional] [readonly] 
**rules** | [**List[FirewallRule]**](FirewallRule.md) |  | [optional] [readonly] 
**read_only** | **bool** | used with free tier vm | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_firewall_rules_set import PatchedFirewallRulesSet

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFirewallRulesSet from a JSON string
patched_firewall_rules_set_instance = PatchedFirewallRulesSet.from_json(json)
# print the JSON string representation of the object
print(PatchedFirewallRulesSet.to_json())

# convert the object into a dict
patched_firewall_rules_set_dict = patched_firewall_rules_set_instance.to_dict()
# create an instance of PatchedFirewallRulesSet from a dict
patched_firewall_rules_set_from_dict = PatchedFirewallRulesSet.from_dict(patched_firewall_rules_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


