# PatchedInboundRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**domain** | **int** |  | [optional] [readonly] 
**pattern** | **str** |  | [optional] 
**mode** | [**ModeEnum**](ModeEnum.md) |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**forward_to** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_inbound_route import PatchedInboundRoute

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInboundRoute from a JSON string
patched_inbound_route_instance = PatchedInboundRoute.from_json(json)
# print the JSON string representation of the object
print(PatchedInboundRoute.to_json())

# convert the object into a dict
patched_inbound_route_dict = patched_inbound_route_instance.to_dict()
# create an instance of PatchedInboundRoute from a dict
patched_inbound_route_from_dict = PatchedInboundRoute.from_dict(patched_inbound_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


