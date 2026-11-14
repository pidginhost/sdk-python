# LBReimageOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** |  | 
**state** | [**LBReimageOperationStateEnum**](LBReimageOperationStateEnum.md) |  | 
**rollback_until** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.lb_reimage_operation import LBReimageOperation

# TODO update the JSON string below
json = "{}"
# create an instance of LBReimageOperation from a JSON string
lb_reimage_operation_instance = LBReimageOperation.from_json(json)
# print the JSON string representation of the object
print(LBReimageOperation.to_json())

# convert the object into a dict
lb_reimage_operation_dict = lb_reimage_operation_instance.to_dict()
# create an instance of LBReimageOperation from a dict
lb_reimage_operation_from_dict = LBReimageOperation.from_dict(lb_reimage_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


