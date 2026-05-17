# ActivateFreeDNS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name or primary key of the domain to activate. | 
**source** | [**SourceEnum**](SourceEnum.md) | &#39;internal&#39; for domains purchased on PidginHost, &#39;external&#39; for user-added domains.  * &#x60;internal&#x60; - Internal * &#x60;external&#x60; - External | 
**ip** | **str** | IPv4 address to use as the default A record for the zone. | 

## Example

```python
from pidginhost_sdk.models.activate_free_dns import ActivateFreeDNS

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateFreeDNS from a JSON string
activate_free_dns_instance = ActivateFreeDNS.from_json(json)
# print the JSON string representation of the object
print(ActivateFreeDNS.to_json())

# convert the object into a dict
activate_free_dns_dict = activate_free_dns_instance.to_dict()
# create an instance of ActivateFreeDNS from a dict
activate_free_dns_from_dict = ActivateFreeDNS.from_dict(activate_free_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


