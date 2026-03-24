# InvoiceDetail


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
**product_info** | **object** |  | [readonly] 
**client_info** | **object** |  | [readonly] 
**invoice_info** | **object** |  | [readonly] 
**payment_method** | **str** |  | [readonly] 
**services** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.invoice_detail import InvoiceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetail from a JSON string
invoice_detail_instance = InvoiceDetail.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetail.to_json())

# convert the object into a dict
invoice_detail_dict = invoice_detail_instance.to_dict()
# create an instance of InvoiceDetail from a dict
invoice_detail_from_dict = InvoiceDetail.from_dict(invoice_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


