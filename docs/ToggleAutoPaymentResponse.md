# ToggleAutoPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**auto_payment** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.toggle_auto_payment_response import ToggleAutoPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleAutoPaymentResponse from a JSON string
toggle_auto_payment_response_instance = ToggleAutoPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(ToggleAutoPaymentResponse.to_json())

# convert the object into a dict
toggle_auto_payment_response_dict = toggle_auto_payment_response_instance.to_dict()
# create an instance of ToggleAutoPaymentResponse from a dict
toggle_auto_payment_response_from_dict = ToggleAutoPaymentResponse.from_dict(toggle_auto_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


