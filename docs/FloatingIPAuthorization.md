# FloatingIPAuthorization

Read-only authorization row for either v4 or v6 (shape is identical).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**server_id** | **int** |  | [readonly] 
**server_hostname** | **str** |  | [readonly] 
**created_at** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.floating_ip_authorization import FloatingIPAuthorization

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIPAuthorization from a JSON string
floating_ip_authorization_instance = FloatingIPAuthorization.from_json(json)
# print the JSON string representation of the object
print(FloatingIPAuthorization.to_json())

# convert the object into a dict
floating_ip_authorization_dict = floating_ip_authorization_instance.to_dict()
# create an instance of FloatingIPAuthorization from a dict
floating_ip_authorization_from_dict = FloatingIPAuthorization.from_dict(floating_ip_authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


