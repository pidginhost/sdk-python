# DashboardBilling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **str** |  | 
**unpaid_count** | **int** |  | 
**unpaid_total** | **str** |  | 
**invoices** | [**List[InvoiceList]**](InvoiceList.md) |  | 

## Example

```python
from pidginhost_sdk.models.dashboard_billing import DashboardBilling

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardBilling from a JSON string
dashboard_billing_instance = DashboardBilling.from_json(json)
# print the JSON string representation of the object
print(DashboardBilling.to_json())

# convert the object into a dict
dashboard_billing_dict = dashboard_billing_instance.to_dict()
# create an instance of DashboardBilling from a dict
dashboard_billing_from_dict = DashboardBilling.from_dict(dashboard_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


