# PaginatedOSImageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OSImage]**](OSImage.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_os_image_list import PaginatedOSImageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOSImageList from a JSON string
paginated_os_image_list_instance = PaginatedOSImageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOSImageList.to_json())

# convert the object into a dict
paginated_os_image_list_dict = paginated_os_image_list_instance.to_dict()
# create an instance of PaginatedOSImageList from a dict
paginated_os_image_list_from_dict = PaginatedOSImageList.from_dict(paginated_os_image_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


