# LBReimageStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**LBReimageOperation**](LBReimageOperation.md) |  | 
**start** | [**LBReimageStart**](LBReimageStart.md) |  | 

## Example

```python
from pidginhost_sdk.models.lb_reimage_status import LBReimageStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LBReimageStatus from a JSON string
lb_reimage_status_instance = LBReimageStatus.from_json(json)
# print the JSON string representation of the object
print(LBReimageStatus.to_json())

# convert the object into a dict
lb_reimage_status_dict = lb_reimage_status_instance.to_dict()
# create an instance of LBReimageStatus from a dict
lb_reimage_status_from_dict = LBReimageStatus.from_dict(lb_reimage_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


