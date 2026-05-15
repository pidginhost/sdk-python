# PatchedPrivateNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**slug** | **str** | CIDR format | [optional] [readonly] 
**address** | **str** | CIDR format | [optional] 
**gateway** | **str** |  | [optional] 
**provisioned** | **bool** |  | [optional] [readonly] 
**servers** | **List[Dict[str, str]]** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_private_network import PatchedPrivateNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPrivateNetwork from a JSON string
patched_private_network_instance = PatchedPrivateNetwork.from_json(json)
# print the JSON string representation of the object
print(PatchedPrivateNetwork.to_json())

# convert the object into a dict
patched_private_network_dict = patched_private_network_instance.to_dict()
# create an instance of PatchedPrivateNetwork from a dict
patched_private_network_from_dict = PatchedPrivateNetwork.from_dict(patched_private_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


