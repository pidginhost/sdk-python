# Gateway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**state** | [**GatewayStateEnum**](GatewayStateEnum.md) |  | [readonly] 
**state_reason** | **str** |  | [readonly] 
**status** | [**ResourceStatusEnum**](ResourceStatusEnum.md) |  | [readonly] 
**desired_revision** | **int** |  | [readonly] 
**applied_revision** | **int** |  | [readonly] 
**ipv4** | **str** |  | [readonly] 
**ipv6** | **str** |  | [readonly] 
**maintenance_weekday** | **int** |  | [readonly] 
**maintenance_hour** | **int** |  | [readonly] 
**ha_enabled** | **bool** |  | [readonly] 
**current_operation** | **UUID** |  | [readonly] 
**created** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.gateway import Gateway

# TODO update the JSON string below
json = "{}"
# create an instance of Gateway from a JSON string
gateway_instance = Gateway.from_json(json)
# print the JSON string representation of the object
print(Gateway.to_json())

# convert the object into a dict
gateway_dict = gateway_instance.to_dict()
# create an instance of Gateway from a dict
gateway_from_dict = Gateway.from_dict(gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


