# ChangeBillingCycleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cycle_id** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.change_billing_cycle_request import ChangeBillingCycleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeBillingCycleRequest from a JSON string
change_billing_cycle_request_instance = ChangeBillingCycleRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeBillingCycleRequest.to_json())

# convert the object into a dict
change_billing_cycle_request_dict = change_billing_cycle_request_instance.to_dict()
# create an instance of ChangeBillingCycleRequest from a dict
change_billing_cycle_request_from_dict = ChangeBillingCycleRequest.from_dict(change_billing_cycle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


