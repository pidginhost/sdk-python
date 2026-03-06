# CancelServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.cancel_service_response import CancelServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelServiceResponse from a JSON string
cancel_service_response_instance = CancelServiceResponse.from_json(json)
# print the JSON string representation of the object
print(CancelServiceResponse.to_json())

# convert the object into a dict
cancel_service_response_dict = cancel_service_response_instance.to_dict()
# create an instance of CancelServiceResponse from a dict
cancel_service_response_from_dict = CancelServiceResponse.from_dict(cancel_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


