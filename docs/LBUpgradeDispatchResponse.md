# LBUpgradeDispatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.lb_upgrade_dispatch_response import LBUpgradeDispatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LBUpgradeDispatchResponse from a JSON string
lb_upgrade_dispatch_response_instance = LBUpgradeDispatchResponse.from_json(json)
# print the JSON string representation of the object
print(LBUpgradeDispatchResponse.to_json())

# convert the object into a dict
lb_upgrade_dispatch_response_dict = lb_upgrade_dispatch_response_instance.to_dict()
# create an instance of LBUpgradeDispatchResponse from a dict
lb_upgrade_dispatch_response_from_dict = LBUpgradeDispatchResponse.from_dict(lb_upgrade_dispatch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


