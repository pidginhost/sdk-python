# SandboxAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**address** | **str** |  | 
**verified_at** | **str** |  | [readonly] 
**created_at** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.sandbox_address import SandboxAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SandboxAddress from a JSON string
sandbox_address_instance = SandboxAddress.from_json(json)
# print the JSON string representation of the object
print(SandboxAddress.to_json())

# convert the object into a dict
sandbox_address_dict = sandbox_address_instance.to_dict()
# create an instance of SandboxAddress from a dict
sandbox_address_from_dict = SandboxAddress.from_dict(sandbox_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


