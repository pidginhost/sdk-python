# ChangeBillingCycleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**billing_cycle** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.change_billing_cycle_response import ChangeBillingCycleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeBillingCycleResponse from a JSON string
change_billing_cycle_response_instance = ChangeBillingCycleResponse.from_json(json)
# print the JSON string representation of the object
print(ChangeBillingCycleResponse.to_json())

# convert the object into a dict
change_billing_cycle_response_dict = change_billing_cycle_response_instance.to_dict()
# create an instance of ChangeBillingCycleResponse from a dict
change_billing_cycle_response_from_dict = ChangeBillingCycleResponse.from_dict(change_billing_cycle_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


