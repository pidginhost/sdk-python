# BucketResizeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota_gb** | **int** |  | 

## Example

```python
from pidginhost_sdk.models.bucket_resize_request import BucketResizeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BucketResizeRequest from a JSON string
bucket_resize_request_instance = BucketResizeRequest.from_json(json)
# print the JSON string representation of the object
print(BucketResizeRequest.to_json())

# convert the object into a dict
bucket_resize_request_dict = bucket_resize_request_instance.to_dict()
# create an instance of BucketResizeRequest from a dict
bucket_resize_request_from_dict = BucketResizeRequest.from_dict(bucket_resize_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


