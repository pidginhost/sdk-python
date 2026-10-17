# InvoiceLocalAmounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**CurrencyEnum**](CurrencyEnum.md) |  | 
**subtotal** | **decimal.Decimal** |  | 
**vat_value** | **decimal.Decimal** |  | 
**total** | **decimal.Decimal** |  | 
**primary** | **bool** | True for a Romanian beneficiary (the rule that picks the PDF language); show RON first. | 

## Example

```python
from pidginhost_sdk.models.invoice_local_amounts import InvoiceLocalAmounts

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLocalAmounts from a JSON string
invoice_local_amounts_instance = InvoiceLocalAmounts.from_json(json)
# print the JSON string representation of the object
print(InvoiceLocalAmounts.to_json())

# convert the object into a dict
invoice_local_amounts_dict = invoice_local_amounts_instance.to_dict()
# create an instance of InvoiceLocalAmounts from a dict
invoice_local_amounts_from_dict = InvoiceLocalAmounts.from_dict(invoice_local_amounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


