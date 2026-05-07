# TransferRoDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain with tld, ex: example.com | 
**auth_code** | **str** | Auth code | 

## Example

```python
from pidginhost_sdk.models.transfer_ro_domain import TransferRoDomain

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRoDomain from a JSON string
transfer_ro_domain_instance = TransferRoDomain.from_json(json)
# print the JSON string representation of the object
print(TransferRoDomain.to_json())

# convert the object into a dict
transfer_ro_domain_dict = transfer_ro_domain_instance.to_dict()
# create an instance of TransferRoDomain from a dict
transfer_ro_domain_from_dict = TransferRoDomain.from_dict(transfer_ro_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


