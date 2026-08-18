# PaginatedK8sPortForwardList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[K8sPortForward]**](K8sPortForward.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_k8s_port_forward_list import PaginatedK8sPortForwardList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedK8sPortForwardList from a JSON string
paginated_k8s_port_forward_list_instance = PaginatedK8sPortForwardList.from_json(json)
# print the JSON string representation of the object
print(PaginatedK8sPortForwardList.to_json())

# convert the object into a dict
paginated_k8s_port_forward_list_dict = paginated_k8s_port_forward_list_instance.to_dict()
# create an instance of PaginatedK8sPortForwardList from a dict
paginated_k8s_port_forward_list_from_dict = PaginatedK8sPortForwardList.from_dict(paginated_k8s_port_forward_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


