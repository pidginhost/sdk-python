# LBReimageStart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** |  | 
**reason** | [**LBReimageAvailabilityEnum**](LBReimageAvailabilityEnum.md) | Why no start is possible now: busy (try later) or unavailable  * &#x60;busy&#x60; - busy * &#x60;unavailable&#x60; - unavailable | 
**plan_id** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.lb_reimage_start import LBReimageStart

# TODO update the JSON string below
json = "{}"
# create an instance of LBReimageStart from a JSON string
lb_reimage_start_instance = LBReimageStart.from_json(json)
# print the JSON string representation of the object
print(LBReimageStart.to_json())

# convert the object into a dict
lb_reimage_start_dict = lb_reimage_start_instance.to_dict()
# create an instance of LBReimageStart from a dict
lb_reimage_start_from_dict = LBReimageStart.from_dict(lb_reimage_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


