# DedicatedRDNS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_id** | **int** |  | 
**reverse_dns** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.dedicated_rdns import DedicatedRDNS

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedRDNS from a JSON string
dedicated_rdns_instance = DedicatedRDNS.from_json(json)
# print the JSON string representation of the object
print(DedicatedRDNS.to_json())

# convert the object into a dict
dedicated_rdns_dict = dedicated_rdns_instance.to_dict()
# create an instance of DedicatedRDNS from a dict
dedicated_rdns_from_dict = DedicatedRDNS.from_dict(dedicated_rdns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


