# DedicatedServerIP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**ip** | **str** |  | 
**reverse_dns** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.dedicated_server_ip import DedicatedServerIP

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServerIP from a JSON string
dedicated_server_ip_instance = DedicatedServerIP.from_json(json)
# print the JSON string representation of the object
print(DedicatedServerIP.to_json())

# convert the object into a dict
dedicated_server_ip_dict = dedicated_server_ip_instance.to_dict()
# create an instance of DedicatedServerIP from a dict
dedicated_server_ip_from_dict = DedicatedServerIP.from_dict(dedicated_server_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


