# SuppressionAddRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**detail** | **str** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.suppression_add_request import SuppressionAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SuppressionAddRequest from a JSON string
suppression_add_request_instance = SuppressionAddRequest.from_json(json)
# print the JSON string representation of the object
print(SuppressionAddRequest.to_json())

# convert the object into a dict
suppression_add_request_dict = suppression_add_request_instance.to_dict()
# create an instance of SuppressionAddRequest from a dict
suppression_add_request_from_dict = SuppressionAddRequest.from_dict(suppression_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


