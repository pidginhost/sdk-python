# DedicatedServerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**status_text** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.dedicated_server_status import DedicatedServerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServerStatus from a JSON string
dedicated_server_status_instance = DedicatedServerStatus.from_json(json)
# print the JSON string representation of the object
print(DedicatedServerStatus.to_json())

# convert the object into a dict
dedicated_server_status_dict = dedicated_server_status_instance.to_dict()
# create an instance of DedicatedServerStatus from a dict
dedicated_server_status_from_dict = DedicatedServerStatus.from_dict(dedicated_server_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


