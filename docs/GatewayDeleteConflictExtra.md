# GatewayDeleteConflictExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **Dict[str, List[str]]** |  | 
**preview** | [**GatewayDeletePreview**](GatewayDeletePreview.md) | Present when the confirmation is stale. | [optional] 

## Example

```python
from pidginhost_sdk.models.gateway_delete_conflict_extra import GatewayDeleteConflictExtra

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDeleteConflictExtra from a JSON string
gateway_delete_conflict_extra_instance = GatewayDeleteConflictExtra.from_json(json)
# print the JSON string representation of the object
print(GatewayDeleteConflictExtra.to_json())

# convert the object into a dict
gateway_delete_conflict_extra_dict = gateway_delete_conflict_extra_instance.to_dict()
# create an instance of GatewayDeleteConflictExtra from a dict
gateway_delete_conflict_extra_from_dict = GatewayDeleteConflictExtra.from_dict(gateway_delete_conflict_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


