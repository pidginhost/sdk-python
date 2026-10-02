# ActivateFreeDNSRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name or primary key of the domain to activate. | 
**source** | [**SourceEnum**](SourceEnum.md) | &#39;internal&#39; for domains purchased on PidginHost, &#39;external&#39; for user-added domains.  * &#x60;internal&#x60; - Internal * &#x60;external&#x60; - External | 
**ip** | **str** | IPv4 address to use as the default A record for the zone. | 

## Example

```python
from pidginhost_sdk.models.activate_free_dns_request import ActivateFreeDNSRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateFreeDNSRequest from a JSON string
activate_free_dns_request_instance = ActivateFreeDNSRequest.from_json(json)
# print the JSON string representation of the object
print(ActivateFreeDNSRequest.to_json())

# convert the object into a dict
activate_free_dns_request_dict = activate_free_dns_request_instance.to_dict()
# create an instance of ActivateFreeDNSRequest from a dict
activate_free_dns_request_from_dict = ActivateFreeDNSRequest.from_dict(activate_free_dns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


