# PaginatedStorageProductList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[StorageProduct]**](StorageProduct.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_storage_product_list import PaginatedStorageProductList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedStorageProductList from a JSON string
paginated_storage_product_list_instance = PaginatedStorageProductList.from_json(json)
# print the JSON string representation of the object
print(PaginatedStorageProductList.to_json())

# convert the object into a dict
paginated_storage_product_list_dict = paginated_storage_product_list_instance.to_dict()
# create an instance of PaginatedStorageProductList from a dict
paginated_storage_product_list_from_dict = PaginatedStorageProductList.from_dict(paginated_storage_product_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


