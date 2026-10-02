# InboundRouteCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** |  | 
**mode** | [**ModeEnum**](ModeEnum.md) |  | 
**webhook_url** | **str** |  | [optional] 
**forward_to** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.inbound_route_create_request import InboundRouteCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InboundRouteCreateRequest from a JSON string
inbound_route_create_request_instance = InboundRouteCreateRequest.from_json(json)
# print the JSON string representation of the object
print(InboundRouteCreateRequest.to_json())

# convert the object into a dict
inbound_route_create_request_dict = inbound_route_create_request_instance.to_dict()
# create an instance of InboundRouteCreateRequest from a dict
inbound_route_create_request_from_dict = InboundRouteCreateRequest.from_dict(inbound_route_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


