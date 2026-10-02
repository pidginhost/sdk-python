# PrivateNetworkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | CIDR format | 
**gateway** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.private_network_request import PrivateNetworkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkRequest from a JSON string
private_network_request_instance = PrivateNetworkRequest.from_json(json)
# print the JSON string representation of the object
print(PrivateNetworkRequest.to_json())

# convert the object into a dict
private_network_request_dict = private_network_request_instance.to_dict()
# create an instance of PrivateNetworkRequest from a dict
private_network_request_from_dict = PrivateNetworkRequest.from_dict(private_network_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


