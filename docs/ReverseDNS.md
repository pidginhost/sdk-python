# ReverseDNS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reverse_dns** | **str** | Fully-qualified domain name for PTR record (e.g., host.example.com) | 

## Example

```python
from pidginhost_sdk.models.reverse_dns import ReverseDNS

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseDNS from a JSON string
reverse_dns_instance = ReverseDNS.from_json(json)
# print the JSON string representation of the object
print(ReverseDNS.to_json())

# convert the object into a dict
reverse_dns_dict = reverse_dns_instance.to_dict()
# create an instance of ReverseDNS from a dict
reverse_dns_from_dict = ReverseDNS.from_dict(reverse_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


