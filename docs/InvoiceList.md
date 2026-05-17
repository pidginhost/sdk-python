# InvoiceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**number_proforma** | **str** |  | [readonly] 
**number_fiscal** | **str** |  | [readonly] 
**status** | [**Status03cEnum**](Status03cEnum.md) |  | [readonly] 
**subtotal** | **decimal.Decimal** |  | [readonly] 
**vat_value** | **decimal.Decimal** |  | [readonly] 
**vat_percentage** | **int** |  | [readonly] 
**total** | **decimal.Decimal** |  | [readonly] 
**invoice_date** | **date** |  | [readonly] 
**due_date** | **date** |  | [readonly] 
**payment_date** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.invoice_list import InvoiceList

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceList from a JSON string
invoice_list_instance = InvoiceList.from_json(json)
# print the JSON string representation of the object
print(InvoiceList.to_json())

# convert the object into a dict
invoice_list_dict = invoice_list_instance.to_dict()
# create an instance of InvoiceList from a dict
invoice_list_from_dict = InvoiceList.from_dict(invoice_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


