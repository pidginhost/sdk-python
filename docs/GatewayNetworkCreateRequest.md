# GatewayNetworkCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **int** | A private network of the service. | 
**role** | [**GatewayNetworkRoleEnum**](GatewayNetworkRoleEnum.md) |  | 

## Example

```python
from pidginhost_sdk.models.gateway_network_create_request import GatewayNetworkCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayNetworkCreateRequest from a JSON string
gateway_network_create_request_instance = GatewayNetworkCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayNetworkCreateRequest.to_json())

# convert the object into a dict
gateway_network_create_request_dict = gateway_network_create_request_instance.to_dict()
# create an instance of GatewayNetworkCreateRequest from a dict
gateway_network_create_request_from_dict = GatewayNetworkCreateRequest.from_dict(gateway_network_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


