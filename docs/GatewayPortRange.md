# GatewayPortRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | 
**end** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.gateway_port_range import GatewayPortRange

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayPortRange from a JSON string
gateway_port_range_instance = GatewayPortRange.from_json(json)
# print the JSON string representation of the object
print(GatewayPortRange.to_json())

# convert the object into a dict
gateway_port_range_dict = gateway_port_range_instance.to_dict()
# create an instance of GatewayPortRange from a dict
gateway_port_range_from_dict = GatewayPortRange.from_dict(gateway_port_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


