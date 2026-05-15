# FirewallRulesSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**status** | [**FirewallRulesSetStatusEnum**](FirewallRulesSetStatusEnum.md) |  | [readonly] 
**rules** | [**List[FirewallRule]**](FirewallRule.md) |  | [readonly] 
**read_only** | **bool** | used with free tier vm | [readonly] 

## Example

```python
from pidginhost_sdk.models.firewall_rules_set import FirewallRulesSet

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRulesSet from a JSON string
firewall_rules_set_instance = FirewallRulesSet.from_json(json)
# print the JSON string representation of the object
print(FirewallRulesSet.to_json())

# convert the object into a dict
firewall_rules_set_dict = firewall_rules_set_instance.to_dict()
# create an instance of FirewallRulesSet from a dict
firewall_rules_set_from_dict = FirewallRulesSet.from_dict(firewall_rules_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


