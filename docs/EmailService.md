# EmailService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**tier** | **str** |  | [readonly] 
**status** | [**ResourceStatusEnum**](ResourceStatusEnum.md) |  | [readonly] 
**sandbox_mode** | **bool** |  | [readonly] 
**auto_suspended** | **bool** |  | [readonly] 
**auto_suspend_reason** | **str** |  | [readonly] 
**msgs_sent_24h** | **int** |  | [readonly] 
**msgs_sent_30d** | **int** |  | [readonly] 
**bounce_rate_pct** | **decimal.Decimal** |  | [readonly] 
**complaint_rate_pct** | **decimal.Decimal** |  | [readonly] 
**dedicated_ip_addon** | **bool** |  | [readonly] 
**quota_monthly** | **str** |  | [readonly] 
**price_monthly_eur** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.email_service import EmailService

# TODO update the JSON string below
json = "{}"
# create an instance of EmailService from a JSON string
email_service_instance = EmailService.from_json(json)
# print the JSON string representation of the object
print(EmailService.to_json())

# convert the object into a dict
email_service_dict = email_service_instance.to_dict()
# create an instance of EmailService from a dict
email_service_from_dict = EmailService.from_dict(email_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


