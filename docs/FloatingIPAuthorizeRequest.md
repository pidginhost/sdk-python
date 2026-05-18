# FloatingIPAuthorizeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.floating_ip_authorize_request import FloatingIPAuthorizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIPAuthorizeRequest from a JSON string
floating_ip_authorize_request_instance = FloatingIPAuthorizeRequest.from_json(json)
# print the JSON string representation of the object
print(FloatingIPAuthorizeRequest.to_json())

# convert the object into a dict
floating_ip_authorize_request_dict = floating_ip_authorize_request_instance.to_dict()
# create an instance of FloatingIPAuthorizeRequest from a dict
floating_ip_authorize_request_from_dict = FloatingIPAuthorizeRequest.from_dict(floating_ip_authorize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


