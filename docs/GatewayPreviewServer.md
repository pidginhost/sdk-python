# GatewayPreviewServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**hostname** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.gateway_preview_server import GatewayPreviewServer

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayPreviewServer from a JSON string
gateway_preview_server_instance = GatewayPreviewServer.from_json(json)
# print the JSON string representation of the object
print(GatewayPreviewServer.to_json())

# convert the object into a dict
gateway_preview_server_dict = gateway_preview_server_instance.to_dict()
# create an instance of GatewayPreviewServer from a dict
gateway_preview_server_from_dict = GatewayPreviewServer.from_dict(gateway_preview_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


