# DNSRecordMutateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**record** | [**DNSRecord**](DNSRecord.md) |  | [optional] 

## Example

```python
from pidginhost_sdk.models.dns_record_mutate_response import DNSRecordMutateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DNSRecordMutateResponse from a JSON string
dns_record_mutate_response_instance = DNSRecordMutateResponse.from_json(json)
# print the JSON string representation of the object
print(DNSRecordMutateResponse.to_json())

# convert the object into a dict
dns_record_mutate_response_dict = dns_record_mutate_response_instance.to_dict()
# create an instance of DNSRecordMutateResponse from a dict
dns_record_mutate_response_from_dict = DNSRecordMutateResponse.from_dict(dns_record_mutate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


