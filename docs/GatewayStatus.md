# GatewayStatus

A gateway's state and the customer part of its last status report; unknown values are null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**GatewayStateEnum**](GatewayStateEnum.md) |  | 
**state_reason** | **str** |  | 
**state_changed_at** | **str** |  | 
**desired_revision** | **int** |  | 
**applied_revision** | **int** |  | 
**last_status_at** | **str** |  | 
**agent_version** | **str** |  | 
**envoy_version** | **str** |  | 
**image_version** | **str** |  | 
**attempted_revision** | **int** |  | 
**local_ready** | **bool** |  | 
**clock_synchronized** | **bool** |  | 
**apply_error** | [**GatewayApplyError**](GatewayApplyError.md) |  | 
**interfaces** | [**List[GatewayInterface]**](GatewayInterface.md) |  | 
**conntrack** | [**GatewayConntrack**](GatewayConntrack.md) |  | 
**egress_probe** | [**GatewayEgressProbe**](GatewayEgressProbe.md) |  | 
**security_updates** | **int** |  | 
**reboot_required** | **bool** |  | 
**uptime_s** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.gateway_status import GatewayStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayStatus from a JSON string
gateway_status_instance = GatewayStatus.from_json(json)
# print the JSON string representation of the object
print(GatewayStatus.to_json())

# convert the object into a dict
gateway_status_dict = gateway_status_instance.to_dict()
# create an instance of GatewayStatus from a dict
gateway_status_from_dict = GatewayStatus.from_dict(gateway_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


