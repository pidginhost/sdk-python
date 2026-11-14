# GatewayRouteOutcome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | queued, running, applied or failed. | 
**completed_at** | **str** |  | 
**reason** | **str** | Why the server failed, or why its applied route is not acknowledged. | 

## Example

```python
from pidginhost_sdk.models.gateway_route_outcome import GatewayRouteOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayRouteOutcome from a JSON string
gateway_route_outcome_instance = GatewayRouteOutcome.from_json(json)
# print the JSON string representation of the object
print(GatewayRouteOutcome.to_json())

# convert the object into a dict
gateway_route_outcome_dict = gateway_route_outcome_instance.to_dict()
# create an instance of GatewayRouteOutcome from a dict
gateway_route_outcome_from_dict = GatewayRouteOutcome.from_dict(gateway_route_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


