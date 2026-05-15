# FloatingIPv6


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
from pidginhost_sdk.models.floating_ipv6 import FloatingIPv6

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIPv6 from a JSON string
floating_ipv6_instance = FloatingIPv6.from_json(json)
# print the JSON string representation of the object
print(FloatingIPv6.to_json())

# convert the object into a dict
floating_ipv6_dict = floating_ipv6_instance.to_dict()
# create an instance of FloatingIPv6 from a dict
floating_ipv6_from_dict = FloatingIPv6.from_dict(floating_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


