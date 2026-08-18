# PaginatedLBFirewallRuleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[LBFirewallRule]**](LBFirewallRule.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_lb_firewall_rule_list import PaginatedLBFirewallRuleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLBFirewallRuleList from a JSON string
paginated_lb_firewall_rule_list_instance = PaginatedLBFirewallRuleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLBFirewallRuleList.to_json())

# convert the object into a dict
paginated_lb_firewall_rule_list_dict = paginated_lb_firewall_rule_list_instance.to_dict()
# create an instance of PaginatedLBFirewallRuleList from a dict
paginated_lb_firewall_rule_list_from_dict = PaginatedLBFirewallRuleList.from_dict(paginated_lb_firewall_rule_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


