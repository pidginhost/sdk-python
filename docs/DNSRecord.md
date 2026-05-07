# DNSRecord

Read-only representation of a DNS record from the cPanel zone dump.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**ttl** | **int** |  | [readonly] 
**type** | **str** |  | [readonly] 
**address** | **str** |  | [readonly] 
**cname** | **str** |  | [readonly] 
**exchange** | **str** |  | [readonly] 
**preference** | **int** |  | [readonly] 
**txtdata** | **str** |  | [readonly] 
**unencoded** | **str** |  | [readonly] 
**target** | **str** |  | [readonly] 
**priority** | **int** |  | [readonly] 
**weight** | **int** |  | [readonly] 
**port** | **int** |  | [readonly] 
**flag** | **int** |  | [readonly] 
**tag** | **str** |  | [readonly] 
**value** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.dns_record import DNSRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DNSRecord from a JSON string
dns_record_instance = DNSRecord.from_json(json)
# print the JSON string representation of the object
print(DNSRecord.to_json())

# convert the object into a dict
dns_record_dict = dns_record_instance.to_dict()
# create an instance of DNSRecord from a dict
dns_record_from_dict = DNSRecord.from_dict(dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


