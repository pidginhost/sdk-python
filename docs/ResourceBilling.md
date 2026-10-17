# ResourceBilling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **decimal.Decimal** |  | 
**currency** | **str** |  | 
**tax_included** | **bool** |  | 
**cycle_months** | **int** |  | 
**cycle_label** | **str** |  | 
**next_invoice** | **date** |  | 
**profile** | [**ResourceBillingProfile**](ResourceBillingProfile.md) |  | 
**metered** | **bool** |  | 
**included** | **bool** |  | 
**hourly_amount** | **decimal.Decimal** |  | [optional] 
**monthly_total** | **decimal.Decimal** |  | [optional] 
**components** | **Dict[str, decimal.Decimal]** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.resource_billing import ResourceBilling

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceBilling from a JSON string
resource_billing_instance = ResourceBilling.from_json(json)
# print the JSON string representation of the object
print(ResourceBilling.to_json())

# convert the object into a dict
resource_billing_dict = resource_billing_instance.to_dict()
# create an instance of ResourceBilling from a dict
resource_billing_from_dict = ResourceBilling.from_dict(resource_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


