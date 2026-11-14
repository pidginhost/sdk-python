# GatewayNetwork

One network the gateway is attached to (spec 5.3). A change is pending until the agent applies its revision (spec 11.2); a failure shows a reason, never its text. The NIC's MAC stays internal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** |  | [readonly] 
**role** | [**GatewayNetworkRoleEnum**](GatewayNetworkRoleEnum.md) |  | [readonly] 
**snat** | **bool** |  | [readonly] 
**state** | [**GatewayNetworkStateEnum**](GatewayNetworkStateEnum.md) |  | [readonly] 
**slot** | **int** |  | [readonly] 
**address** | **str** |  | [readonly] 
**changed_revision** | **int** |  | [readonly] 
**pending** | **bool** |  | [readonly] 
**reason** | **str** | Why the last network change failed, or empty. | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway_network import GatewayNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayNetwork from a JSON string
gateway_network_instance = GatewayNetwork.from_json(json)
# print the JSON string representation of the object
print(GatewayNetwork.to_json())

# convert the object into a dict
gateway_network_dict = gateway_network_instance.to_dict()
# create an instance of GatewayNetwork from a dict
gateway_network_from_dict = GatewayNetwork.from_dict(gateway_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


