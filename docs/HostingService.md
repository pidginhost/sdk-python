# HostingService

Read-only serializer for shared/cPanel hosting services.

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
**package_name** | **str** |  | [readonly] 
**node_url** | **str** |  | [readonly] 
**username** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.hosting_service import HostingService

# TODO update the JSON string below
json = "{}"
# create an instance of HostingService from a JSON string
hosting_service_instance = HostingService.from_json(json)
# print the JSON string representation of the object
print(HostingService.to_json())

# convert the object into a dict
hosting_service_dict = hosting_service_instance.to_dict()
# create an instance of HostingService from a dict
hosting_service_from_dict = HostingService.from_dict(hosting_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


