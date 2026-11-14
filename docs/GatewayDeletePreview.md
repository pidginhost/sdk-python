# GatewayDeletePreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** |  | 
**servers** | [**List[GatewayPreviewServer]**](GatewayPreviewServer.md) |  | 
**networks** | [**List[GatewayPreviewNetwork]**](GatewayPreviewNetwork.md) |  | 

## Example

```python
from pidginhost_sdk.models.gateway_delete_preview import GatewayDeletePreview

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayDeletePreview from a JSON string
gateway_delete_preview_instance = GatewayDeletePreview.from_json(json)
# print the JSON string representation of the object
print(GatewayDeletePreview.to_json())

# convert the object into a dict
gateway_delete_preview_dict = gateway_delete_preview_instance.to_dict()
# create an instance of GatewayDeletePreview from a dict
gateway_delete_preview_from_dict = GatewayDeletePreview.from_dict(gateway_delete_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


