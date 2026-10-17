# ResourceBillingProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.resource_billing_profile import ResourceBillingProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceBillingProfile from a JSON string
resource_billing_profile_instance = ResourceBillingProfile.from_json(json)
# print the JSON string representation of the object
print(ResourceBillingProfile.to_json())

# convert the object into a dict
resource_billing_profile_dict = resource_billing_profile_instance.to_dict()
# create an instance of ResourceBillingProfile from a dict
resource_billing_profile_from_dict = ResourceBillingProfile.from_dict(resource_billing_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


