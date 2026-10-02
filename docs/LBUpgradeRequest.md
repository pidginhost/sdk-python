# LBUpgradeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Return the computed plan without performing it | [optional] [default to False]
**inspection_id** | **str** | The plan identifier returned by a dry run | [optional] 

## Example

```python
from pidginhost_sdk.models.lb_upgrade_request import LBUpgradeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LBUpgradeRequest from a JSON string
lb_upgrade_request_instance = LBUpgradeRequest.from_json(json)
# print the JSON string representation of the object
print(LBUpgradeRequest.to_json())

# convert the object into a dict
lb_upgrade_request_dict = lb_upgrade_request_instance.to_dict()
# create an instance of LBUpgradeRequest from a dict
lb_upgrade_request_from_dict = LBUpgradeRequest.from_dict(lb_upgrade_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


