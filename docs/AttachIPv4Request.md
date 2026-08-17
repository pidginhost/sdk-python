# AttachIPv4Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **str** | ID or address of an IPv4 you own. | 
**reboot** | **bool** | Restart the server so the guest OS picks up the address. | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.attach_ipv4_request import AttachIPv4Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachIPv4Request from a JSON string
attach_ipv4_request_instance = AttachIPv4Request.from_json(json)
# print the JSON string representation of the object
print(AttachIPv4Request.to_json())

# convert the object into a dict
attach_ipv4_request_dict = attach_ipv4_request_instance.to_dict()
# create an instance of AttachIPv4Request from a dict
attach_ipv4_request_from_dict = AttachIPv4Request.from_dict(attach_ipv4_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


