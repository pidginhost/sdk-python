# DNSGlueRequest

A glue / \"personal DNS\" record: registers a child nameserver host at the registry as ``<name>.<domain>`` pointing at ``ip`` (and optional ``ip2``). Required before another domain can delegate to that nameserver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | only subdomain part | 
**ip** | **str** |  | 
**ip2** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.dns_glue_request import DNSGlueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DNSGlueRequest from a JSON string
dns_glue_request_instance = DNSGlueRequest.from_json(json)
# print the JSON string representation of the object
print(DNSGlueRequest.to_json())

# convert the object into a dict
dns_glue_request_dict = dns_glue_request_instance.to_dict()
# create an instance of DNSGlueRequest from a dict
dns_glue_request_from_dict = DNSGlueRequest.from_dict(dns_glue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


