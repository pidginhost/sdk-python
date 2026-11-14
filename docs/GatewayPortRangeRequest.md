# GatewayPortRangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | 
**end** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.gateway_port_range_request import GatewayPortRangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayPortRangeRequest from a JSON string
gateway_port_range_request_instance = GatewayPortRangeRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayPortRangeRequest.to_json())

# convert the object into a dict
gateway_port_range_request_dict = gateway_port_range_request_instance.to_dict()
# create an instance of GatewayPortRangeRequest from a dict
gateway_port_range_request_from_dict = GatewayPortRangeRequest.from_dict(gateway_port_range_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


