# Bucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**full_name** | **str** |  | [readonly] 
**quota_gb** | **int** |  | [readonly] 
**used_bytes** | **int** |  | [readonly] 
**object_count** | **int** |  | [readonly] 
**public_read** | **bool** |  | [readonly] 
**status** | [**ResourceStatusEnum**](ResourceStatusEnum.md) |  | [readonly] 
**endpoint** | **str** |  | [readonly] 
**region** | **str** |  | [readonly] 
**created** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.bucket import Bucket

# TODO update the JSON string below
json = "{}"
# create an instance of Bucket from a JSON string
bucket_instance = Bucket.from_json(json)
# print the JSON string representation of the object
print(Bucket.to_json())

# convert the object into a dict
bucket_dict = bucket_instance.to_dict()
# create an instance of Bucket from a dict
bucket_from_dict = Bucket.from_dict(bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


