# GatewayOperation

An operation's progress (spec 5.11). A route apply's per-server evidence (node, QEMU process, guest boot, config) stays internal: each server shows its status. Error text is never published, as it can be a Proxmox exception's text, which names nodes: a failure shows a reason from the fixed vocabulary in gateway.reasons.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [readonly] 
**kind** | [**GatewayOperationKindEnum**](GatewayOperationKindEnum.md) |  | [readonly] 
**status** | [**GatewayOperationStatusEnum**](GatewayOperationStatusEnum.md) |  | [readonly] 
**network** | **int** |  | [readonly] 
**revision** | **int** |  | [readonly] 
**started_at** | **str** |  | [readonly] 
**deadline_at** | **str** |  | [readonly] 
**completed_at** | **str** |  | [readonly] 
**servers** | **List[int]** |  | [readonly] 
**outcomes** | [**Dict[str, GatewayRouteOutcome]**](GatewayRouteOutcome.md) |  | [readonly] 
**reason** | **str** | Why the operation failed; empty unless it did. | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway_operation import GatewayOperation

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayOperation from a JSON string
gateway_operation_instance = GatewayOperation.from_json(json)
# print the JSON string representation of the object
print(GatewayOperation.to_json())

# convert the object into a dict
gateway_operation_dict = gateway_operation_instance.to_dict()
# create an instance of GatewayOperation from a dict
gateway_operation_from_dict = GatewayOperation.from_dict(gateway_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


