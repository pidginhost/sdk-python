# CompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cif_vat** | **str** |  | [optional] 
**reg** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**bank** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**address** | [**AddressRequest**](AddressRequest.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.company_request import CompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyRequest from a JSON string
company_request_instance = CompanyRequest.from_json(json)
# print the JSON string representation of the object
print(CompanyRequest.to_json())

# convert the object into a dict
company_request_dict = company_request_instance.to_dict()
# create an instance of CompanyRequest from a dict
company_request_from_dict = CompanyRequest.from_dict(company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


