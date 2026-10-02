# FirewallRulesSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.firewall_rules_set_request import FirewallRulesSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRulesSetRequest from a JSON string
firewall_rules_set_request_instance = FirewallRulesSetRequest.from_json(json)
# print the JSON string representation of the object
print(FirewallRulesSetRequest.to_json())

# convert the object into a dict
firewall_rules_set_request_dict = firewall_rules_set_request_instance.to_dict()
# create an instance of FirewallRulesSetRequest from a dict
firewall_rules_set_request_from_dict = FirewallRulesSetRequest.from_dict(firewall_rules_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


