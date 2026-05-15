# SendingDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**status** | [**SendingDomainStatusEnum**](SendingDomainStatusEnum.md) |  | [readonly] 
**dns_source** | [**DnsSourceEnum**](DnsSourceEnum.md) |  | [readonly] 
**use_inbound** | **bool** |  | [readonly] 
**dkim_selector** | **str** |  | [readonly] 
**dkim_record** | **str** |  | [readonly] 
**spf_record** | **str** |  | [readonly] 
**dmarc_record** | **str** |  | [readonly] 
**verified_at** | **str** |  | [readonly] 
**last_check_at** | **str** |  | [readonly] 
**last_check_errors** | **object** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.sending_domain import SendingDomain

# TODO update the JSON string below
json = "{}"
# create an instance of SendingDomain from a JSON string
sending_domain_instance = SendingDomain.from_json(json)
# print the JSON string representation of the object
print(SendingDomain.to_json())

# convert the object into a dict
sending_domain_dict = sending_domain_instance.to_dict()
# create an instance of SendingDomain from a dict
sending_domain_from_dict = SendingDomain.from_dict(sending_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


