# CheckAvailabilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain with tld, ex: example.com | 

## Example

```python
from pidginhost_sdk.models.check_availability_request import CheckAvailabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAvailabilityRequest from a JSON string
check_availability_request_instance = CheckAvailabilityRequest.from_json(json)
# print the JSON string representation of the object
print(CheckAvailabilityRequest.to_json())

# convert the object into a dict
check_availability_request_dict = check_availability_request_instance.to_dict()
# create an instance of CheckAvailabilityRequest from a dict
check_availability_request_from_dict = CheckAvailabilityRequest.from_dict(check_availability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


