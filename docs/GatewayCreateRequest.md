# GatewayCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**ipv4** | **str** |  | [optional] 
**ipv6** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.gateway_create_request import GatewayCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayCreateRequest from a JSON string
gateway_create_request_instance = GatewayCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GatewayCreateRequest.to_json())

# convert the object into a dict
gateway_create_request_dict = gateway_create_request_instance.to_dict()
# create an instance of GatewayCreateRequest from a dict
gateway_create_request_from_dict = GatewayCreateRequest.from_dict(gateway_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


