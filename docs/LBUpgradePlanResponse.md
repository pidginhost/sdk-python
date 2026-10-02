# LBUpgradePlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inspection_id** | **str** |  | 
**convergence** | **str** |  | 
**level** | **int** |  | 
**actions** | **List[str]** |  | 
**blockers** | **List[str]** |  | 
**can_execute** | **bool** |  | 

## Example

```python
from pidginhost_sdk.models.lb_upgrade_plan_response import LBUpgradePlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LBUpgradePlanResponse from a JSON string
lb_upgrade_plan_response_instance = LBUpgradePlanResponse.from_json(json)
# print the JSON string representation of the object
print(LBUpgradePlanResponse.to_json())

# convert the object into a dict
lb_upgrade_plan_response_dict = lb_upgrade_plan_response_instance.to_dict()
# create an instance of LBUpgradePlanResponse from a dict
lb_upgrade_plan_response_from_dict = LBUpgradePlanResponse.from_dict(lb_upgrade_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


