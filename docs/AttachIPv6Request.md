# AttachIPv6Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6** | **str** | ID or address of an IPv6 you own. | 
**reboot** | **bool** | Restart the server so the guest OS picks up the address. | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.attach_ipv6_request import AttachIPv6Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachIPv6Request from a JSON string
attach_ipv6_request_instance = AttachIPv6Request.from_json(json)
# print the JSON string representation of the object
print(AttachIPv6Request.to_json())

# convert the object into a dict
attach_ipv6_request_dict = attach_ipv6_request_instance.to_dict()
# create an instance of AttachIPv6Request from a dict
attach_ipv6_request_from_dict = AttachIPv6Request.from_dict(attach_ipv6_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


