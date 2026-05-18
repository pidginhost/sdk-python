# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**company** | **int** |  | [optional] 
**billing_cycle** | **int** |  | [readonly] 
**hostname** | **str** |  | [readonly] 
**price** | **decimal.Decimal** | Euro without TVA | [readonly] 
**status** | [**Status63aEnum**](Status63aEnum.md) |  | [readonly] 
**created** | **str** |  | [readonly] 
**modified** | **str** |  | [readonly] 
**terminated** | **date** |  | [readonly] 
**next_invoice** | **date** |  | [readonly] 
**primary_service** | **int** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


