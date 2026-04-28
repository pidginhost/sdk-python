# PrivateNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**slug** | **str** | CIDR format | [readonly] 
**address** | **str** | CIDR format | 
**gateway** | **str** |  | [optional] 
**provisioned** | **bool** |  | [readonly] 
**servers** | **List[Dict[str, str]]** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.private_network import PrivateNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetwork from a JSON string
private_network_instance = PrivateNetwork.from_json(json)
# print the JSON string representation of the object
print(PrivateNetwork.to_json())

# convert the object into a dict
private_network_dict = private_network_instance.to_dict()
# create an instance of PrivateNetwork from a dict
private_network_from_dict = PrivateNetwork.from_dict(private_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


