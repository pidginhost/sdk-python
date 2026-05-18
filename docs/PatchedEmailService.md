# PatchedEmailService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**tier** | **str** |  | [optional] [readonly] 
**status** | [**StatusA57Enum**](StatusA57Enum.md) |  | [optional] [readonly] 
**sandbox_mode** | **bool** |  | [optional] [readonly] 
**auto_suspended** | **bool** |  | [optional] [readonly] 
**auto_suspend_reason** | **str** |  | [optional] [readonly] 
**msgs_sent_24h** | **int** |  | [optional] [readonly] 
**msgs_sent_30d** | **int** |  | [optional] [readonly] 
**bounce_rate_pct** | **decimal.Decimal** |  | [optional] [readonly] 
**complaint_rate_pct** | **decimal.Decimal** |  | [optional] [readonly] 
**dedicated_ip_addon** | **bool** |  | [optional] [readonly] 
**quota_monthly** | **str** |  | [optional] [readonly] 
**price_monthly_eur** | **str** |  | [optional] [readonly] 

## Example

```python
from pidginhost_sdk.models.patched_email_service import PatchedEmailService

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEmailService from a JSON string
patched_email_service_instance = PatchedEmailService.from_json(json)
# print the JSON string representation of the object
print(PatchedEmailService.to_json())

# convert the object into a dict
patched_email_service_dict = patched_email_service_instance.to_dict()
# create an instance of PatchedEmailService from a dict
patched_email_service_from_dict = PatchedEmailService.from_dict(patched_email_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


