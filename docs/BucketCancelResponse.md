# BucketCancelResponse

Body of the 202 answered by ``BucketViewSet.destroy``.  Deletion is asynchronous, so the route cannot answer 204: the caller needs the id it cancelled and the status it moved to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.bucket_cancel_response import BucketCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BucketCancelResponse from a JSON string
bucket_cancel_response_instance = BucketCancelResponse.from_json(json)
# print the JSON string representation of the object
print(BucketCancelResponse.to_json())

# convert the object into a dict
bucket_cancel_response_dict = bucket_cancel_response_instance.to_dict()
# create an instance of BucketCancelResponse from a dict
bucket_cancel_response_from_dict = BucketCancelResponse.from_dict(bucket_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


