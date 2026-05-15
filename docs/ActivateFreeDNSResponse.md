# ActivateFreeDNSResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**domain** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.activate_free_dns_response import ActivateFreeDNSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateFreeDNSResponse from a JSON string
activate_free_dns_response_instance = ActivateFreeDNSResponse.from_json(json)
# print the JSON string representation of the object
print(ActivateFreeDNSResponse.to_json())

# convert the object into a dict
activate_free_dns_response_dict = activate_free_dns_response_instance.to_dict()
# create an instance of ActivateFreeDNSResponse from a dict
activate_free_dns_response_from_dict = ActivateFreeDNSResponse.from_dict(activate_free_dns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


