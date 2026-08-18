# K8sPortForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**internal_ip** | **str** |  | 
**port** | **int** |  | 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | 

## Example

```python
from pidginhost_sdk.models.k8s_port_forward import K8sPortForward

# TODO update the JSON string below
json = "{}"
# create an instance of K8sPortForward from a JSON string
k8s_port_forward_instance = K8sPortForward.from_json(json)
# print the JSON string representation of the object
print(K8sPortForward.to_json())

# convert the object into a dict
k8s_port_forward_dict = k8s_port_forward_instance.to_dict()
# create an instance of K8sPortForward from a dict
k8s_port_forward_from_dict = K8sPortForward.from_dict(k8s_port_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


