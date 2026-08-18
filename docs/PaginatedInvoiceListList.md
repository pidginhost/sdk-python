# PaginatedInvoiceListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[InvoiceList]**](InvoiceList.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_invoice_list_list import PaginatedInvoiceListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInvoiceListList from a JSON string
paginated_invoice_list_list_instance = PaginatedInvoiceListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedInvoiceListList.to_json())

# convert the object into a dict
paginated_invoice_list_list_dict = paginated_invoice_list_list_instance.to_dict()
# create an instance of PaginatedInvoiceListList from a dict
paginated_invoice_list_list_from_dict = PaginatedInvoiceListList.from_dict(paginated_invoice_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


