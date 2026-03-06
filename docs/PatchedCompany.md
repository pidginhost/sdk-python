# PatchedCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**cif_vat** | **str** |  | [optional] 
**reg** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**bank** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_company import PatchedCompany

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCompany from a JSON string
patched_company_instance = PatchedCompany.from_json(json)
# print the JSON string representation of the object
print(PatchedCompany.to_json())

# convert the object into a dict
patched_company_dict = patched_company_instance.to_dict()
# create an instance of PatchedCompany from a dict
patched_company_from_dict = PatchedCompany.from_dict(patched_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


