# TransferRoDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain with tld, ex: example.com | 
**auth_code** | **str** | Auth code | 

## Example

```python
from pidginhost_sdk.models.transfer_ro_domain_request import TransferRoDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRoDomainRequest from a JSON string
transfer_ro_domain_request_instance = TransferRoDomainRequest.from_json(json)
# print the JSON string representation of the object
print(TransferRoDomainRequest.to_json())

# convert the object into a dict
transfer_ro_domain_request_dict = transfer_ro_domain_request_instance.to_dict()
# create an instance of TransferRoDomainRequest from a dict
transfer_ro_domain_request_from_dict = TransferRoDomainRequest.from_dict(transfer_ro_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


