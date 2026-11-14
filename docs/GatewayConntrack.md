# GatewayConntrack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**max** | **int** |  | 
**insert_failures** | **str** | An unsigned 64-bit decimal string. | 

## Example

```python
from pidginhost_sdk.models.gateway_conntrack import GatewayConntrack

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayConntrack from a JSON string
gateway_conntrack_instance = GatewayConntrack.from_json(json)
# print the JSON string representation of the object
print(GatewayConntrack.to_json())

# convert the object into a dict
gateway_conntrack_dict = gateway_conntrack_instance.to_dict()
# create an instance of GatewayConntrack from a dict
gateway_conntrack_from_dict = GatewayConntrack.from_dict(gateway_conntrack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


