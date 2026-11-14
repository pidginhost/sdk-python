# GatewayReenrollConflict

A re-enrollment's 409 answer: the conflict, and a fresh preview of what the restart takes away.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**extra** | [**GatewayDeleteConflictExtra**](GatewayDeleteConflictExtra.md) |  | 

## Example

```python
from pidginhost_sdk.models.gateway_reenroll_conflict import GatewayReenrollConflict

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayReenrollConflict from a JSON string
gateway_reenroll_conflict_instance = GatewayReenrollConflict.from_json(json)
# print the JSON string representation of the object
print(GatewayReenrollConflict.to_json())

# convert the object into a dict
gateway_reenroll_conflict_dict = gateway_reenroll_conflict_instance.to_dict()
# create an instance of GatewayReenrollConflict from a dict
gateway_reenroll_conflict_from_dict = GatewayReenrollConflict.from_dict(gateway_reenroll_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


