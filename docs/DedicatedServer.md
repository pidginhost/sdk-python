# DedicatedServer

Read-only serializer for dedicated server services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**hostname** | **str** |  | [readonly] 
**status** | [**Status63aEnum**](Status63aEnum.md) |  | [readonly] 
**price** | **decimal.Decimal** | Euro without TVA | [readonly] 
**next_invoice** | **date** |  | [readonly] 
**created** | **str** |  | [readonly] 
**billing_cycle** | **str** |  | [readonly] 
**server_status** | **str** |  | [readonly] 
**ips** | **str** |  | [readonly] 
**os_name** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.dedicated_server import DedicatedServer

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServer from a JSON string
dedicated_server_instance = DedicatedServer.from_json(json)
# print the JSON string representation of the object
print(DedicatedServer.to_json())

# convert the object into a dict
dedicated_server_dict = dedicated_server_instance.to_dict()
# create an instance of DedicatedServer from a dict
dedicated_server_from_dict = DedicatedServer.from_dict(dedicated_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


