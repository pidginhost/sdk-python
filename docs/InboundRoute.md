# InboundRoute


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

## Example

```python
from pidginhost_sdk.models.inbound_route import InboundRoute

# TODO update the JSON string below
json = "{}"
# create an instance of InboundRoute from a JSON string
inbound_route_instance = InboundRoute.from_json(json)
# print the JSON string representation of the object
print(InboundRoute.to_json())

# convert the object into a dict
inbound_route_dict = inbound_route_instance.to_dict()
# create an instance of InboundRoute from a dict
inbound_route_from_dict = InboundRoute.from_dict(inbound_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


