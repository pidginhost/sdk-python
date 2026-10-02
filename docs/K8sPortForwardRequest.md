# K8sPortForwardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_ip** | **str** |  | 
**port** | **int** |  | 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | 

## Example

```python
from pidginhost_sdk.models.k8s_port_forward_request import K8sPortForwardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of K8sPortForwardRequest from a JSON string
k8s_port_forward_request_instance = K8sPortForwardRequest.from_json(json)
# print the JSON string representation of the object
print(K8sPortForwardRequest.to_json())

# convert the object into a dict
k8s_port_forward_request_dict = k8s_port_forward_request_instance.to_dict()
# create an instance of K8sPortForwardRequest from a dict
k8s_port_forward_request_from_dict = K8sPortForwardRequest.from_dict(k8s_port_forward_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


