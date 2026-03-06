# EligibleVM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**hostname** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.eligible_vm import EligibleVM

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleVM from a JSON string
eligible_vm_instance = EligibleVM.from_json(json)
# print the JSON string representation of the object
print(EligibleVM.to_json())

# convert the object into a dict
eligible_vm_dict = eligible_vm_instance.to_dict()
# create an instance of EligibleVM from a dict
eligible_vm_from_dict = EligibleVM.from_dict(eligible_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


