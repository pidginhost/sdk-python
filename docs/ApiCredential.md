# ApiCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**label** | **str** |  | [readonly] 
**key_prefix** | **str** |  | [readonly] 
**last_used_at** | **str** |  | [readonly] 
**active** | **bool** |  | [readonly] 
**created_at** | **str** |  | [readonly] 
**revoked_at** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.api_credential import ApiCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCredential from a JSON string
api_credential_instance = ApiCredential.from_json(json)
# print the JSON string representation of the object
print(ApiCredential.to_json())

# convert the object into a dict
api_credential_dict = api_credential_instance.to_dict()
# create an instance of ApiCredential from a dict
api_credential_from_dict = ApiCredential.from_dict(api_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


