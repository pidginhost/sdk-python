# BucketCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**quota_gb** | **int** |  | 
**public_read** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.bucket_create_request import BucketCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BucketCreateRequest from a JSON string
bucket_create_request_instance = BucketCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BucketCreateRequest.to_json())

# convert the object into a dict
bucket_create_request_dict = bucket_create_request_instance.to_dict()
# create an instance of BucketCreateRequest from a dict
bucket_create_request_from_dict = BucketCreateRequest.from_dict(bucket_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


