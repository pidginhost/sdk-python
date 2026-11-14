# GatewayDeleteConflict

A delete's 409 answer: the conflict, and a fresh preview of what the delete takes away.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**extra** | [**GatewayDeleteConflictExtra**](GatewayDeleteConflictExtra.md) |  | 

## Example

```python
from pidginhost_sdk.models.gateway_delete_conflict import GatewayDeleteConflict

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDeleteConflict from a JSON string
gateway_delete_conflict_instance = GatewayDeleteConflict.from_json(json)
# print the JSON string representation of the object
print(GatewayDeleteConflict.to_json())

# convert the object into a dict
gateway_delete_conflict_dict = gateway_delete_conflict_instance.to_dict()
# create an instance of GatewayDeleteConflict from a dict
gateway_delete_conflict_from_dict = GatewayDeleteConflict.from_dict(gateway_delete_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


