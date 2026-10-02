# FirewallRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**FirewallRuleDirectionEnum**](FirewallRuleDirectionEnum.md) |  | 
**action** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | 
**protocol** | **str** |  | [optional] 
**source** | **str** | single IP, range (20.34.101.207-201.3.9.99) or comma separated list | [optional] 
**sport** | **str** | numbers (0-65535), range (\&quot;\\d+:\\d+\&quot;, like \&quot;80:85\&quot;), comma separated list | [optional] 
**destination** | **str** | single IP, range (20.34.101.207-201.3.9.99) or comma separated list | [optional] 
**dport** | **str** | numbers (0-65535), range (\&quot;\\d+:\\d+\&quot;, like \&quot;80:85\&quot;), comma separated list | [optional] 
**enabled** | **bool** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.firewall_rule_request import FirewallRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRuleRequest from a JSON string
firewall_rule_request_instance = FirewallRuleRequest.from_json(json)
# print the JSON string representation of the object
print(FirewallRuleRequest.to_json())

# convert the object into a dict
firewall_rule_request_dict = firewall_rule_request_instance.to_dict()
# create an instance of FirewallRuleRequest from a dict
firewall_rule_request_from_dict = FirewallRuleRequest.from_dict(firewall_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


