# GatewayPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** |  | 
**servers** | [**List[GatewayPreviewServer]**](GatewayPreviewServer.md) |  | 

## Example

```python
from pidginhost_sdk.models.gateway_preview import GatewayPreview

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayPreview from a JSON string
gateway_preview_instance = GatewayPreview.from_json(json)
# print the JSON string representation of the object
print(GatewayPreview.to_json())

# convert the object into a dict
gateway_preview_dict = gateway_preview_instance.to_dict()
# create an instance of GatewayPreview from a dict
gateway_preview_from_dict = GatewayPreview.from_dict(gateway_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


