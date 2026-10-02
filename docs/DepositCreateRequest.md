# DepositCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.deposit_create_request import DepositCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DepositCreateRequest from a JSON string
deposit_create_request_instance = DepositCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DepositCreateRequest.to_json())

# convert the object into a dict
deposit_create_request_dict = deposit_create_request_instance.to_dict()
# create an instance of DepositCreateRequest from a dict
deposit_create_request_from_dict = DepositCreateRequest.from_dict(deposit_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


