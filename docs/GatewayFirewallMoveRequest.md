# GatewayFirewallMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | The position to move the rule to, from 0. | 

## Example

```python
from pidginhost_sdk.models.gateway_firewall_move_request import GatewayFirewallMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayFirewallMoveRequest from a JSON string
gateway_firewall_move_request_instance = GatewayFirewallMoveRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayFirewallMoveRequest.to_json())

# convert the object into a dict
gateway_firewall_move_request_dict = gateway_firewall_move_request_instance.to_dict()
# create an instance of GatewayFirewallMoveRequest from a dict
gateway_firewall_move_request_from_dict = GatewayFirewallMoveRequest.from_dict(gateway_firewall_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


