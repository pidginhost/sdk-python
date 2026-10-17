# DNSRecord

Read-only representation of a DNS record from the cPanel zone dump.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**ttl** | **int** |  | [readonly] 
**type** | **str** |  | [readonly] 
**address** | **str** |  | [optional] 
**cname** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**preference** | **int** |  | [optional] 
**txtdata** | **str** |  | [optional] 
**unencoded** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**weight** | **int** |  | [optional] 
**port** | **int** |  | [optional] 
**flag** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

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


