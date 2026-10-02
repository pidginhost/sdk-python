# PatchedInboundRouteCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** |  | [optional] 
**mode** | [**ModeEnum**](ModeEnum.md) |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**forward_to** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_inbound_route_create_request import PatchedInboundRouteCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInboundRouteCreateRequest from a JSON string
patched_inbound_route_create_request_instance = PatchedInboundRouteCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedInboundRouteCreateRequest.to_json())

# convert the object into a dict
patched_inbound_route_create_request_dict = patched_inbound_route_create_request_instance.to_dict()
# create an instance of PatchedInboundRouteCreateRequest from a dict
patched_inbound_route_create_request_from_dict = PatchedInboundRouteCreateRequest.from_dict(patched_inbound_route_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


