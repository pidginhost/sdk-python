# PatchedCompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**cif_vat** | **str** |  | [optional] 
**reg** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**bank** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**address** | [**AddressRequest**](AddressRequest.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.patched_company_request import PatchedCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCompanyRequest from a JSON string
patched_company_request_instance = PatchedCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedCompanyRequest.to_json())

# convert the object into a dict
patched_company_request_dict = patched_company_request_instance.to_dict()
# create an instance of PatchedCompanyRequest from a dict
patched_company_request_from_dict = PatchedCompanyRequest.from_dict(patched_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


