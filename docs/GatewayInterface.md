# GatewayInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot** | **int** |  | 
**name** | **str** |  | 
**state** | **str** | up, down or unknown. | 
**addresses** | **List[str]** |  | 

## Example

```python
from pidginhost_sdk.models.gateway_interface import GatewayInterface

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayInterface from a JSON string
gateway_interface_instance = GatewayInterface.from_json(json)
# print the JSON string representation of the object
print(GatewayInterface.to_json())

# convert the object into a dict
gateway_interface_dict = gateway_interface_instance.to_dict()
# create an instance of GatewayInterface from a dict
gateway_interface_from_dict = GatewayInterface.from_dict(gateway_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


