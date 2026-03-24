# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**status** | [**SubscriptionStatusEnum**](SubscriptionStatusEnum.md) |  | [readonly] 
**service** | **int** |  | [readonly] 
**service_hostname** | **str** |  | [readonly] 
**subtotal** | **decimal.Decimal** |  | [readonly] 
**vat_value** | **decimal.Decimal** |  | [readonly] 
**total** | **decimal.Decimal** |  | [readonly] 
**creation_date** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


