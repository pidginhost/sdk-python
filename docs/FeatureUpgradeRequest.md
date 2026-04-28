# FeatureUpgradeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_name** | **str** | Name of the feature to upgrade (e.g. cert-manager) | 
**retry** | **bool** | Retry a failed install | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.feature_upgrade_request import FeatureUpgradeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureUpgradeRequest from a JSON string
feature_upgrade_request_instance = FeatureUpgradeRequest.from_json(json)
# print the JSON string representation of the object
print(FeatureUpgradeRequest.to_json())

# convert the object into a dict
feature_upgrade_request_dict = feature_upgrade_request_instance.to_dict()
# create an instance of FeatureUpgradeRequest from a dict
feature_upgrade_request_from_dict = FeatureUpgradeRequest.from_dict(feature_upgrade_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


