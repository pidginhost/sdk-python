# PatchedK8sPortForwardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_ip** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_k8s_port_forward_request import PatchedK8sPortForwardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedK8sPortForwardRequest from a JSON string
patched_k8s_port_forward_request_instance = PatchedK8sPortForwardRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedK8sPortForwardRequest.to_json())

# convert the object into a dict
patched_k8s_port_forward_request_dict = patched_k8s_port_forward_request_instance.to_dict()
# create an instance of PatchedK8sPortForwardRequest from a dict
patched_k8s_port_forward_request_from_dict = PatchedK8sPortForwardRequest.from_dict(patched_k8s_port_forward_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


