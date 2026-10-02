# FloatingIPv6CreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] [default to '']

## Example

```python
from pidginhost_sdk.models.floating_ipv6_create_request import FloatingIPv6CreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIPv6CreateRequest from a JSON string
floating_ipv6_create_request_instance = FloatingIPv6CreateRequest.from_json(json)
# print the JSON string representation of the object
print(FloatingIPv6CreateRequest.to_json())

# convert the object into a dict
floating_ipv6_create_request_dict = floating_ipv6_create_request_instance.to_dict()
# create an instance of FloatingIPv6CreateRequest from a dict
floating_ipv6_create_request_from_dict = FloatingIPv6CreateRequest.from_dict(floating_ipv6_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


