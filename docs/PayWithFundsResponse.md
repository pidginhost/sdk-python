# PayWithFundsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**balance** | **decimal.Decimal** |  | 

## Example

```python
from pidginhost_sdk.models.pay_with_funds_response import PayWithFundsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayWithFundsResponse from a JSON string
pay_with_funds_response_instance = PayWithFundsResponse.from_json(json)
# print the JSON string representation of the object
print(PayWithFundsResponse.to_json())

# convert the object into a dict
pay_with_funds_response_dict = pay_with_funds_response_instance.to_dict()
# create an instance of PayWithFundsResponse from a dict
pay_with_funds_response_from_dict = PayWithFundsResponse.from_dict(pay_with_funds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


