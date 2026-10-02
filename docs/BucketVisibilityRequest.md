# BucketVisibilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_read** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.bucket_visibility_request import BucketVisibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BucketVisibilityRequest from a JSON string
bucket_visibility_request_instance = BucketVisibilityRequest.from_json(json)
# print the JSON string representation of the object
print(BucketVisibilityRequest.to_json())

# convert the object into a dict
bucket_visibility_request_dict = bucket_visibility_request_instance.to_dict()
# create an instance of BucketVisibilityRequest from a dict
bucket_visibility_request_from_dict = BucketVisibilityRequest.from_dict(bucket_visibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


