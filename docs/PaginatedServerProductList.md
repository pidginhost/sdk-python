# PaginatedServerProductList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ServerProduct]**](ServerProduct.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_server_product_list import PaginatedServerProductList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedServerProductList from a JSON string
paginated_server_product_list_instance = PaginatedServerProductList.from_json(json)
# print the JSON string representation of the object
print(PaginatedServerProductList.to_json())

# convert the object into a dict
paginated_server_product_list_dict = paginated_server_product_list_instance.to_dict()
# create an instance of PaginatedServerProductList from a dict
paginated_server_product_list_from_dict = PaginatedServerProductList.from_dict(paginated_server_product_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


