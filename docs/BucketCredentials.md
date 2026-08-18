# BucketCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**endpoint** | **str** |  | 
**region** | **str** |  | 
**access_key** | **str** |  | 
**secret_key** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.bucket_credentials import BucketCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of BucketCredentials from a JSON string
bucket_credentials_instance = BucketCredentials.from_json(json)
# print the JSON string representation of the object
print(BucketCredentials.to_json())

# convert the object into a dict
bucket_credentials_dict = bucket_credentials_instance.to_dict()
# create an instance of BucketCredentials from a dict
bucket_credentials_from_dict = BucketCredentials.from_dict(bucket_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


