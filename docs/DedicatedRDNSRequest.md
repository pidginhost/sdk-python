# DedicatedRDNSRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_id** | **int** |  | 
**reverse_dns** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.dedicated_rdns_request import DedicatedRDNSRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedRDNSRequest from a JSON string
dedicated_rdns_request_instance = DedicatedRDNSRequest.from_json(json)
# print the JSON string representation of the object
print(DedicatedRDNSRequest.to_json())

# convert the object into a dict
dedicated_rdns_request_dict = dedicated_rdns_request_instance.to_dict()
# create an instance of DedicatedRDNSRequest from a dict
dedicated_rdns_request_from_dict = DedicatedRDNSRequest.from_dict(dedicated_rdns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


