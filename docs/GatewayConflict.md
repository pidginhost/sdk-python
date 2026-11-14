# GatewayConflict

A 409 answer: the conflict, and for a destructive action a fresh preview to confirm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**extra** | [**GatewayConflictExtra**](GatewayConflictExtra.md) |  | 

## Example

```python
from pidginhost_sdk.models.gateway_conflict import GatewayConflict

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayConflict from a JSON string
gateway_conflict_instance = GatewayConflict.from_json(json)
# print the JSON string representation of the object
print(GatewayConflict.to_json())

# convert the object into a dict
gateway_conflict_dict = gateway_conflict_instance.to_dict()
# create an instance of GatewayConflict from a dict
gateway_conflict_from_dict = GatewayConflict.from_dict(gateway_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


