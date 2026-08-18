# PatchedK8sPortForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**internal_ip** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_k8s_port_forward import PatchedK8sPortForward

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedK8sPortForward from a JSON string
patched_k8s_port_forward_instance = PatchedK8sPortForward.from_json(json)
# print the JSON string representation of the object
print(PatchedK8sPortForward.to_json())

# convert the object into a dict
patched_k8s_port_forward_dict = patched_k8s_port_forward_instance.to_dict()
# create an instance of PatchedK8sPortForward from a dict
patched_k8s_port_forward_from_dict = PatchedK8sPortForward.from_dict(patched_k8s_port_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


