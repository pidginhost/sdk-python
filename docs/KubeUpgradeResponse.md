# KubeUpgradeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.kube_upgrade_response import KubeUpgradeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KubeUpgradeResponse from a JSON string
kube_upgrade_response_instance = KubeUpgradeResponse.from_json(json)
# print the JSON string representation of the object
print(KubeUpgradeResponse.to_json())

# convert the object into a dict
kube_upgrade_response_dict = kube_upgrade_response_instance.to_dict()
# create an instance of KubeUpgradeResponse from a dict
kube_upgrade_response_from_dict = KubeUpgradeResponse.from_dict(kube_upgrade_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


