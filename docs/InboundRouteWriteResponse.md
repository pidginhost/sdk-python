# InboundRouteWriteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**domain** | **int** |  | [readonly] 
**pattern** | **str** |  | 
**mode** | [**ModeEnum**](ModeEnum.md) |  | 
**webhook_url** | **str** |  | [optional] 
**forward_to** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **str** |  | [readonly] 
**webhook_secret** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.inbound_route_write_response import InboundRouteWriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InboundRouteWriteResponse from a JSON string
inbound_route_write_response_instance = InboundRouteWriteResponse.from_json(json)
# print the JSON string representation of the object
print(InboundRouteWriteResponse.to_json())

# convert the object into a dict
inbound_route_write_response_dict = inbound_route_write_response_instance.to_dict()
# create an instance of InboundRouteWriteResponse from a dict
inbound_route_write_response_from_dict = InboundRouteWriteResponse.from_dict(inbound_route_write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


