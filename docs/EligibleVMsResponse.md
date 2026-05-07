# EligibleVMsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vms** | [**List[EligibleVM]**](EligibleVM.md) |  | 

## Example

```python
from pidginhost_sdk.models.eligible_vms_response import EligibleVMsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EligibleVMsResponse from a JSON string
eligible_vms_response_instance = EligibleVMsResponse.from_json(json)
# print the JSON string representation of the object
print(EligibleVMsResponse.to_json())

# convert the object into a dict
eligible_vms_response_dict = eligible_vms_response_instance.to_dict()
# create an instance of EligibleVMsResponse from a dict
eligible_vms_response_from_dict = EligibleVMsResponse.from_dict(eligible_vms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


