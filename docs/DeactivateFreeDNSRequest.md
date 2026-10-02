# DeactivateFreeDNSRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name or primary key of the domain to deactivate. | 
**source** | [**SourceEnum**](SourceEnum.md) |  | 

## Example

```python
from pidginhost_sdk.models.deactivate_free_dns_request import DeactivateFreeDNSRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivateFreeDNSRequest from a JSON string
deactivate_free_dns_request_instance = DeactivateFreeDNSRequest.from_json(json)
# print the JSON string representation of the object
print(DeactivateFreeDNSRequest.to_json())

# convert the object into a dict
deactivate_free_dns_request_dict = deactivate_free_dns_request_instance.to_dict()
# create an instance of DeactivateFreeDNSRequest from a dict
deactivate_free_dns_request_from_dict = DeactivateFreeDNSRequest.from_dict(deactivate_free_dns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


