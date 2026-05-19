# DNSRecordCreate

Validate input for creating or editing a DNS record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Record hostname (use &#39;@&#39; or leave empty for zone apex). | 
**ttl** | **int** | Time to live in seconds. | 
**type** | [**DNSRecordCreateTypeEnum**](DNSRecordCreateTypeEnum.md) | DNS record type.  * &#x60;A&#x60; - A * &#x60;AAAA&#x60; - AAAA * &#x60;TYPE257&#x60; - TYPE257 * &#x60;CNAME&#x60; - CNAME * &#x60;MX&#x60; - MX * &#x60;SRV&#x60; - SRV * &#x60;TXT&#x60; - TXT | 
**address** | **str** | IPv4/IPv6 address (A/AAAA). | [optional] 
**cname** | **str** | Canonical name (CNAME). | [optional] 
**exchange** | **str** | Mail exchange host (MX). | [optional] 
**preference** | **int** | MX preference / priority. | [optional] 
**txtdata** | **str** | TXT record data. | [optional] 
**unencoded** | **str** | Unencoded TXT value. | [optional] 
**target** | **str** | SRV target host. | [optional] 
**priority** | **int** | SRV priority. | [optional] 
**weight** | **int** | SRV weight. | [optional] 
**port** | **int** | SRV port. | [optional] 
**flag** | **int** | CAA flag (TYPE257). | [optional] 
**tag** | **str** | CAA tag (TYPE257). | [optional] 
**value** | **str** | CAA value (TYPE257). | [optional] 
**line** | **int** | Line number of existing record to edit. Omit to add a new record. | [optional] 

## Example

```python
from pidginhost_sdk.models.dns_record_create import DNSRecordCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DNSRecordCreate from a JSON string
dns_record_create_instance = DNSRecordCreate.from_json(json)
# print the JSON string representation of the object
print(DNSRecordCreate.to_json())

# convert the object into a dict
dns_record_create_dict = dns_record_create_instance.to_dict()
# create an instance of DNSRecordCreate from a dict
dns_record_create_from_dict = DNSRecordCreate.from_dict(dns_record_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


