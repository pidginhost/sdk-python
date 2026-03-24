# FeatureUpgradeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.feature_upgrade_response import FeatureUpgradeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureUpgradeResponse from a JSON string
feature_upgrade_response_instance = FeatureUpgradeResponse.from_json(json)
# print the JSON string representation of the object
print(FeatureUpgradeResponse.to_json())

# convert the object into a dict
feature_upgrade_response_dict = feature_upgrade_response_instance.to_dict()
# create an instance of FeatureUpgradeResponse from a dict
feature_upgrade_response_from_dict = FeatureUpgradeResponse.from_dict(feature_upgrade_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


