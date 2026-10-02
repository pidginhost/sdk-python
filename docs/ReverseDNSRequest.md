# ReverseDNSRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reverse_dns** | **str** | Fully-qualified domain name for PTR record (e.g., host.example.com) | 

## Example

```python
from pidginhost_sdk.models.reverse_dns_request import ReverseDNSRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseDNSRequest from a JSON string
reverse_dns_request_instance = ReverseDNSRequest.from_json(json)
# print the JSON string representation of the object
print(ReverseDNSRequest.to_json())

# convert the object into a dict
reverse_dns_request_dict = reverse_dns_request_instance.to_dict()
# create an instance of ReverseDNSRequest from a dict
reverse_dns_request_from_dict = ReverseDNSRequest.from_dict(reverse_dns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


