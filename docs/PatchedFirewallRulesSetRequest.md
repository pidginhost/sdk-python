# PatchedFirewallRulesSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_firewall_rules_set_request import PatchedFirewallRulesSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFirewallRulesSetRequest from a JSON string
patched_firewall_rules_set_request_instance = PatchedFirewallRulesSetRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedFirewallRulesSetRequest.to_json())

# convert the object into a dict
patched_firewall_rules_set_request_dict = patched_firewall_rules_set_request_instance.to_dict()
# create an instance of PatchedFirewallRulesSetRequest from a dict
patched_firewall_rules_set_request_from_dict = PatchedFirewallRulesSetRequest.from_dict(patched_firewall_rules_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


