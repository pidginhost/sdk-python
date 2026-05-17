# FloatingIPv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**address** | **str** |  | [readonly] 
**gateway** | **str** |  | [readonly] 
**prefix** | **int** |  | [readonly] 
**label** | **str** |  | [optional] 
**authorized_vm_count** | **int** |  | [readonly] 
**created_at** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.floating_ipv4 import FloatingIPv4

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIPv4 from a JSON string
floating_ipv4_instance = FloatingIPv4.from_json(json)
# print the JSON string representation of the object
print(FloatingIPv4.to_json())

# convert the object into a dict
floating_ipv4_dict = floating_ipv4_instance.to_dict()
# create an instance of FloatingIPv4 from a dict
floating_ipv4_from_dict = FloatingIPv4.from_dict(floating_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


