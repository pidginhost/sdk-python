# LBReimageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** | The plan_id returned by GET | 
**confirmation** | **str** | The cluster&#39;s name, typed to confirm | 

## Example

```python
from pidginhost_sdk.models.lb_reimage_request import LBReimageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LBReimageRequest from a JSON string
lb_reimage_request_instance = LBReimageRequest.from_json(json)
# print the JSON string representation of the object
print(LBReimageRequest.to_json())

# convert the object into a dict
lb_reimage_request_dict = lb_reimage_request_instance.to_dict()
# create an instance of LBReimageRequest from a dict
lb_reimage_request_from_dict = LBReimageRequest.from_dict(lb_reimage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


