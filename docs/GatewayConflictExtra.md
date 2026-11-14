# GatewayConflictExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **Dict[str, List[str]]** |  | 
**preview** | [**GatewayPreview**](GatewayPreview.md) | Present when the confirmation is stale. | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_conflict_extra import GatewayConflictExtra

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayConflictExtra from a JSON string
gateway_conflict_extra_instance = GatewayConflictExtra.from_json(json)
# print the JSON string representation of the object
print(GatewayConflictExtra.to_json())

# convert the object into a dict
gateway_conflict_extra_dict = gateway_conflict_extra_instance.to_dict()
# create an instance of GatewayConflictExtra from a dict
gateway_conflict_extra_from_dict = GatewayConflictExtra.from_dict(gateway_conflict_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


