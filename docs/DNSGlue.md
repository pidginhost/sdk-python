# DNSGlue

A glue / \"personal DNS\" record: registers a child nameserver host at the registry as ``<name>.<domain>`` pointing at ``ip`` (and optional ``ip2``). Required before another domain can delegate to that nameserver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | only subdomain part | 
**ip** | **str** |  | 
**ip2** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.dns_glue import DNSGlue

# TODO update the JSON string below
json = "{}"
# create an instance of DNSGlue from a JSON string
dns_glue_instance = DNSGlue.from_json(json)
# print the JSON string representation of the object
print(DNSGlue.to_json())

# convert the object into a dict
dns_glue_dict = dns_glue_instance.to_dict()
# create an instance of DNSGlue from a dict
dns_glue_from_dict = DNSGlue.from_dict(dns_glue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


